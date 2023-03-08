    # Hangman
    ### Video Demo:  https://youtu.be/B7kX40KsV1M
    #### Description:

    This project is a python adaptation of the common game Hangman, can be played only from the command line interface and contains no graphics. Although the game itself is very simple, the code is not so, the code contains validation functions to avoid any user error, six different categories to play, as well of three different difficulty levels to increase the challenge and at last but not least whithin the same execution of the game, you can consult your game stats of what you have played so far.

    As mentioned before the game contains 6 categories to play with, which are: animals, movies, food, clothes, plants and famous persons, these categores contains related words to the topic, so it becomes easier to guess. After selecting one category, all categories except from famous persons contains three difficulty levels: easy, medium and hard. Each level determines the lenght of the word or words to guess.

    Once these options have been chosen by the user the game starts, the user will now have 8 tries to try to guess the word. In the screen the user will see the tries he has left, the incorrect letters and the incorrect word guesses he had tried, the user also will see '_ _ _ _' or as many underscores as the word has.

    The user will now try to guess the word either by typing a letter or by typing a full word, if the guess is wrong the word or letter will appear on the screen as a reminder of what have been tried. If the user got a letter correctly the underscore will change to the letter or letters the word has '_ _ e _ e' or if the user guesses the word correctly the word appears complete and he wins the game.

    If the user repeats a letter or a word, the program prompts the user to try again without adding a miss, if the user runs out of chances, the game reveals the word and the user loses the game and the program returns to the main menu, so the user can choose to play again, see their in game stats or exit the game.

    Now lets talk of what is inside the game, the program consists of one class, one main function and 5 functions.

    For the main function, is the core of the game, from there all secondary functions and the class can be called, and contains a loop to keep playing until the user says otherwise.

    So the game starts, the code enters the loop and prompts the user for a category, the user then can select a category by typing a number from 1 to 6 or typing the name of the category, from there main calls the function category_validation to validate if the user prompted a valid option for category, if the option is invalid, then the program reprompts the user, if the option is valid then continues to the difficulty selection.

    Again, main calls a second function difficulty_validation to prompt and validate the user to choose a difficulty whether by number or text, if the option is invalid the program reprompts the user until a valid difficulty is chosen and if the user prompts a correct difficulty the program returns to main.

    Then main calls a function called category_words which receives two arguments, category and difficulty. Then the function from a predefined lists of words, choose a list depending on the category, filter the list according to the difficulty and returns a word of an expected length and topic.

    Finally, main calls the function hangman which receives the word and inmediately a second function called generate incognito is called to create a string with the number of underscores and spaces depending on the lenght of the word and returns that string. From there hangman returns to the stage and enters a loop that will be cycling while there are any attempts left, prompt the user for a letter or word and change the underscore with a letter or the complete word if guessed correctly. Wether the word is guessed correctly or failed the game returns to the main menu either to continue playing, check the stats or exit the game.

    Once the game returns to the main menu the Game_Stats object is called and update the stats accordingly if the previous game was won or lost and keeps record of which words have been guessed or missed.

    This was CS50P :D