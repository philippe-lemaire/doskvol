import random


def fortuneRoll(dice=1):
    """Rolls a fortune roll and returns 3, 5, 6 or Critical (2 dice minimum for critical)"""
    keeplowest = False
    if dice == 0:  # special case, roll 2 keep lowest
        dice = 2
        keeplowest = True

    rolls = [random.randint(1, 6) for d in range(dice)]
    print(rolls)
    if keeplowest:
        rolls.remove(max(rolls))

    if rolls.count(6) >= 2:
        return "Critical"

    roll = max(rolls)
    if roll <= 3:
        return 3
    if roll <= 5:
        return 5
    return 6


if __name__ == "__main__":
    for k in range(10):
        print(f"Rolling with {k} dice. Got a {fortuneRoll(k)}.")
