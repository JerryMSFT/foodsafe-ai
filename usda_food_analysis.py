import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import requests
import io
import zipfile

# Download and load USDA data
def load_usda_data():
    url = "https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_foundation_food_csv_2022-10-28.zip"
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        with z.open("food.csv") as f:
            food_df = pd.read_csv(f, low_memory=False)
        with z.open("food_nutrient.csv") as f:
            nutrient_df = pd.read_csv(f, low_memory=False)
    
    # Merge food and nutrient data
    df = food_df.merge(nutrient_df, on='fdc_id')
    return df

# Load and process USDA data
print("Loading USDA data... This may take a few minutes.")
usda_df = load_usda_data()

# Function to identify allergens
common_allergens = ['milk', 'eggs', 'peanuts', 'tree nuts', 'fish', 'shellfish', 'soy', 'wheat']
def identify_allergens(description):
    if isinstance(description, str):
        return [allergen for allergen in common_allergens if allergen in description.lower()]
    return []

# Function to estimate nutritional content
def estimate_nutrition(row):
    try:
        if row['nutrient_id'] == 1003 and row['amount'] > 20:  # Protein
            return 'high in protein'
        elif row['nutrient_id'] == 1004 and row['amount'] > 20:  # Total lipid (fat)
            return 'high in fat'
        elif row['nutrient_id'] == 1005 and row['amount'] > 50:  # Carbohydrate
            return 'high in carbohydrates'
        else:
            return 'balanced'
    except:
        return 'unknown'

# Prepare data for classification
print("Processing data...")
usda_df['allergens'] = usda_df['description'].apply(identify_allergens)
usda_df['nutrition'] = usda_df.apply(estimate_nutrition, axis=1)

# Clean description column
usda_df['clean_description'] = usda_df['description'].apply(lambda x: str(x) if isinstance(x, str) else '')

# Train a simple classifier for dietary categories
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(usda_df['clean_description'])
y_vegan = usda_df['clean_description'].apply(lambda x: 1 if 'vegan' in x.lower() else 0)
y_vegetarian = usda_df['clean_description'].apply(lambda x: 1 if 'vegetarian' in x.lower() else 0)
y_gluten_free = usda_df['clean_description'].apply(lambda x: 1 if 'gluten-free' in x.lower() else 0)

clf_vegan = MultinomialNB().fit(X, y_vegan)
clf_vegetarian = MultinomialNB().fit(X, y_vegetarian)
clf_gluten_free = MultinomialNB().fit(X, y_gluten_free)

# Function to classify dietary categories
def classify_diet(description):
    X_input = vectorizer.transform([description])
    vegan = clf_vegan.predict(X_input)[0]
    vegetarian = clf_vegetarian.predict(X_input)[0]
    gluten_free = clf_gluten_free.predict(X_input)[0]
    
    categories = []
    if vegan:
        categories.append('vegan')
    if vegetarian:
        categories.append('vegetarian')
    if gluten_free:
        categories.append('gluten-free')
    
    return categories if categories else ['none identified']

# Function to suggest substitutions
def suggest_substitutions(allergens):
    substitutions = []
    if 'milk' in allergens:
        substitutions.append('Consider substituting milk with almond milk or soy milk')
    if 'wheat' in allergens:
        substitutions.append('Consider substituting wheat flour with almond flour or coconut flour')
    if 'eggs' in allergens:
        substitutions.append('Consider substituting eggs with applesauce or mashed bananas in baking')
    return substitutions if substitutions else ['No specific substitutions suggested']

# Function to check ingredient prevalence
def ingredient_prevalence(ingredient):
    count = sum(1 for desc in usda_df['clean_description'] if ingredient.lower() in desc.lower())
    if count > len(usda_df) / 10:
        return f'{ingredient} is very common in foods'
    elif count > 0:
        return f'{ingredient} is found in some foods'
    else:
        return f'{ingredient} is not commonly found in our database of foods'

# Main analysis function
def analyze_food(food_name):
    food_data = usda_df[usda_df['clean_description'].str.contains(food_name, case=False, na=False)].iloc[0]
    allergens = identify_allergens(food_data['clean_description'])
    nutrition = food_data['nutrition']
    diet_categories = classify_diet(food_data['clean_description'])
    substitutions = suggest_substitutions(allergens)
    
    print(f"Analysis for food: {food_data['clean_description']}")
    print(f"Potential allergens: {', '.join(allergens) if allergens else 'None identified'}")
    print(f"Estimated nutritional content: {nutrition}")
    print(f"Dietary categories: {', '.join(diet_categories)}")
    print(f"Suggested substitutions: {'; '.join(substitutions)}")
    
    # Ask about specific ingredient prevalence
    while True:
        ing = input("Enter an ingredient to check its prevalence (or 'quit' to exit): ").strip()
        if ing.lower() == 'quit':
            break
        print(ingredient_prevalence(ing))

# Interactive loop
print("USDA Food Analysis Model")
print("Enter a food name, and I'll provide an analysis based on USDA data.")
while True:
    food_name = input("\nEnter a food name or 'quit' to exit: ").strip()
    if food_name.lower() == 'quit':
        break
    try:
        analyze_food(food_name)
    except IndexError:
        print(f"Sorry, I couldn't find data for '{food_name}' in the USDA database.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

