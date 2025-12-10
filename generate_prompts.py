
import json
import random

# Load existing prompts
file_path = '/Users/samseen/DEV/Prromts/prompts.json'
try:
    with open(file_path, 'r') as f:
        data = json.load(f)
        last_id = int(data[-1]['id'])
except (FileNotFoundError, json.JSONDecodeError, IndexError):
    data = []
    last_id = 0

new_prompts = []

# Components based on the guide
subjects = [
    "a stoic robot barista with glowing blue optics", "a fluffy calico cat wearing a tiny wizard hat",
    "a cyberpunk street vendor selling neon noodles", "an astronaut playing chess with an alien",
    "a transparent glass sculpture of a lion", "a miniature city inside a lightbulb",
    "a vintage typewriter coming to life", "a dragon made of swirling smoke",
    "a futuristic racer on a hoverbike", "a detective examining a glowing clue",
    "a steampunk owl with brass gears", "a mystical tree with crystal leaves",
    "a chef preparing a dish of floating ingredients", "a musician playing an instrument made of light",
    "a samurai standing in a field of red spider lilies", "a diver discovering a sunken technological city",
    "a polar bear wearing steampunk goggles", "a family of robots having a picnic",
    "a wizard reading a holographic grimoire", "a bioluminescent jellyfish floating in air"
]

compositions = [
    "extreme close-up", "wide shot", "low angle shot", "portrait",
    "bird's eye view", "dutch angle", "over-the-shoulder shot", "macro photography",
    "fisheye lens", "panoramic view", "isometric view", "silhouette shot"
]

actions = [
    "brewing a cup of coffee", "casting a magical spell", "mid-stride running through a field",
    "reading an ancient scroll", "creating a holographic map", "meditating in mid-air",
    "painting a portal to another world", "fixing a complex machine", "dancing in the rain",
    "looking at a galaxy map", "serving customers", "planting a glowing seed",
    "playing a violin", "climbing a digital mountain", "watching a binary sunset"
]

locations = [
    "a futuristic cafe on Mars", "a cluttered alchemist's library", "a sun-drenched meadow at golden hour",
    "a neon-lit cyberpunk alleyway", "an underwater obsidian palace", "a floating island in the clouds",
    "a cozy cottage in a snowy forest", "a high-tech laboratory", "a bustling intergalactic market",
    "a serene zen garden in space", "a post-apocalyptic overgrown city", "a crystal cave",
    "the surface of a glitched computer screen", "a victorian greenhouse", "a desert with purple sand"
]

styles = [
    "3D animation", "film noir", "watercolor painting", "photorealistic", "1990s product photography",
    "cyberpunk aesthetic", "steampunk style", "studio Ghibli style", "oil painting",
    "pixel art", "vaporwave", "cinematic concept art", "blueprint schematic", "claymation",
    "retro comic book style", "ukiyo-e woodblock print", "low poly 3d", "vector art"
]

camera_details = [
    "shallow depth of field (f/1.8)", "Golden hour backlighting creating long shadows",
    "Cinematic color grading with muted teal tones", "dramatic chiaroscuro lighting",
    "volumetric fog and god rays", "studio lighting with softbox", "high contrast black and white",
    "lens flare and chromatic aberration", "soft pastel color palette", "neon rim lighting"
]

text_integrations = [
    "The headline 'URBAN EXPLORER' rendered in bold, white, sans-serif font at the top",
    "A neon sign reading 'OPEN 24/7' glowing in the background",
    "The word 'MAGIC' written in sparkling dust",
    "A book title 'THE FUTURE' clearly visible on the spine",
    "A poster on the wall with the text 'TRAVEL TO MARS'",
    "Label 'FIG 1.1' next to the diagram",
    "A speech bubble saying 'Hello World'",
    "Graffiti on the wall spelling out 'HOPE'",
    "A digital HUD displaying 'SYSTEM READY'",
    "The brand name 'NANO' embossed on the product"
]

# Generate 300 prompts
for i in range(300):
    category_choice = random.choice(['General', 'Text Rendering', 'Diagram', 'Portrait', 'Landscape', 'Product'])
    
    prompt_text = ""
    title_text = ""
    
    # Randomly structure the prompt based on tips
    structure_type = random.choice([1, 2, 3, 4])
    
    if structure_type == 1: # Standard Subject/Action/Loc/Style
        s = random.choice(subjects)
        a = random.choice(actions)
        l = random.choice(locations)
        st = random.choice(styles)
        prompt_text = f"{st} of {s} {a} in {l}."
        title_text = f"{st.split()[0].title()} {s.split()[0].title()} {s.split()[-1].title()}"

    elif structure_type == 2: # Detailed Camera/Composition
        c = random.choice(compositions)
        s = random.choice(subjects)
        cam = random.choice(camera_details)
        prompt_text = f"{c} of {s}. {cam}."
        title_text = f"{c.title()} {s.split()[-1].title()}"

    elif structure_type == 3: # Text Integration
        s = random.choice(subjects)
        l = random.choice(locations)
        t = random.choice(text_integrations)
        prompt_text = f"A photorealistic image of {s} in {l}. {t}."
        title_text = f"Text Integration: {s.split()[-1].title()}"

    elif structure_type == 4: # Complex Mix
        s = random.choice(subjects)
        a = random.choice(actions)
        l = random.choice(locations)
        cam = random.choice(camera_details)
        prompt_text = f"{s} {a} in {l}. Shot with {cam}."
        title_text = f"Cinematic {s.split()[0].title()} {s.split()[-1].title()}"

    # Add variations and randomness
    if random.random() > 0.7:
        prompt_text += f" {random.choice(camera_details)}"

    last_id += 1
    new_entry = {
        "id": str(last_id),
        "title": title_text[:50], # Keep title reasonable
        "category": category_choice,
        "prompt": prompt_text,
        "tags": ["gemininanobanana", "generated", category_choice.lower(), random.choice(styles).split()[0].lower()]
    }
    new_prompts.append(new_entry)

# Append and save
data.extend(new_prompts)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print(f"Successfully added {len(new_prompts)} prompts. Total now: {len(data)}")
