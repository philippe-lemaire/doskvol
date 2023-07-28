import random

MOODS = [
    "Dark or Cold",
    "Bright or Lively",
    "Quiet or Refined",
    "Abandoned or Decrepit",
    "Cramped or Noisy",
    "Cozy or Warm",
]


class Street:
    def __init__(self):
        self.mood = random.choice(MOODS)

    def __str__(self):
        return f"A {self.mood} street."
