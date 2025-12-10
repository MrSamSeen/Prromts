
import json
import random

# Load existing prompts to get ID sequence
file_path = '/Users/samseen/DEV/Prromts/prompts.json'
try:
    with open(file_path, 'r') as f:
        data = json.load(f)
        last_id = int(data[-1]['id'])
except (FileNotFoundError, json.JSONDecodeError, IndexError):
    data = []
    last_id = 0

new_prompts = []

# ------------------------------------------------------------------
# 1. Professional Photography (20 prompts)
# ------------------------------------------------------------------
photography_subjects = [
    ("an elderly watchmaker fixing a clock", "macro shot, 100mm lens"),
    ("a ballerina tying her shoes", "low angle, shallow depth of field f/2.8"),
    ("a street musician in the rain", "cinematic lighting, 50mm lens, high contrast"),
    ("a lion roaring at sunset", "telephoto 400mm, golden hour backlighting"),
    ("a futuristic cityscape at night", "wide angle 24mm, long exposure, light trails"),
    ("a chef plating a gourmet dish", "overhead shot, softbox lighting, high key"),
    ("a surfer catching a wave", "fast shutter speed, action shot, GoPro style"),
    ("a model with avant-garde makeup", "studio portrait, rembrandt lighting, sharp focus"),
    ("a dew drop on a spider web", "extreme macro, bokeh background"),
    ("a vintage car rally", "panning shot, motion blur backdrop"),
    ("a woman looking out a rainy window", "moody lighting, focus on reflections"),
    ("a climber dangling from a cliff", "drone shot, dramatic perspective"),
    ("a jazz saxophonist in a smoky club", "spotlight, noir style, monochrome"),
    ("a field of lavender", "landscape photography, f/16 for deep focus"),
    ("a fox in the snow", "telephoto, sharp eyes, soft white background"),
    ("a busy tokyo crossing", "tilt-shift effect, miniature look"),
    ("a campfire on a beach under the milky way", "long exposure, star photography"),
    ("a diver swimming with whales", "underwater photography, sun rays penetrating water"),
    ("a bride adjusting her veil", "soft window light, ethereal mood"),
    ("a skateboarder mid-air", "fisheye lens, dynamic angle, urban background")
]

for subject, style in photography_subjects:
    last_id += 1
    new_prompts.append({
        "id": str(last_id),
        "title": f"Photo: {subject.split()[:3]}...",
        "category": "Photography",
        "prompt": f"Professional photography of {subject}. Settings: {style}. Highly detailed, 8k resolution.",
        "tags": ["gemininanobanana", "photography", "realistic", "professional"]
    })

# ------------------------------------------------------------------
# 2. Typography & Text Integration (20 prompts)
# ------------------------------------------------------------------
typography_ideas = [
    ("a neon sign in a rainy alley", "OPEN LATE"),
    ("a vintage travel poster for Mars", "VISIT MARS"),
    ("a coffee bag on a wooden table", "FRESH BREW"),
    ("a futuristic movie poster", "THE LAST SYNTH"),
    ("a graffiti wall in a subway", "REBEL ART"),
    ("a minimalist book cover", "SILENCE"),
    ("a cereal box on a breakfast table", "CRUNCHY LOOPS"),
    ("a handwritten letter with a quill", "Dearest Friend"),
    ("a street sign in a blizzard", "NOWHERE"),
    ("a t-shirt design on a model", "CODE LIFE"),
    ("a monumental stone engraving", "ETERNITY"),
    ("a chalkboard menu in a cafe", "Daily Specials"),
    ("a retro arcade game screen", "INSERT COIN"),
    ("a holographic hud interface", "ACCESS DENIED"),
    ("a wedding invitation card with flowers", "Save the Date"),
    ("a license plate on a muscle car", "FAST 88"),
    ("a billboard in Times Square", "BUY NOW"),
    ("a greeting card with a cute bear", "Happy Birthday"),
    ("a newspaper headline on a park bench", "ALIENS LAND"),
    ("a tattoo on an arm", "STRENGTH")
]

for context, text in typography_ideas:
    last_id += 1
    new_prompts.append({
        "id": str(last_id),
        "title": f"Text: {text}",
        "category": "Typography",
        "prompt": f"A high-quality image of {context}. The text '{text}' is clearly visible, correctly spelled, and rendered in a style matching the environment.",
        "tags": ["gemininanobanana", "typography", "text-rendering", "design"]
    })

