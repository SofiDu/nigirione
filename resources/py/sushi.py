import json

#PRICES

NORMALBOX = "7.50€"



# Define menu items

menu_items = [
    {"title": "A1 Sashimi Salmão", "price": NORMALBOX, "image": "resources/img/sushi/a1.png"},
    {"title": "A2 Sashimi Misto", "price": NORMALBOX, "image": "resources/img/sushi/a2.png"},
    {"title": "A3 Maki+Califórnia", "price": NORMALBOX, "image": "resources/img/sushi/a3.png"},
    {"title": "A4 Sushi Salmão/Ovo/Queijo", "price": NORMALBOX, "image": "resources/img/sushi/a4.png"},
    {"title": "A5 Nigiri Salmão", "price": NORMALBOX, "image": "resources/img/sushi/a5.png"}
]

file_path = "resources/js/menuTakeAway.json"

# Write menu items to JSON file
with open(file_path, 'w') as f:
    json.dump(menu_items, f, indent=2)