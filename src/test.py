import json

# Path to the JSON file
file_path = './src/data/data.json'

# Read and load the JSON data
with open(file_path, 'r', encoding='utf-8') as file:
    word_fa = json.load(file)

# Print to verify the content
# print(word_fa)

print(len(word_fa['word']))