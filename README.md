# User Guide: USDA Food Analysis Model

## Introduction

The USDA Food Analysis Model is a Python-based tool that uses data from the USDA FoodData Central database to provide insights about various foods. This guide will help you set up and use the tool effectively.

## Setup

1. Ensure you have Python installed on your system (version 3.7 or higher recommended).

2. Install the required packages by running the following command in your terminal:
   ```
   pip install pandas numpy scikit-learn requests
   ```

3. Download the script file (`usda_food_analysis.py`) and save it to a directory of your choice.

## Running the Script

1. Open a terminal or command prompt.

2. Navigate to the directory containing the `usda_food_analysis.py` file.

3. Run the script using the following command:
   ```
   python usda_food_analysis.py
   ```

4. The script will start by downloading and processing the USDA data. This may take several minutes. Please be patient.

5. Once the data is loaded and processed, you'll see the prompt:
   ```
   USDA Food Analysis Model
   Enter a food name, and I'll provide an analysis based on USDA data.
   ```

## How to Use the Model

### Entering Food Names

- Type the name of a food and press Enter. For example:
  ```
  Enter a food name or 'quit' to exit: Apple
  ```

- Be as specific as possible. For example, "Red apple" might yield different results from "Green apple".

- If the food isn't found, try alternative names or more general terms. For example, if "Granny Smith apple" isn't found, try "Green apple" or just "Apple".

### Understanding the Output

For each food, the model will provide:

1. Potential allergens
2. Estimated nutritional content
3. Dietary categories (vegan, vegetarian, gluten-free)
4. Suggested substitutions (if allergens are present)

### Checking Ingredient Prevalence

After each food analysis, you can check the prevalence of specific ingredients:

- Enter an ingredient name when prompted. For example:
  ```
  Enter an ingredient to check its prevalence (or 'quit' to exit): Sugar
  ```

- Type 'quit' to return to the main food entry prompt.

### Exiting the Program

- Type 'quit' at the main food entry prompt to exit the program.

## What You Can Ask

1. Food Analysis:
   - You can ask about any food in the USDA database. Examples:
     - "Apple"
     - "Chicken breast"
     - "Whole wheat bread"
     - "Greek yogurt"

2. Ingredient Prevalence:
   - After a food analysis, you can ask about the prevalence of any ingredient. Examples:
     - "Sugar"
     - "Salt"
     - "Vitamin C"
     - "Folic acid"

## Tips for Effective Use

- Start with basic, common food names and then get more specific if needed.
- For packaged or processed foods, try including brand names if known.
- When checking ingredient prevalence, use both common and scientific names for best results.
- Remember that the tool's knowledge is based on the USDA database, so very recent food trends or highly specialized products might not be included.

## Limitations

- The tool provides general information and should not be used for medical advice.
- Nutritional estimates are broad categories and not exact measurements.
- The dietary category classification (vegan, vegetarian, gluten-free) is based on ingredient analysis and may not be 100% accurate for all foods.

## Troubleshooting

If you encounter any errors:
1. Ensure all required packages are installed correctly.
2. Check your internet connection, as the tool needs to download USDA data.
3. If issues persist, try restarting the script.

For any unresolved issues or questions, please contact the developer.

