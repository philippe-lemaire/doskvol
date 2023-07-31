import random
from .rollmechanics import fortuneRoll


def roll_gender():
    r = 6
    while r == 6:
        r = random.randint(1, 6)
        if r <= 2:
            return "Man"
        if r <= 4:
            return "Woman"
        if r == 5:
            return "Ambiguous, Concealed"


TRAITS = (
    "Charming",
    "Cold",
    "Cavalier",
    "Brash",
    "Suspicious",
    "Obsessive",
    "Shrewd",
    "Quiet",
    "Moody",
    "Fierce",
    "Careless",
    "Secretive",
    "Ruthless",
    "Calculating",
    "Defiant",
    "Gracious",
    "Insightful",
    "Dishonest",
    "Patient",
    "Vicious",
    "Sophisticated",
    "Paranoid",
    "Enthusiastic",
    "Elitist",
    "Savage",
    "Cooperative",
    "Arrogant",
    "Confident",
    "Vain",
    "Daring",
    "Volatile",
    "Candid",
    "Subtle",
    "Melancholy",
    "Enigmatic",
    "Calm",
)

INTERESTS = (
    "Fine whiskey, wine, beer",
    "Fine food, restaurants",
    "Fine clothes, jewelry, furs",
    "Fine arts, opera, theater",
    "Painting, drawing, sculpture",
    "History, legends",
    "Architecture, furnishings",
    "Poetry, novels, writing",
    "Pit-fighting, duels",
    "Forgotten gods",
    "Chruch of Ecstasy",
    "Path of Echoes",
    "Weeping Lady, charity",
    "Antiques, artifacts, curios",
    "Horses, riding",
    "Gadgets, new technology",
    "Weapons collector",
    "Music, instruments, dance",
    "Hunting, shooting",
    "Cooking, gardening",
    "Gambling, cards, dice",
    "Natural philosophy",
    "Drugs, essences, tobacco",
    "Lovers, romance, trysts",
    "Parties, social events",
    "Exploration, adventure",
    "Pets (birds, dogs, cats)",
    "Craft (leatherwork, etc.)",
    "Ships, boating",
    "Politics, journalism",
    "Arcane books, rituals",
    "Spectrology, electroplasm",
    "Alchemy, medicine",
    "Essences, alchemy",
    "Demon lore, legends",
    "Pre-cataclysm legends",
)

QUIRKS = (
    "Superstitious. Believes in signs, magic numbers.",
    "Devoted to their family.",
    "Married into important / powerful family.",
    "Holds their position to spy for another faction.",
    "Reclusive. Prefers to interact via messengers.",
    "Massive debts (to banks / criminals / family)",
    "Blind to flaws in friends, allies, family, etc.",
    "Once hollowed, then restored. Immune to spirits.",
    "Has chronic illness that requires frequent care.",
    "Secretly (openly?) controlled by possessing spirit.",
    "Serves a demon’s agenda (knowingly or not).",
    "Proud of heritage, traditions, native language.",
    "Concerned with appearances, gossip, peers.",
    "Drug / alcohol abuser. Often impaired by their vice.",
    "Holds their position due to blackmail.",
    "Relies on council to make decisions.",
    "Involved with war crimes from the Unity War.",
    "Leads a double life using cover identity.",
    "Black sheep / outcast from family or organization.",
    "In prison or under noble’s house arrest.",
    "Well-traveled. Connections outside Doskvol.",
    "Revolutionary. Plots against the Imperium.",
    "Inherited their position. May not deserve / want it.",
    "Celebrity. Popularized in print / song / theater.",
    "Scandalous reputation (deserved or not).",
    "Surrounded by sycophants, supplicants, toadies.",
    "Spotless reputation. Highly regarded.",
    "Bigoted against culture / belief / social class.",
    "Visionary. Holds radical views for future.",
    "Cursed, haunted, harassed by spirits or demon.",
    "Intense, unreasonable phobia or loathing.",
    "Extensive education on every scholarly subject.",
    "Keeps detailed journals, notes, records, ledgers.",
    "Is blindly faithful to an ideal, group, or tradition.",
    "Deeply traditional. Opposed to new ideas.",
    "A fraud. Some important aspect is fabricated.",
)

