import random

def generate_story():
    # User inputs
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    action = input("Enter an action: ")
    animal = input("Enter an animal: ")

    # Random story components
    adjectives = ["brave", "clever", "funny", "mysterious", "kind"]
    objects = ["sword", "key", "book", "map", "torch"]
    places = ["castle", "forest", "mountain", "beach", "cave"]
    animals = ["lion", "eagle", "dolphin", "tiger", "unicorn"]

    # Generate the story
    story = f"Once upon a time, there was a {adjectives[random.randint(0, 4)]} adventurer named {name}."
    story += f"\n{name} embarked on a journey to the {place} to {action}."
    story += f"\nOn the way, {name} encountered a {adjectives[random.randint(0, 4)]} {animal}."
    story += f"\nWith their trusty {objects[random.randint(0, 4)]}, {name} and the {animal} ventured into the {places[random.randint(0, 4)]}."
    story += f"\nThe journey was filled with excitement and danger, but in the end, {name} and the {animal} emerged victorious!"

    # Print the story
    print("\nHere's your random story:\n")
    print(story)

# Generate a story when the program runs
generate_story()
