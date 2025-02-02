import google.generativeai as genai
import os
import pandas as pd
from dotenv import load_dotenv

import networkx as nx
import matplotlib.pyplot as plt
import json
load_dotenv()
import tkinter as tk
from tkinter import filedialog
import re
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError(" API key not found. Make sure the .env file is set correctly.")


genai.configure(api_key=GEMINI_API_KEY)


with open("system_prompt.txt", mode="r") as f:
    system_prompt = f.read()

#system prompt.txt is supposed to train the model

model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=system_prompt)

root = tk.Tk()
root.withdraw()  
file_path = filedialog.askopenfilename(title="Select Excel Dataset", filetypes=[("Excel files", "*.xlsx;*.xls")])

df = pd.read_excel(file_path)










def extract_entities_and_relationships(text):
    """Extracts relationships using Gemini AI with error handling."""
    if pd.isna(text) or text.strip() == "":
        return None  
    
    try:
        response = model.generate_content(text)
        
        if hasattr(response, "text") and isinstance(response.text, str):
            return response.text  
        else:
            return " Error: No valid response text"
    except Exception as e:
        return -1 


def visualization():
    G =nx.Graph()
    for _, row in df.iterrows():
        entities = row["Entities"]
        relationships = row["Relationships"]
        print(relationships)
        if isinstance(entities, str) and isinstance(relationships, str):
            
            
           

            for relation in relationships:
                if isinstance(relation, list) and len(relation) == 2:
                    entity1, entity2 = relation
                    G.add_node(entity1)
                    G.add_node(entity2)
                    G.add_edge(entity1, entity2, label="relationship")  
                
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color="skyblue", edge_color="gray", font_size=10, node_size=3000)

    plt.title("Entity Relationship Graph", fontsize=14)
    plt.show()


dataset = []
chatSession = model.start_chat()


for i, text in enumerate(df["Text"]):
    extracted_data = extract_entities_and_relationships(text)
    while extracted_data == -1:
        
        extracted_data = extract_entities_and_relationships(text)
        
    if extracted_data is None or not isinstance(extracted_data, str):
        dataset.append(("No Entities Found", "No Relationships Found"))
        continue  # Skip to next row
    parts = extracted_data.split("{\"Relationships\":", maxsplit=1)

    entities_part = parts[0].strip()  
    relationships_part = "{Relationships:" + parts[1].strip()  + "}" if len(parts)>1 else None
    dataset.append((entities_part, relationships_part))  




df["Entities"] = [item[0] for item in dataset]
df["Relationships"] = [item[1] for item in dataset]
print(df["Relationships"])


missing_values = df.isnull().sum()
print('Null values found ', missing_values)

df.dropna(subset = ["Entities", "Relationships"])

df = df.drop_duplicates()

visualization()



df.to_excel("resultS.xlsx", index=False)

print(" Processing complete. Results saved to 'modified_wikileaks_parsed.xlsx'.")
final =model.generate_content("From the following excerpts, summarize the entities and relationships that appear throughout the input. Point out Extreme values or unusual relationships detected in the dataset. Also point out a conclusion that includes repeated patterns and strong relationships between the entities, finishing with reasons why this tool is useful for security. Each excerpt is seperated by five hashtags (#####) and are unrelated to other excerpts given.\n" + "#####\n".join(df["Text"]))
print(final)
