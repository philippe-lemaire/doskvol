import random
from .rollmechanics import fortuneRoll


MOODS = [
    "Dark or Cold",
    "Bright or Lively",
    "Quiet or Refined",
    "Abandoned or Decrepit",
    "Cramped or Noisy",
    "Cozy or Warm",
]

IMPRESSIONS = {
    "Sights": [
        "Rain Slick, Oil Slick",
        "Dancing Shadows, Flickering Lights",
        "Mist, Fog, Frost",
        "Fleeting Shapes, Echoes in the Ghost Field",
        "Soot, Ash Clouds, Grime",
        "Crackling Electricity, Wires, Mechanisms",
    ],
    "Sounds": [
        "Machinery, Workers",
        "Fluttering Cloth, Howling Wind",
        "Laughter, Song, Music",
        "Whispers, Echoes, Strange Voices",
        "Thunder, Driving Rain",
        "Bells, Clock Chimes, Harbor Horns",
    ],
    "Smells": [
        "Cook Fires, Furnaces",
        "Damp Wood, Decay, Refuse",
        "Animals, Hides, Blood",
        "Chemicals, Distillates, Fumes",
        "Rain Water, Ocean",
        "Ozone, Electroplasmic Discharges",
    ],
}

USE = {
    3: ["Residential", "Crafts", "Labor", "Shops", "Trade", "Hospitality"],
    5: [
        "Law, Government",
        "Public Space",
        "Power",
        "Manufacture",
        "Transportation",
        "Leisure",
    ],
    6: ["Vice", "Entertainment", "Storage", "Cultivation", "Academic", "Artists"],
}

TYPE = {
    3: [
        "Narrow Lane",
        "Tight Alley",
        "Twisting Street",
        "Rough Road",
        "Bridge",
        "Waterway",
    ],
    5: [
        "Closed Court",
        "Open Plaza",
        "Paved Avenue",
        "Tunnel",
        "Wide Boulevard",
        "Roundabout",
    ],
    6: [
        "Elevated",
        "Flooded",
        "Suspended",
        "Subterranean",
        "Floating",
        "Private, Gated",
    ],
}

DETAILS = {
    1: [
        "Metal Supports",
        "Ironwork Gates, Fences",
        "Belching Chimneys",
        "Metal Grates, Hatches, Doors",
        "Clockwork Mechanisms",
        "Rigging, Cables",
    ],
    2: [
        "Stairs, Ramps, Terraces",
        "Wooden Scaffolds",
        "Skyways",
        "Rooftop Spaces",
        "Rails, Train Cars",
        "Hidden Passages",
    ],
    3: [
        "Banners, Pennants",
        "Festival Decorations",
        "Crowd, Parade, Riot",
        "Street Performers",
        "Makeshift Stalls, Shelters",
        "Crisscrossing Routes",
    ],
    4: [
        "Gang Markings",
        "Patrol Posts",
        "Lookouts",
        "Stocks, Public Punishment",
        "Street Crier, Visionary",
        "News Stand, Public Notices",
    ],
    5: [
        "Stray Animals",
        "Landscaping",
        "Muck, Mire",
        "Construction, Demolition",
        "Foul Runoff, Fumes, Smoke",
        "Orphans, Beggars",
    ],
    6: [
        "Ancient Ruin",
        "Leering Gargoyles",
        "Sprit Chimes, Wards",
        "Eerie Emptiness",
        "Quarantine, Lockdown",
        "Shrine Offerings",
    ],
}


class Street:
    def __init__(self):
        self.mood = random.choice(MOODS)
        self.impressions = {
            sense: random.choice(IMPRESSIONS[sense])
            for sense in ["Sights", "Sounds", "Smells"]
        }
        self.use = random.choice(USE.get(fortuneRoll()))
        self.type = random.choice(TYPE.get(fortuneRoll()))
        self.detail = random.choice(DETAILS[random.randint(1, 6)])

    def __str__(self):
        return f"""A {self.mood} street.
        The impressions it gives are : {self.impressions}.
        Its use is {self.use}.
        Its type is {self.type}.
        A detail: {self.detail}.
        """
