guesses = 0
wins = 0


while True:
    word = input("Think of a word or press Q to quit: ").lower()
    blanks = '_' * len(word)
    if word == "q":
        break
    word_valid = str.isalpha(word)
    if not word_valid:
        print("Please make the word has no numbers, spaces or special characters.")
        continue

while blanks != word:
    print(blanks)
    guess = input("Guess a letter:").lower()
    if len(guess) != 1:
        print("Please only guess one letter.")
        continue
    # word.count('guess')
