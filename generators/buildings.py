import random

EXTERIORS = {
    "material": [
        "Gray Brick",
        "Stone & Timbers",
        "Cut Stone and Blocks",
        "Wooden Boards",
        "Plaster Board & Timbers",
        "Metal Sheeting",
    ],
    "details": [
        "Tile Work",
        "Iron Work",
        "Glass Work",
        "Stone Work",
        "Wood Work",
        "Landscaping",
    ],
}
USE_COMMON = ["Bunk House"]
USE_RARE = ["Market House"]  # let's put the 36 options flat here
DETAILS = ["Dripping Water", "Creaking Floorboards"]


class Building:
    def __init__(self, rarity):
        self.rarity = rarity
        self.exterior = {
            "material": random.choice(EXTERIORS["material"]),
            "details": random.choice(EXTERIORS["details"]),
        }
        if self.rarity == "common":
            self.use = random.choice(USE_COMMON)
        if self.rarity == "rare":
            self.use = random.choice(USE_RARE)
        self.details = random.choice(DETAILS)

    def __str__(self):
        return f"""A Building with {self.rarity} and {self.details}"""
