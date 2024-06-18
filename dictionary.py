import json
import difflib

# Load JSON data into a Python dictionary
def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to return a definition of a word
def get_definition(word, dictionary):
    # Normalize the word to lowercase
    word = word.lower()
    
    # Check if the word exists in the dictionary
    if word in dictionary:
        return dictionary[word]
    else:
        # If the word is not found, suggest close matches
        suggestions = difflib.get_close_matches(word, dictionary.keys())
        if suggestions:
            return f"Did you mean '{suggestions[0]}'? Here is the definition: {dictionary[suggestions[0]]}"
        else:
            return "The word is not found in the dictionary."

# Main function to interact with the user
def main():
    dictionary_file_path = 'dictionary.json'  # Replace with your JSON dictionary file path
    dictionary = load_dictionary(dictionary_file_path)
    
    while True:
        word = input("Enter a word to find its definition (or type 'exit' to quit): ")
        if word.lower() == 'exit':
            break
        definition = get_definition(word, dictionary)
        print(definition)

if __name__ == "__main__":
    main()
