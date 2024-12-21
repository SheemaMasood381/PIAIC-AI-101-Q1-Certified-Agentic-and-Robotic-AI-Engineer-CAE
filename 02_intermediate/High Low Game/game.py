import random
def generate_two_random_numbers():
    return random.randint(1,100), random.randint(1,100) 

score: int = 0

print("""Welcome to the High-Low Game!
--------------------------------""")

rounds = int(input("How many rounds you wnat to play? "))
for i in range(rounds):
    print(f"Rount {i+1}")
    numbers = generate_two_random_numbers()
    print(f"Your number is {numbers[0]}")
    guess = input("Do you think your number is higher or lower than the computer's?: ")
    if (guess.lower() == 'higher' and numbers[0] > numbers[1]):
        score = score + 1
        print(f"""
            You were right! The computer's number was {numbers[1]}
            Your score is now {score}
        """)
    elif (guess.lower() == 'lower' and numbers[0] < numbers[1]):
        score = score + 1
        print(f"""
            You were right! The computer's number was {numbers[1]}
            Your score is now {score}
        """)
    else:
        print(f"""
            Aww, that's incorrect. The computer's number was {numbers[1]}
            Your score is now {score}
        """)

print(f"Your score is {score}")
print("Thanks for playing!")