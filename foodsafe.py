import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np

# Custom dataset
class FoodDataset(Dataset):
    def __init__(self, ingredients, labels):
        self.ingredients = ingredients
        self.labels = labels
    
    def __len__(self):
        return len(self.ingredients)
    
    def __getitem__(self, idx):
        return self.ingredients[idx], self.labels[idx]

# Simple feedforward neural network
class FoodAnalysisModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(FoodAnalysisModel, self).__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        return x

# Training function
def train_model(model, train_loader, criterion, optimizer, num_epochs):
    model.train()
    for epoch in range(num_epochs):
        total_loss = 0
        for ingredients, labels in train_loader:
            outputs = model(ingredients)
            loss = criterion(outputs, labels)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        avg_loss = total_loss / len(train_loader)
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {avg_loss:.4f}')

# Evaluation function
def evaluate_model(model, test_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for ingredients, labels in test_loader:
            outputs = model(ingredients)
            predicted = (outputs > 0.5).float()
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    
    accuracy = correct / total
    print(f'Test Accuracy: {accuracy:.4f}')

# Function to preprocess ingredient input
def preprocess_ingredients(ingredients, ingredient_to_index):
    vector = torch.zeros(len(ingredient_to_index))
    for ingredient in ingredients:
        if ingredient in ingredient_to_index:
            vector[ingredient_to_index[ingredient]] = 1
    return vector

# Interactive mode function
def interactive_mode(model, ingredient_to_index):
    model.eval()
    while True:
        ingredients_input = input("Enter ingredients (comma-separated) or 'quit' to exit: ")
        if ingredients_input.lower() == 'quit':
            break
        
        ingredients = [ing.strip().lower() for ing in ingredients_input.split(',')]
        input_vector = preprocess_ingredients(ingredients, ingredient_to_index)
        
        with torch.no_grad():
            output = model(input_vector.unsqueeze(0))
            probability = torch.sigmoid(output).item()
        
        if probability > 0.5:
            print(f"This food might be linked to health issues (Probability: {probability:.2f})")
        else:
            print(f"This food is likely safe (Probability: {probability:.2f})")

# Main execution
if __name__ == "__main__":
    # Simulated data (replace with your actual data)
    num_samples = 1000
    num_ingredients = 100
    
    # Create a mapping of ingredient names to indices
    ingredients_list = [f"ingredient_{i}" for i in range(num_ingredients)]
    ingredient_to_index = {ing: i for i, ing in enumerate(ingredients_list)}
    
    # Generate random ingredient combinations
    ingredients_data = torch.randint(0, 2, (num_samples, num_ingredients)).float()
    
    # Generate random labels (0: safe, 1: unsafe)
    labels_data = torch.randint(0, 2, (num_samples, 1)).float()
    
    # Split data into train and test sets
    train_size = int(0.8 * num_samples)
    train_ingredients, test_ingredients = ingredients_data[:train_size], ingredients_data[train_size:]
    train_labels, test_labels = labels_data[:train_size], labels_data[train_size:]
    
    # Create datasets and dataloaders
    train_dataset = FoodDataset(train_ingredients, train_labels)
    test_dataset = FoodDataset(test_ingredients, test_labels)
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
    
    # Initialize model, loss, and optimizer
    input_size = num_ingredients
    hidden_size = 50
    output_size = 1
    model = FoodAnalysisModel(input_size, hidden_size, output_size)
    criterion = nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    # Train the model
    train_model(model, train_loader, criterion, optimizer, num_epochs=10)
    
    # Evaluate the model
    evaluate_model(model, test_loader)
    
    # Start interactive mode
    print("\nEntering interactive mode...")
    interactive_mode(model, ingredient_to_index)

