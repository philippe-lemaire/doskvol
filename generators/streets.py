import random

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


class Street:
    def __init__(self):
        self.mood = random.choice(MOODS)
        self.impressions = {
            sense: random.choice(IMPRESSIONS[sense])
            for sense in ["Sights", "Sounds", "Smells"]
        }

    def __str__(self):
        return f"""A {self.mood} street.
        The impressions it gives are : {self.impressions}"""
