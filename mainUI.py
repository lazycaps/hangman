import tkinter as tk
from tkinter import *

chances = 6
guesses = set()
word_valid = ""
blanks_list = []
remaining_word_length = ""


def convert(string):
    return list(string)


def update_chances_label():
    chances_label_display.config(text="You have " + str(chances) + " chances remaining.")
    guesses_string = ", ".join(guesses)  # Convert the set to a string with comma-separated values
    repeated_guess_display.config(text="You have already guessed that letter. \nYou have guessed: " + guesses_string)


def validate_input_or_guess():
    # Check the current focus and call the appropriate function
    if str(window.focus_get()) == str(word):
        validate_input()
    elif str(window.focus_get()) == str(guess):
        validate_guess()


def validate_input():
    global word_valid
    global blanks_list
    global remaining_word_length
    word_valid = word.get()
    if word_valid.isalpha():
        blanks_list = convert("_" * len(word_valid))
        blanks_label_display.pack()
        word_bad_label.pack_forget()
        print("good")
        remaining_word_length = len(word_valid)
        guess.config(state="normal")
        guess_button.config(state="normal")
        word.config(state="disabled")
        word_button.config(state="disabled")
        chances_label_display.pack()
    else:
        print("bad")
        update_label_visibility()


def validate_guess():
    global blanks_list
    global remaining_word_length
    global chances
    global guesses
    guess_bad_label.pack_forget()
    guess_valid = guess.get().lower()
    if chances == 1:
        guess.config(state="disabled")
        guess_button.config(state="disabled")
        lolded.pack()
        lolded_button.pack()
    if guess_valid in guesses:
        print("already guessed")
        print(guesses)
        repeated_guess_display.pack()
        guess.delete(0, "end")
        return
    if guess_valid.isalpha() and len(guess_valid) == 1:
        guesses.add(guess_valid.lower())
        update_chances_label()
        if guess_valid.lower() in word_valid.lower():
            guess_bad_label.pack_forget()
            if word_valid.lower().count(guess_valid.lower()) >= 1:
                guess_occurrences = word_valid.lower().count(guess_valid.lower())
                remaining_word_length = guess_occurrences - word_valid.lower().count(guess_valid.lower())
                for idx, x in enumerate(word_valid.lower()):
                    if x == guess_valid.lower():
                        blanks_list[idx] = word_valid[idx]
                blanks_label_display.config(text="".join(blanks_list))
                incorrect_label_display.pack_forget()
                guess_bad_label.pack_forget()
                incorrect_label_display.pack_forget()
                print("work")
                print(remaining_word_length)
                if "_" not in blanks_list:
                    end_label_display.pack()
                    guess.config(state="disabled")
                    guess_button.config(state="disabled")
                guess.delete(0, "end")
                print(guesses)
        else:
            print("Guess not in the word.")
            guess.delete(0, "end")
            incorrect_label_display.pack()
            chances = chances - 1
            chances_label_display.pack()
            update_chances_label()
            print(chances)
            print(guesses)
    else:
        print("bad case 2")
        update_guess_visibility()
        update_chances_label()
        guess.delete(0, "end")


def update_label_visibility():
    if not word_valid.isalpha():
        word_bad_label.pack()
    else:
        word_bad_label.pack_forget()


def update_guess_visibility():
    guess_valid = guess.get().lower()
    if not guess_valid.isalpha() or len(guess_valid) == 1:
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

word_bad_label = tk.Label(window, text="Please make the word only have letters.", background="red")
word_bad_label.pack_forget()

word_label = tk.Label(window, text="Enter a word:", bg="black")
word_label.pack()

word = Entry(window, width=40, bg="gray", show="*")
word.pack()

word_button = tk.Button(window, text='Confirm', width=25, bg="gray", command=validate_input)
word_button.pack()

guess_bad_label = tk.Label(window, text="Please make the guess be alphabetical and have only 1 letter.",
                           background="red")
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
blanks_label_display.pack_forget()

chances_label_display = tk.Label(window, text="You have " + str(chances) + " chances remaining.")
chances_label_display.pack_forget()

repeated_guess_display = tk.Label(window, text="You have already guessed that letter. \nYou have guessed: " +
                                               str(guesses))
repeated_guess_display.pack_forget()

incorrect_label_display = tk.Label(window, text="That letter is not in the word.", bg="red")
incorrect_label_display.pack_forget()

lolded = tk.Label(window, bg="red", text="You ran out of chances. Press the button to exit.")
lolded.pack_forget()

lolded_button = tk.Button(window, text="Exit", bg="red", command=window.destroy)
lolded_button.pack_forget()

end_label_display = tk.Label(window, text="You guessed the word!", background="green")
end_label_display.pack_forget()

window.bind('<Return>', lambda event: validate_input_or_guess())

window.mainloop()
