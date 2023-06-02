import getpass

chances = 6
word = 0
guesses = []


# Python code to convert string to list character-wise
def convert(string):
    list1 = []
    list1[:0] = string
    return list1


while word == 0:
    word = getpass.getpass("Think of a word or press Q to quit: ").lower()
    blanks = '_' * len(word)
    if word == "q":
        print("Thanks for playing!")
        quit()
    word_valid = str.isalpha(word)
    if not word_valid:
        print("Please make the word has no numbers, spaces or special characters.")
        word = 0

word_list = convert(word)
blanks_list = convert(blanks)
# Convert word to list

remaining_word_length = len(word)

while remaining_word_length != 0:
    print(''.join(blanks_list))
    guess = input("Guess a letter: ").lower()
    if not str.isalpha(guess):
        print("Please use an alphabetic character.")
        continue

    elif len(guess) != 1:
        print("Please only guess one letter.")
        continue

    if guess in guesses:
        print("That letter has already been guessed!")
        print("You have guessed these letters: ", guesses)

    else:
        if word.count(guess) >= 1:
            guess_occurrences = word.count(guess)
            guesses.append(guess)
            indexes = [
                index for index in range(len(word))
                if word.startswith(guess, index)
            ]
            for idx, x in enumerate(blanks_list):
                if word_list[idx] == guess:
                    blanks_list[idx] = guess
            print("Yes! The letter", guess, "is in the word", guess_occurrences, "times.")
            remaining_word_length = remaining_word_length - guess_occurrences

        elif chances == 1:
            print("You ran out of chances.")
            exit()

        else:
            print("No, the letter", guess, "is not in the word.")
            guesses.append(guess)
            chances = chances - 1
            print("You now have", chances, "lives.")

print("You guessed the word!")
print("The word was:", word)
