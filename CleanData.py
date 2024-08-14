import pandas as pd

# Step 1: Load the CSV file
file_path = '/Users/Alveena/Desktop/PyGames?/venv/bin/PoetryNumbersCSV.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Step 2: Drop columns that contain only NaN values
data_cleaned = data.dropna(axis=1, how='all')

# Step 3: Extract the poem and emotion data from the index and reset the index
data_cleaned = data_cleaned.reset_index()
data_cleaned.columns = ['Poem', 'Emotion', 'NaN1', 'NaN2']  # Rename columns for clarity

# Step 4: Drop unnecessary NaN columns
data_cleaned = data_cleaned.drop(columns=['NaN1', 'NaN2'])

# Step 5: Remove the first row which is acting as a header
data_cleaned = data_cleaned.iloc[1:].reset_index(drop=True)

# Step 6: Display or save the cleaned data
print(data_cleaned.head())

# Optionally, save the cleaned data to a new CSV file
data_cleaned.to_csv('Cleaned_PoetryNumbers.csv', index=False)
