import streamlit as st

def find_the_treasure_streamlit():
    st.title("Find the Treasure Game")
    st.write("Welcome to the 'Find the Treasure' game!")
    st.write("Choose a number between 1 and 20 as the treasure location.")
    st.write("The computer will try to find the treasure using the least possible steps.")

    # User inputs the treasure location
    treasure_location = st.number_input("Enter the treasure's location (1-20):", min_value=1, max_value=20, step=1, format="%d")

    if st.button("Start the Game"):
        st.write("The computer will now try to find the treasure...")

        # Computer uses binary search to guess the treasure location
        low = 1
        high = 20
        guesses = 0

        while low <= high:
            guesses += 1
            guess = (low + high) // 2
            st.write(f"Step {guesses}: Checking clue at number {guess}...")

            if guess < treasure_location:
                st.write("Too low!")
                low = guess + 1
            elif guess > treasure_location:
                st.write("Too high!")
                high = guess - 1
            else:
                st.success(f"The computer found the treasure at number {guess}!")
                st.write(f"It took {guesses} guesses to find the treasure.")
                break

        st.write("Thank you for playing 'Find the Treasure'!")

if __name__ == "__main__":
    find_the_treasure_streamlit()
