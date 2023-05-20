import streamlit as st
import random

# List of healthy words
healthy_words = ['exercise', 'nutrition', 'wellness', 'hydrate', 'balance']

def main():
    st.title("Healthy Word Scramble")
    st.write("Welcome to the Healthy Word Scramble Game!")
    st.write("Unscramble the letters to form a healthy word.")

    # Get a random word from the list
    word = random.choice(healthy_words)

    # Scramble the word
    scrambled_word = scramble_word(word)

    # Display the scrambled word
    st.subheader("Scrambled Word:")
    st.write(scrambled_word)

    # User input field
    user_input = st.text_input("Enter your answer")

    # Check if the answer is correct
    if user_input.lower() == word:
        st.success("Congratulations! Your answer is correct.")
    elif user_input != '':
        st.error("Oops! Your answer is incorrect. Try again.")

    # Play again button
    if st.button("Play Again"):
        main()

def scramble_word(word):
    # Shuffle the letters of the word
    letters = list(word)
    random.shuffle(letters)
    scrambled_word = ''.join(letters)
    return scrambled_word

if __name__ == '__main__':
    main()
