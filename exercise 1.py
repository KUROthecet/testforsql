import json
from collections import Counter

def def_word_cnt(text):
    # Split the text into words and count them using Counter
    word_counts = dict(Counter(text.split()))
    return word_counts

def save_json_files(input_text):
    word_counts = def_word_cnt(input_text)
    # Create 100 JSON files without using explicit loops
    [
        json.dump(word_counts, open(f"result_{i}.json", "w"))
        for i in range(1, 101)
    ]

# Get input from keyboard
if __name__ == "__main__":
    input_text = input("Enter a string: ")
    save_json_files(input_text)