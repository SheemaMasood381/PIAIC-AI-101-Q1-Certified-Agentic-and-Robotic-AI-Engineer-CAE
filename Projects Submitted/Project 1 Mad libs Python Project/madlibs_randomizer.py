"""
Project 02: Madlibs Randomizer

This Python project randomly selects a Madlib template from a set of predefined templates and generates a Madlib story. 
The templates are imported from separate modules, and the script uses the `random.choice` function to select one at random.

Modules:
- code: Contains a Madlib template related to programming.
- hp: Contains a Harry Potter-themed Madlib template.
- hunger_games: Contains a Hunger Games-themed Madlib template.
- zombie: Contains a zombie-themed Madlib template.

How it works:
1. The script imports the Madlib templates from the specified modules.
2. It uses `random.choice` to select one of the imported modules.
3. It calls the `madlib` function from the selected module to generate and print a Madlib story.

Instructions:
1. Ensure that the `samples` package contains the modules `code`, `hp`, `hunger_games`, and `zombie`.
2. Run this script to generate a random Madlib story.

"""

from samples import code, hp, hunger_games, zombie
import random

if __name__ == "__main__":
    m = random.choice([code, hp, hunger_games, zombie])
    m.madlib()