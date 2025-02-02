Overview

This project extracts entities and their relationships from text data using Google Gemini AI, visualizes the relationships as a graph, and generates a summary. The tool processes an Excel dataset, applies AI-based entity extraction, and presents insights for security and analytical purposes.

Features

Loads text data from an Excel file.

Uses Google Gemini AI for entity and relationship extraction.

Creates a graph visualization of the extracted relationships.

Generates a final summary highlighting key relationships, extreme values, and repeated patterns.

Saves results to an Excel file.

Dependencies

Ensure you have the following Python libraries installed:

pip install google-generativeai pandas python-dotenv networkx matplotlib tkinter openpyxl

Libraries Used

google.generativeai: For AI-based entity extraction.

os: For environment variable handling.

pandas: For data processing.

dotenv: For loading API keys.

networkx: For graph-based relationship visualization.

matplotlib.pyplot: For drawing graphs.

json: For handling structured AI responses.

tkinter: For file selection dialog.

re: For text processing.

Setup

Set up your API key:

Create a .env file in the project directory.

Add your Google Gemini API key:

GEMINI_API_KEY=your_api_key_here

Run the script:

python your_script.py

Select an Excel file containing text data.

The script will process the text and extract entity relationships.

A graph will be displayed showing relationships between entities.

The extracted results will be saved in results.xlsx.

A summary report will be generated and printed in the console.

Output Files

results.xlsx: Contains extracted entities and relationships.

Graph Visualization: Displays extracted relationships visually.

Usage & Applications

This tool can be used for:

Security Analysis: Detecting unusual relationships in datasets.

Research & Intelligence: Extracting structured insights from large text corpora.

Data Science & Visualization: Understanding entity interactions in various domains.

Troubleshooting

Ensure the .env file is correctly set up with the API key.

Verify that the Excel file is properly formatted with a "Text" column.

If visualization errors occur, check networkx and matplotlib installation.

License

This project is open-source and can be modified as needed.

