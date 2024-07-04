def display(word, guessed_letters):
    word_print = ""
    for letter in word:
        if letter in guessed_letters:  # if the guessed_letters list is part of the word
            word_print += letter + " "
        else:  # if the letter in the word is not guessed yet, put an underscore and a space after
            word_print += "_ "
    return word_print.strip()

def hangman():
    word = "your word"
    guessed_letters = []
    lives = 3

    print("Lives:", lives)
    print("Word:", display(word, guessed_letters))

    while #_____:
        # receive an input for the choice of the letter
        #

        # check if letter is already guessed
        #
        #
        # continue the while loop because after going through an if statement, python
        # automatically exits out of the while loop
        #


        # add letter to the list of guessed letters
        guessed_letters.append(letter)

        # check if the letter is in the word
        #
        # if letter is not in the word, take away a life and show how many lifes are remaining
        #
        #
        #

        # show the updated screen
        current_screen = display(word, guessed_letters)
        print("Word:", current_screen)

        # if an underscore is NOT in the screen, we know that we guessed all the letters so we win!
        #
        # print out a congratulations message
        #
        # use break to break out of our if statement!


    # outside the while loop, if we are at 0 lives, we lose the game
    #
    #


if __name__ == "__main__":
    hangman()
