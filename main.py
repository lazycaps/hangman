import getpass

guesses = 0
wins = 0
game_won = False


# Python code to convert string to list character-wise
def convert(string):
    list1 = []
    list1[:0] = string
    return list1


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
word_list = convert(word)
blanks_list = convert(blanks)
# Convert word to list

remaining_word_length = len(word)

while ''.join(blanks_list) != ''.join(word_list):
    print(''.join(blanks_list))
    guess = input("Guess a letter: ")
    if not str.isalpha(guess):
        print("Please use an alphabetic character.")

    elif len(guess) != 1:
        print("Please only guess one letter.")

    else:
        if word.lower().count(guess.lower()) >= 1:
            guess_occurrences = word.lower().count(guess.lower())
            indexes = [
                index for index in range(len(word))
                if word.startswith(guess, index)
            ]
            for idx, x in enumerate(blanks_list):
                # print(idx, x)
                if word_list[idx] == guess:
                    blanks_list[idx] = guess
            print("Yes! The letter", guess, "is in the word", guess_occurrences, "times.")
            remaining_word_length = remaining_word_length - guess_occurrences
            # print(remaining_word_length)
            # print(indexes)
            # Debug purposes only ^

        else:
            print("No, the letter", guess, "is not in the word.")

print("You guessed the word! Thanks for playing!")
