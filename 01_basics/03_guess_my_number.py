guess: int = 34
number = input("Guess my number ")

while(guess != int(number)):
    if (int(number) > guess):
        print("Your guess is too high")
    elif (int(number) < guess):
        print("Your guess is too low")
    number = input("Guess my number ")

print(f"Congrats! The number was: {number}")