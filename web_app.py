import streamlit as st
import json
import os
import random

WORDS_FILE = "global_database_words.json"
CHOSEN_FILE = "global_database_chosen.json"

def get_words():
    if not os.path.exists(WORDS_FILE):
        return []
    try:
        with open(WORDS_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_words(word_list):
    with open(WORDS_FILE, "w") as f:
        json.dump(word_list, f)

def get_chosen():
    if not os.path.exists(CHOSEN_FILE):
        return "No word chosen yet"
    try:
        with open(CHOSEN_FILE, "r") as f:
            return json.load(f)
    except:
        return "No word chosen yet"

def set_chosen(word):
    with open(CHOSEN_FILE, "w") as f:
        json.dump(word, f)

st.title("Random Word Picker")

# Input field to add words
user_input = st.text_input("Enter words (separated by spaces):")
if st.button("Create"):
    if user_input.strip():
        current_list = get_words()
        updated_list = current_list + user_input.split()
        save_words(updated_list)
        st.success("Words added successfully.")

# Button to pick a random word
if st.button("Random Word"):
    current_list = get_words()
    if current_list:
        chosen_word = random.choice(current_list)
        set_chosen(chosen_word)
    else:
        st.warning("The word list is empty.")

# Display current chosen word
st.divider()
active_word = get_chosen()
st.subheader(f"The chosen word is: {active_word}")
