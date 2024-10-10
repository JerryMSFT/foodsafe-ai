# Food Ingredient Analysis Model

## Introduction

This tool uses a machine learning model to analyze food ingredients and provide insights about potential dietary considerations. It's designed to help users make informed decisions about their food choices based on ingredient composition.

## What This Model Can Do

- Identify potential allergens in foods based on ingredient lists
- Estimate basic nutritional content (e.g., if a food is likely high in sugar, fat, or protein)
- Classify foods into dietary categories (e.g., vegan, vegetarian, gluten-free)
- Suggest possible ingredient substitutions for common dietary restrictions
- Provide general information about the prevalence of certain ingredients in processed foods

## What This Model Cannot Do

- Diagnose medical conditions or allergies
- Predict specific health outcomes like weight gain, fatigue, or disease risk
- Provide personalized dietary advice
- Replace the advice of a medical professional or registered dietitian
- Guarantee the safety or healthfulness of any food product

## How to Use the Model

1. Run the interactive mode of the program.
2. When prompted, enter a list of ingredients separated by commas.
3. The model will analyze the ingredients and provide its insights.

## Example Prompts

Good examples of what to ask:

- "What are the main ingredients in ketchup, and are any common allergens present?"
- "Is this ingredient list (flour, sugar, butter, eggs) suitable for a vegan diet?"
- "Based on these ingredients, is this product likely to be high in added sugars?"
- "What are some gluten-free alternatives to these ingredients: wheat flour, barley malt?"
- "How common is high fructose corn syrup in this type of product?"

Avoid asking:

- "Will eating hot dogs and ketchup make me fat?"
- "Can these ingredients cause cancer?"
- "Is this food healthy for me?"
- "How many calories are in this food?"
- "Will this food give me energy or make me tired?"

## Interpreting Results

- The model provides probabilities or likelihoods, not definitive answers.
- Results should be considered as general guidance, not medical or nutritional advice.
- Always verify information with reliable sources, especially for health-critical decisions.

## Limitations and Disclaimers

- This model is based on general patterns in food ingredients and may not account for all possible variations or special cases.
- It does not have access to complete nutritional information or serving sizes.
- The model's knowledge is based on its training data and may not reflect the most current nutritional research or food industry practices.
- Always read product labels and consult with healthcare professionals for personalized dietary advice.

## Using with PyTorch

This project uses PyTorch for building and training the machine learning model. Here's how to set up and use the model:

1. Install PyTorch:
   ```
   pip install torch torchvision torchaudio
   ```

2. Clone the repository:
   ```
   git clone https://github.com/yourusername/foodsafe-ai.git
   cd foodsafe-ai
   ```

3. Install other dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the training script:
   ```
   python train_model.py
   ```

5. Start the interactive mode:
   ```
   python interactive_mode.py
   ```

6. When prompted, enter food ingredients separated by commas.

Note: Make sure you have a CUDA-compatible GPU for faster training, although the model can run on CPU as well.

## Customizing the Model

You can customize the model architecture in `model.py`. Adjust hyperparameters like learning rate, batch size, and number of epochs in `train_model.py`.

To use your own dataset:
1. Prepare your data in a CSV format with columns for ingredients and labels.
2. Modify the `load_data()` function in `data_loader.py` to load your dataset.
3. Adjust the `preprocess_ingredients()` function in `utils.py` if your data requires different preprocessing.

## Further Information

For more detailed nutritional information, please consult:
- USDA FoodData Central: https://fdc.nal.gov/
- FDA Food Labeling and Nutrition: https://www.fda.gov/food/food-labeling-nutrition

Remember, this tool is meant to provide general insights and should not replace professional medical or nutritional advice.