FIRST_NAMES = (
    "Adric",
    "Aldo",
    "Amosen",
    "Andrel",
    "Arden",
    "Arlyn",
    "Arquo",
    "Arvus",
    "Ashlyn",
    "Branon",
    "Brace",
    "Brance",
    "Brena",
    "Bricks",
    "Candra",
    "Carissa",
    "Carro",
    "Casslyn",
    "Cavelle",
    "Clave",
    "Corille",
    "Cross",
    "Crowl",
    "Cyrene",
    "Daphnia",
    "Drav",
    "Edlun",
    "Emeline",
    "Grine",
    "Helles",
    "Hix",
    "Holtz",
    "Kamelin",
    "Kelyr",
    "Kobb",
    "Kristov",
    "Laudius",
    "Lauria",
    "Lenia",
    "Lizete",
    "Lorette",
    "Lucella",
    "Lynthia",
    "Mara",
    "Milos",
    "Morlan",
    "Myre",
    "Narcus",
    "Naria",
    "Noggs",
    "Odrienne",
    "Orlan",
    "Phin",
    "Polonia",
    "Quess",
    "Remira",
    "Ring",
    "Roethe",
    "Sesereth",
    "Sethla",
    "Skannon",
    "Stavrul",
    "Stev",
    "Syra",
    "Talitha",
    "Tesslyn",
    "Thena",
    "Timoth",
    "Tocker",
    "Una",
    "Vaurin",
    "Veleris",
    "Veretta",
    "Vestine",
    "Vey",
    "Volette",
    "Vond",
    "Weaver",
    "Wester",
    "Zamira",
)

LAST_NAMES = (
    "Ankhayat",
    "Arran",
    "Athanoch",
    "Basran",
    "Boden",
    "Booker",
    "Bowman",
    "Breakiron",
    "Brogan",
    "Clelland",
    "Clermont",
    "Coleburn",
    "Comber",
    "Daava",
    "Dalmore",
    "Danfield",
    "Dunvil",
    "Farros",
    "Grine",
    "Haig",
    "Helker",
    "Helles",
    "Hellyers",
    "Jayan",
    "Jeduin",
    "Kardera",
    "Karstas",
    "Keel",
    "Kessarin",
    "Kinclaith",
    "Lomond",
    "Maroden",
    "Michter",
    "Morriston",
    "Penderyn",
    "Prichard",
    "Rowan",
    "Sevoy",
    "Skelkallan",
    "Skora",
    "Slane",
    "Strangford",
    "Strathmill",
    "Templeton",
    "Tyrconnell",
    "Vale",
    "Walund",
    "Welker",
)

ALIASES = (
    "Bell",
    "Birch",
    "Bricks",
    "Bug",
    "Chime",
    "Coil",
    "Cricket",
    "Cross",
    "Crow",
    "Echo",
    "Flint",
    "Frog",
    "Frost",
    "Grip",
    "Gunner",
    "Hammer",
    "Hook",
    "Junker",
    "Mist",
    "Moon",
    "Nail",
    "Needle",
    "Ogre",
    "Pool",
    "Ring",
    "Ruby",
    "Silver",
    "Skinner",
    "Song",
    "Spur",
    "Tackle",
    "Thistle",
    "Thorn",
    "Tick-Tock",
    "Twelves",
    "Vixen",
    "Whip",
    "Wicker",
)

LOOKS = (
    "Large",
    "Lovely",
    "Weathered",
    "Chiseled",
    "Handsome",
    "Athletic",
    "Slim",
    "Dark",
    "Fair",
    "Stout",
    "Delicate",
    "Scarred",
    "Bony",
    "Worn",
    "Rough",
    "Plump",
    "Wiry",
    "Striking",
    "Short",
    "Tall",
    "Sexy",
    "Wild",
    "Elegant",
    "Stooped",
    "Cute",
    "Plain",
    "Old",
    "Young",
    "Stylish",
    "Strange",
    "Disfigured, Maimed",
    "Glasses, Monocle",
    "Prosthetic, Crippled",
    "Long Hair, Beard, Wig",
    "Shorn, Bald",
    "Tattooed",
)

GOALS = (
    "Wealth",
    "Power",
    "Authority",
    "Prestige, Fame",
    "Control",
    "Knowledge",
    "Pleasure",
    "Revenge",
    "Freedom",
    "Achievement",
    "Happiness",
    "Infamy, Fear",
    "Respect",
    "Love",
    "Change",
    "Chaos, Destruction",
    "Justice",
    "Cooperation",
)

PREFERRED_METHODS = (
    "Violence",
    "Threats",
    "Negotiation",
    "Study",
    "Manipulation",
    "Strategy",
    "Theft",
    "Arcane",
    "Commerce",
    "Hard Work",
    "Law, Politics",
    "Sabotage",
    "Subterfuge",
    "Alchemy",
    "Blackmail",
    "Teamwork",
    "Espionage",
    "Chaos",
)


class Person:
    """A class to represent a random person you meet in Doskvol"""

    def __init__(self):
        self.gender = roll_gender()
        self.looks = random.choice(LOOKS)
        self.goals = random.choice(GOALS)
        self.preferredMethods = random.choice(PREFERRED_METHODS)
        self.profession = None
        self.trait = random.choice(TRAITS)
        self.interests = random.choice(INTERESTS)
        self.quirk = random.choice(QUIRKS)
        self.first_name = random.choice(FIRST_NAMES)
        self.last_name = random.choice(LAST_NAMES)
        self.alias = random.choice(ALIASES)
