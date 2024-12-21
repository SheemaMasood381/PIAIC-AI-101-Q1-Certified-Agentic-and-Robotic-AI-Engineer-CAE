"""
Project 01: Madlibs

This is a simple Python project designed for beginners to practice string concatenation and user input.
The program generates a fun and interactive story by asking the user for different types of words 
(such as adjectives, verbs, and famous people's names) and inserting those words into a pre-defined template.

Instructions:
1. Run the script.
2. Follow the prompts to enter an adjective, two verbs, and a famous person's name.
3. The program will then print a humorous and personalized story using the words you provided.

"""

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
    I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)