import tkinter as tk
from tkinter import *

chances = 6
guesses = set()
word_valid = ""
blanks_list = []
remaining_word_length = ""


def convert(string):
    return list(string)


def validate_input():
    global word_valid
    global blanks_list
    global remaining_word_length
    word_valid = word.get()
    if word_valid.isalpha():
        blanks_list = convert("_" * len(word_valid))
        print("good")
        remaining_word_length = len(word_valid)
        guess.config(state="normal")
        guess_button.config(state="normal")
        word.config(state="disabled")
        word_button.config(state="disabled")
    else:
        print("bad")
        update_label_visibility()


def validate_guess():
    global blanks_list
    global remaining_word_length
    guess_valid = guess.get().lower()
    if guess_valid.isalpha() and len(guess_valid) == 1:
        if word_valid.lower().count(guess_valid) >= 1:
            guess_occurrences = word_valid.lower().count(guess_valid)
            remaining_word_length = guess_occurrences - word_valid.lower().count(guess_valid)
            guesses.add(guess_valid)
            for idx, x in enumerate(word_valid.lower()):
                if x == guess_valid:
                    blanks_list[idx] = word_valid[idx]
            print("work")
            print(remaining_word_length)
        else:
            print("bad")
            update_guess_visibility()


def update_label_visibility():
    if not word_valid.isalpha():
        word_bad_label.pack()
    else:
        word_bad_label.pack_forget()


def update_guess_visibility():
    guess_valid = guess.get().lower()
    if not guess_valid.isalpha() or len(guess_valid) != 1:
        guess_bad_label.pack()
    else:
        guess_bad_label.pack_forget()


def buttonclick():
    print("Test")


window = Tk()
window.geometry("420x420")
window.title("Hangman Game")
window.config(background="black")

info_label = tk.Label(
    window,
    text='You have 6 lives to guess the word.\nWhen you run out of lives, the game ends.',
    bg="black"
)
info_label.pack()

word_bad_label = tk.Label(window, text="Please make the word only have letters.")
word_bad_label.pack_forget()

word_label = tk.Label(window, text="Enter a word:", bg="black")
word_label.pack()

word = Entry(window, width=40, bg="gray", show="*")
word.pack()

word_button = tk.Button(window, text='Confirm', width=25, bg="gray", command=validate_input)
word_button.pack()

guess_bad_label = tk.Label(
    window,
    text="Please make the guess be alphabetical and have only 1 letter."
)
guess_bad_label.pack_forget()

guess_label = tk.Label(window, text="Guess a letter:", bg="black")
guess_label.pack()

guess = Entry(window, width=40, bg="gray")
guess.pack()
guess.config(state="disabled")

guess_button = tk.Button(window, text='Confirm', width=25, bg="gray", command=validate_guess)
guess_button.pack()
guess_button.config(state="disabled")

blanks_label_display = tk.Label(window, text=blanks_list, bg="black")
blanks_label_display.pack()

window.mainloop()