# ------------------------------------------------------------------
# 3. Creative & Surreal Concepts (20 prompts)
# ------------------------------------------------------------------
surreal_concepts = [
    "A cloud shaped like a sleeping cat floating over a city.",
    "A house made entirely of translucent gummy candy.",
    "A giraffe wearing a monocle and a suit reading a newspaper.",
    "A tree where the leaves are glowing lightbulbs.",
    "An ocean made of liquid gold with diamond waves.",
    "A snail with a disco ball as a shell.",
    "A stairway leading up into a galaxy portal.",
    "A chess game played by two nebulas in space.",
    "A human silhouette filled with a thunderstorm.",
    "A library where books are flying like birds.",
    "A city built on the back of a giant turtle.",
    "A teapot pouring a waterfall into a canyon cup.",
    "A lion made of fire fighting a tiger made of ice.",
    "A bicycle with oranges for wheels.",
    "A vintage TV showing the viewer's reflection in the future.",
    "A forest of giant mushrooms with windows and doors.",
    "A fish swimming in the air through a city street.",
    "A melting pocket watch on a desert branch (Dali style).",
    "A robot painting a self-portrait on a canvas.",
    "An astronaut meditating on a floating lotus in space."
]

for concept in surreal_concepts:
    last_id += 1
    new_prompts.append({
        "id": str(last_id),
        "title": "Surreal Concept",
        "category": "Surrealism",
        "prompt": f"Create a surreal and imaginative image: {concept} Vibrant colors, dreamlike atmosphere, high detail.",
        "tags": ["gemininanobanana", "surreal", "creative", "art"]
    })

# ------------------------------------------------------------------
# 4. Product Mockups & Branding (20 prompts)
# ------------------------------------------------------------------
product_scenarios = [
    ("a sleek matte black smartphone", "hovering in a void"),
    ("a luxury perfume bottle", "on a reflective surface with rose petals"),
    ("a craft beer can", "on a rustic wooden bar counter"),
    ("a branded sneaker", "floating with dynamic particles"),
    ("a minimalist furniture set", "in a sunlit modern living room"),
    ("a package of gourmet chocolate", "studio lighting, dark background"),
    ("a tube of organic lipstick", "smear texture background"),
    ("a smart watch", "on a wrist jogging in the park"),
    ("a glass of whiskey", "ice cubes, warm ambient bar lighting"),
    ("a bag of premium coffee beans", "spilled beans texture"),
    ("a set of wireless headphones", "neon lighting, cyber background"),
    ("a ceramic vase", "minimalist nordic style interior"),
    ("a soda can with condensation", "fresh, ice cold vibe"),
    ("a leather wallet", "beside a vintage camera"),
    ("a tube of paint", "squeezed out, colorful mess"),
    ("a drone", "flying over a mountain landscape"),
    ("a gaming mouse", "RGB lighting, dark desk setup"),
    ("a bamboo toothbrush", "bathroom counter, eco green vibe"),
    ("a hardcover book", "on a nightstand with a lamp"),
    ("a diamond ring", "macro shot, sparkle effect")
]

for product, setting in product_scenarios:
    last_id += 1
    new_prompts.append({
        "id": str(last_id),
        "title": f"Product: {product.split()[-1].title()}",
        "category": "Product",
        "prompt": f"Commercial product photography of {product}, placed {setting}. Studio quality lighting, 4k resolution, advertising style.",
        "tags": ["gemininanobanana", "product", "commercial", "mockup"]
    })

# ------------------------------------------------------------------
# 5. Diagrams & Infographics (20 prompts)
# ------------------------------------------------------------------
diagram_topics = [
    ("an exploded view of a mechanical watch", "technical drawing style"),
    ("a cross-section of a volcano", "educational infographic style"),
    ("a map of a fictional fantasy kingdom", "parchment texture, intricate details"),
    ("a diverse food pyramid", "colorful vector illustration"),
    ("the life cycle of a butterfly", "scientific illustration"),
    ("anatomy of a human heart", "medical diagram style"),
    ("floor plan of a modern apartment", "blueprint style, white on blue"),
    ("solar system orbits", "dark background, glowing lines"),
    ("parts of a flower", "botanical illustration"),
    ("a timeline of human evolution", "horizontal infographic"),
    ("how a car engine works", "3D cutaway render"),
    ("types of coffee drinks", "chalkboard style illustration"),
    ("layers of the earth's atmosphere", "flat design style"),
    ("a subway map of a megacity", "clean lines, color coded"),
    ("muscles of the human back", "realistic shading"),
    ("water cycle diagram", "arrows and labels, friendly style"),
    ("guitar chord chart", "clean graphic design"),
    ("periodic table of elements", "modern grid layout"),
    ("constellation map of the northern hemisphere", "star chart style"),
    ("recipe steps for baking bread", "icon based infographic")
]

for topic, style in diagram_topics:
    last_id += 1
    new_prompts.append({
        "id": str(last_id),
        "title": f"Diagram: {topic.split()[:2]}",
        "category": "Educational",
        "prompt": f"Create an accurate {style} of {topic}. Clear labels, high fidelity, educational purpose.",
        "tags": ["gemininanobanana", "diagram", "infographic", "educational"]
    })

# Append and save
data.extend(new_prompts)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print(f"Successfully added {len(new_prompts)} high-quality prompts. Total now: {len(data)}")
