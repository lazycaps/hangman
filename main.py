import getpass

guesses = 0
wins = 0

game_won = False

while True:
    word = getpass.getpass("Think of a word or press Q to quit: ").lower()
    blanks = '_' * len(word)
    if word == "q":
        print("Thanks for playing!")
        quit()
    word_valid = str.isalpha(word)
    if not word_valid:
        print("Please make the word has no numbers, spaces or special characters.")
        continue
    else:
        break

remaining_word_length = len(word)

while remaining_word_length != 0:
    print(blanks)
    guess = input("Guess a letter: ")
    if not str.isalpha(guess):
        print("Please use an alphabetic character.")

    elif len(guess) != 1:
        print("Please only guess one letter.")

    else:
        if word.lower().count(guess.lower()) >= 1:
            guess_result = word.lower().count(guess.lower())
            print("Yes! The letter", guess, "is in the word", guess_result, "times.")
            remaining_word_length = remaining_word_length - guess_result
            print(remaining_word_length)
        else:
            print("No, the letter", guess, "is not in the word.")

    # word.count('guess')
print("You guessed the word! Thanks for playing!")
