import pandas as pd
from collections import defaultdict
import json

# Load the cleaned CSV file
cleaned_file_path = '/Users/Alveena/Desktop/PyGames?/venv/bin/Cleaned_PoetryNumbers.csv'  # Replace with your actual file path
try:
    data = pd.read_csv(cleaned_file_path)
except FileNotFoundError:
    print(f"File not found at path: {cleaned_file_path}")
    exit()

# Initialize a dictionary to hold the intents
intents_dict = defaultdict(lambda: {"patterns": [], "responses": []})

# Populate the dictionary with tags, patterns, and responses
for index, row in data.iterrows():
    emotion = row['Emotion']
    poem = row['Poem']
    if pd.notna(emotion) and pd.notna(poem):
        # For demonstration, adding a generic pattern based on the emotion
        if not intents_dict[emotion]["patterns"]:
            intents_dict[emotion]["patterns"].append(f"I feel {emotion}")
            intents_dict[emotion]["patterns"].append(f"Why do I feel {emotion}?")
            intents_dict[emotion]["patterns"].append(f"What causes {emotion}?")
        # Add the poem to responses
        intents_dict[emotion]["responses"].append(poem)

# Convert the dictionary to a list of intents
intents_list = [{"tag": emotion, "patterns": details["patterns"], "responses": details["responses"]}
                for emotion, details in intents_dict.items()]

# Wrap the intents list in a dictionary
intents_json = {"intents": intents_list}

# Display the intents (optional)
print(json.dumps(intents_json, indent=4))

# Save the intents to a JSON file
output_file_path = '/Users/Alveena/Desktop/PyGames?/venv/bin/PoetryIntents.json'  # Replace with your desired output path
with open(output_file_path, 'w') as json_file:
    json.dump(intents_json, json_file, indent=4)

print(f"Intents successfully saved to {output_file_path}")

