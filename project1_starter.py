"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Noble McGregor
Date: 10/22/25

AI Usage: Utilizing ai to debug file creation has been a great help, finding out how to use incoding helped as i did not know how to previously
Example: AI helped me get past case sensitivity by normalizing all characters and with how to find file directory in pc
"""

level = 1
gold = 100
def create_character(name, character_class):
    normal_class = character_class.lower()
    """
    name = input(f"Please enter your name: ")
    character_class = input(f"Please choose a class of the following: warrior, mage, rogue, or cleric: ")
    Code to use to input name and character class when create_character is empty
    """
    
    if normal_class == "warrior":
        strength = 20
        magic = 3
        health = 150
    elif normal_class == "mage":
        strength = 5
        magic = 25
        health = 75
    elif normal_class == "rogue":
        strength = 10
        magic = 6
        health = 100
    elif normal_class == "cleric":
        strength = 7
        magic = 13
        health = 90
    else:
        return None
        
    return {"name":  name, "class": character_class, "level": level, "strength": strength, "magic": magic, "health": health, "gold": gold}
    pass

def calculate_stats(character_class, level): 
    character_class = character_class.lower()
    if character_class == "warrior":
        strength = 20 + 20 * level
        magic = 3 + 2 * level
        health = 150 + 90 * level
    elif character_class == "mage":
        strength = 5 + 2 * level
        magic = 25 + 25 * level
        health = 75 + 15 * level
    elif character_class == "rogue":
        strength = 10 + 8 * level
        magic = 6 + 4 * level
        health = 100 + 30 * level
    elif character_class == "cleric":
        strength = 7 + 5 * level
        magic = 13 + 12 * level
        health = 90 + 40 * level

    
    else:
        return None
    return (strength, magic, health)

    pass

def save_character(character, filename):
    import os
    directory = os.path.dirname(filename)

    if not isinstance(character, dict) or not filename:
        return False
    if directory and not os.path.exists(directory):
        return False

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
    return True

    pass

def load_character(filename):
    import os
    if os.path.exists(filename) == False:
        return None

    file = open(filename, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()

    character = {}
    for line in lines:
        if ": " in line:
            key, value = line.strip().split(": ", 1)
            if key == "Character Name":
                character["name"] = value
            elif key == "Class":
                character["class"] = value
            elif key == "Level":
                character["level"] = int(value)
            elif key == "Strength":
                character["strength"] = int(value)
            elif key == "Magic":
                character["magic"] = int(value)
            elif key == "Health":
                character["health"] = int(value)
            elif key == "Gold":
                character["gold"] = int(value)
    return character

    pass

def display_character(character):
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")

    pass

def level_up(character):
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    
    pass

if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    player = create_character("Joe", "warrior")
    print(player)
    print(calculate_stats("warrior", 1))
    print(calculate_stats("mage", 1))
    print(level_up("warrior"))
    print(display_character("warrior"))
