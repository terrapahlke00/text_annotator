# Text Annotator with Keyword Categorization
This tool allows for the efficient annotation and categorization of text. Given a chunk of text, the program automatically parses it into sentences and prompts the user to input keywords for each sentence. Once a keyword is identified, the user is then asked to assign it to a predefined category or create a new category.

## Key features include:
- **Text Segmentation**: The input text is split into individual sentences for granular annotation.

- **Interactive Keyword Annotation**: For each sentence, the user is prompted to identify the keywords and categorize them. This step ensures precise and context-specific tagging.

- **Automatic Keyword Categorization**: If a keyword is already present in the keyword bank, the system automatically categorizes it, eliminating the need for manual input and speeding up the annotation process.

- **Exportable Annotations**: After all sentences are processed and keywords categorized, the tool generates a .json file containing the annotated text. This file can be used as a dataset for machine learning models, enabling more efficient training and analysis.

- **Keyword Bank**: The system maintains a bank of pre-defined keywords, which helps automate the categorization for recurring terms, ensuring consistency and reducing annotation time.

This tool is designed for anyone looking to build structured datasets for natural language processing (NLP) models or simply categorize textual data more efficiently.
