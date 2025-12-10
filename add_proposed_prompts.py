
import json
import re

# File paths
markdown_path = '/Users/samseen/DEV/Prromts/proposed_prompts.md'
json_path = '/Users/samseen/DEV/Prromts/prompts.json'

# Category mapping based on headers
category_map = {
    "Text Rendering Mastery": "Typography",
    "Camera & Cinematic Control": "Photography",
    "Logic, Diagrams & Infographics": "Educational",
    "Creative & Surreal Concepts": "Surrealism",
    "Brand, Product & Style Consistency": "Product"
}

# Load existing JSON
try:
    with open(json_path, 'r') as f:
        data = json.load(f)
        if data:
            last_id = int(data[-1]['id'])
        else:
            last_id = 0
except (FileNotFoundError, json.JSONDecodeError):
    data = []
    last_id = 0

# Read Markdown
with open(markdown_path, 'r') as f:
    md_content = f.read()

# Helper to process sections
current_category = "General"
new_prompts = []

# Regex to find sections and items
# Splitting by lines
lines = md_content.split('\n')

for line in lines:
    line = line.strip()
    
    # Detect Header
    if line.startswith('## '):
        header_text = line.replace('## ', '').split('(')[0].strip()
        current_category = category_map.get(header_text, "General")
        continue
    
    # Detect List Item
    # Format: 1. **Title**: "Prompt"
    match = re.match(r'^\d+\.\s+\*\*(.*?)\*\*:\s+"(.*?)"', line)
    if match:
        title = match.group(1)
        prompt_text = match.group(2)
        
        last_id += 1
        
        # Determine tags based on category
        tags = ["gemininanobanana", current_category.lower()]
        if current_category == "Typography":
            tags.extend(["text", "design"])
        elif current_category == "Photography":
            tags.extend(["photo", "realistic"])
        elif current_category == "Educational":
            tags.extend(["diagram", "infographic"])
        elif current_category == "Surrealism":
            tags.extend(["art", "creative"])
        elif current_category == "Product":
            tags.extend(["commercial", "mockup"])
            
        new_entry = {
            "id": str(last_id),
            "title": title,
            "category": current_category,
            "prompt": prompt_text,
            "tags": tags
        }
        new_prompts.append(new_entry)

# Append and Save
data.extend(new_prompts)

with open(json_path, 'w') as f:
    json.dump(data, f, indent=4)

print(f"Successfully processed markdown and added {len(new_prompts)} prompts. Total now: {len(data)}")
