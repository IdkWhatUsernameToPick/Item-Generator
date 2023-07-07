import random
import os

owners = ['Doctor', 'Archer', 'Magician', 'Warrior', 'Killer', 'Serial Killer', 'Potion Seller', 'Scout', 'Soldier', 'Pyro', 'Demoman', 'Heavy', 'Engineer', 'Medic', 'Sniper', 'Spy', 'Hunter', 'Mom', 'Dad', 'God', 'Devil', 'Terrorist']
adjectives = ['Mighty', 'Cunning', 'Powerful', 'Swift', 'Wise', 'Sneaky', 'Chromatic', 'Legendary', 'Mythic', 'Epic', 'Uncommon', 'Common', 'Godlike', 'Invisible', 'Diamond', 'Gold', 'Iron', 'Steel', 'Insane', 'Broken', 'Old', 'New']
nouns = ['Staff', 'Sword', 'Wand', 'Bow', 'Dagger', 'Gloves', 'Knife', 'Table', 'Card', 'Card Deck', 'Photo', 'Belt', 'Crossbow', 'Potion', 'Mace', 'Minigun', 'Uzi', 'Pistol', 'Scissors', 'Dick', 'Phone', 'PC', 'Crystal Ball', 'Chicken Wing']
verbs = ['Killing', 'Dancing', 'Flying', 'Healing', 'Invisibility', 'Mind Reading', 'Godly Powers', 'Mind Control', 'Fire', 'Water', 'Wind', 'Earth', 'Thunderstorm', 'Infinite Knowledge', 'Electricity', 'Summoning', 'Life Steal', 'Time Control']

def generate_phrase():
    owner = random.choice(owners)
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    return f"Generated: {owner}'s {adjective} {noun} of {verb}"

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear console screen
    phrase = generate_phrase()
    print(phrase)

    choice = input("Generate another phrase? (1) Yes / (2) No: ")
    if choice == '2':
        break
