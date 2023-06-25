#! python3
'''
A word game where your goal is to guess each letter of a preselected word.
If you guess incorrectly six times, you lose. Each time you guess incorrectly,
the console will print a piece of a man hanging in a scaffold. Hence the name
Hangman.
'''
import random


def print_scaffold(guesses, wd):
    # Print the scaffold arrangmenet based on the nubmer of times the user
    # failed to guess the correct letter.
    if guesses == 0:
        print('''\
    _________
    |	 |
    |
    |
    |
    |
    |________''')
    elif guesses == 1:
        print('''\
    _________
    |	 |
    |	 O
    |
    |
    |
    |________''')
    elif guesses == 2:
        print('''\
    _________
    |	 |
    |	 O
    |	 |
    |	 |
    |
    |________''')
    elif (guesses == 3):
        print('''
    _________
    |	 |
    |	 O
    |	\|
    |	 |
    |
    |________''')
    elif (guesses == 4):
        print('''
    _________
    |	 |
    |	 O
    |	\|/
    |	 |
    |
    |________''')
    elif (guesses == 5):
        print('''\
    _________
    |	 |
    |	 O
    |	\|/
    |	 |
    |	/
    |________''')
    elif (guesses == 6):
        print(guesses)
        print('''\
    _________
    |	 |
    |	 O
    |	\|/
    |	 |
    |	/ \\
    |________''')
        print("\n")
        print('The word was "%s".' % wd)
        print("\n")
        print("\nYOU LOSE! TRY AGAIN!")
        print("\nWould you like to play again, type 1 for yes or 2 for no?")
        again = str(input("> "))
        again = again.lower()
        if again == "1":
            hangMan()  # restarts a new game if user types '1'
    return


def selectWord():
    # Function that selects a word from a text file called "FREQ.txt" and
    # strips that word of all unnecessary characters.
    file = open('FREQ.txt', 'r')
    words = file.readlines()
    file.close()
    myword = 'a'
    while len(myword) < 4:  # makes sure word is at least 4 letters long
        myword = random.choice(words)
    myword = str(myword).strip('[]')
    myword = str(myword).strip("''")
    myword = str(myword).strip("\n")
    myword = str(myword).strip("\r")
    myword = myword.lower()
    return myword


def hangMan():
    # The main game loop. It assigns the word selected by the selectWord
    # function to word, and prints blanks to the consoel representing the
    # number of letters in the word.
    guesses = 0
    word = selectWord()
    word_list = list(word)  # contains a list of all letters in the word
    blanks = "_" * len(word)  # empty letters that are printed to console
    blanks_list = list(blanks)  # list of the blanks
    new_blanks_list = list(blanks)
    guess_list = []  # will contain all guessed letters

    print("Let's play hangman!\n")
    print_scaffold(guesses, word)  # prints the first scaffold scheme
    print("\n")
    print("    " + ' '.join(blanks_list))
    print("\n")
    print("Guess a letter.\n")

    while guesses < 6:
        # this loop repeats so long as the player has not exceeded the
        # allowed number of gueses.

        guess = str(input("> "))
        guess = guess.lower()

        if len(guess) > 1:
            # ensures the user enters only one letter.
            print("Stop cheating! Enter one letter at time.")
        elif guess == "":
            # informs the user that blanks are not valid.
            print("Don't you want to play? Enter one letter at a time.")
        elif guess in guess_list:
            # if the letter has already been guessed, provide a list of the
            # guessed letters and ask for a new letter.
            print("You already guessed that letter!\
                  Here is what you've guessed: ")
            print(' '.join(guess_list))
        else:
            guess_list.append(guess)  # adds letters to guess_list
            i = 0
            while i < len(word):
                if guess == word[i]:  # if the guess is in the word
                    new_blanks_list[i] = word_list[i]  # blank list updated
                i += 1

            if new_blanks_list == blanks_list:
                print("Your letter isn't here.")
                guesses += 1
                print_scaffold(guesses, word)

                if guesses < 6:
                    print("Guess again.")
                    print(' '.join(blanks_list))

            elif word_list != blanks_list:
                blanks_list = new_blanks_list[:]
                print(' '.join(blanks_list))

            if word_list == blanks_list:
                print("\nYOU WIN! Here is your prize:")
                print("\n")
                print("Would you like to play again?")
                print("Type 1 for yes or 2 for no.")
                again = str(input("> "))
                if again == "1":
                    hangMan()
                quit()

            else:
                print("Great guess! Guess another!")


hangMan()
