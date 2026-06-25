#RANDOM EXCUSE GENERATOR
import random

subjects = [
    "My pet goat",
    "My neighbor",
    "A mysterious wizard",
    "An alien",
    "My little brother",
    "A ninja",
    "A dragon",
    "A talking cat",
    "A time traveler",
    "The school principal"
]

actions = [
    "ate",
    "stole",
    "destroyed",
    "launched",
    "hid",
    "froze",
    "teleported",
    "accidentally deleted",
    "burned",
    "turned invisible around"
]

objects = [
    "my homework",
    "my laptop",
    "my science project",
    "my backpack",
    "my bicycle",
    "my phone",
    "my exam paper",
    "my notes",
    "my calculator",
    "my keyboard"
]

reasons = [
    "while I was fighting a dragon",
    "during a zombie invasion",
    "because the moon exploded",
    "while saving the world",
    "during a secret mission",
    "because gravity stopped working",
    "while escaping aliens",
    "during a pirate attack",
    "because a wizard cursed me",
    "while traveling through time"
]

locations = [
    "at school",
    "in the jungle",
    "on Mars",
    "inside a volcano",
    "under the ocean",
    "at a secret laboratory",
    "in another dimension",
    "inside a spaceship"
]
def excuse_printer():
 print("Welcome to Random Excuse Generator!")
 print("Developer : Mukund Jha")
 print("")
 print(f"{random.choice(subjects)} {random.choice(actions)} {random.choice(objects)} {random.choice(reasons)} {random.choice(locations)}.")

excuse_printer()