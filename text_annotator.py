# text_annotator.py takes a text block from raw_text.py, the keyword_dictionary already defined,
# and a annotation_path where the annotated .json file will be saved to.

# libraries
import json
import os
from raw_text import raw_text

# Constants
DICT_PATH = "keyword_dictionary.json"
ANNOTATION_PATH = "annotations.json"
NEW_FILE = False;

# --- Functions ---

# Load existing keyword dictionary
def load_keyword_dict():
    if os.path.exists(DICT_PATH):
        with open(DICT_PATH, "r") as f:
            return json.load(f)
    return {}

# Save keyword dictionary
def save_keyword_dict(keyword_dictionary):
    with open(DICT_PATH, "w") as f:
        json.dump(keyword_dictionary, f, indent=4)

# Ask user for category if keyword is new
def get_keyword_category(keyword, keyword_dict):
    keyword = keyword.lower().strip()
    if keyword in keyword_dict:
        print(f"'{keyword}' already categorized as: {keyword_dict[keyword]}")
        return keyword_dict[keyword]
    else:
        category = input(f"What category for '{keyword}'? (e.g., SKILL, TOOL, QUALIFICATION): ").strip().lower()
        keyword_dict[keyword] = category
        save_keyword_dict(keyword_dict)
        return category

# Split text into blocks
def convert_text_to_list(text):
    blocks = text.strip().split('\n\n')
    return [block.strip() for block in blocks if block.strip()]

# --- Main Program ---

# Convert job description text into sections
job_desc_list = convert_text_to_list(raw_text)

# Load the reusable keyword-category dictionary
keyword_dict = load_keyword_dict()
results = []

for text in job_desc_list:
    print("\nText:\n", text)
    keywords = input("Enter keywords for this section, separated by commas: ")
    keywords = [kw.strip().lower() for kw in keywords.split(",") if kw.strip()]

    annotated_keywords = []
    for kw in keywords:
        category = get_keyword_category(kw, keyword_dict)
        annotated_keywords.append({"keyword": kw, "category": category})

    results.append({"text": text, "keywords": annotated_keywords})

# Save annotated data
if NEW_FILE:
    # Create a new .json file for every new text block
    # Saves as json
    with open("job_desc_data/annotations.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nAnnotations saved to: {ANNOTATION_PATH}")
    print(f"Keyword dictionary saved to: {DICT_PATH}")

else:
    # Add to exisiting .json file
    # Load existing annotations if available
    if os.path.exists(ANNOTATION_PATH):
        with open(ANNOTATION_PATH, "r") as f:
            existing_results = json.load(f)
    else:
        existing_results = []

    # Append new results
    combined_results = existing_results + results

    # Save combined results
    with open(ANNOTATION_PATH, "w") as f:
        json.dump(combined_results, f, indent=2)

    print(f"\nAnnotations saved to: {ANNOTATION_PATH}")
    print(f"Keyword dictionary saved to: {DICT_PATH}")