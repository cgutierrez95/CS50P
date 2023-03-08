import random
def main():

    game_stats = Game_Stats()

    while True:
        try:

            print('Welcome to hangman, please select a category')
            print('1) Animals \n2) Movies \n3) Food \n4) Clothes \n5) Plants \n6) Famous Persons \n7) Game Stats \n8) Exit (CTRL + D)')

            category = input('Category: ').lower()

            if category == '8' or category.lower() == 'exit':
                print("Thank You For Playing!!")
                return

            if category == '7':
                print('\nYour Game Stats')
                print('Games Won: ', game_stats._games_won)
                print('Words Won: ', game_stats._words_won)
                print('Games Lost: ', game_stats._games_lost)
                print ('Words Lost: ' , game_stats._words_lost)
                print()
                continue

            valid = category_validation(category)

            if (category != 'Famous Persons' and category != '6') and valid:
                difficulty = difficulty_validation()
            else:
                difficulty = 'no'

            if valid:
                target_word = category_words(category, difficulty)
                game_status =  hangman(target_word)

                game_stats.add_stat(game_status, target_word)

        except EOFError:
            return

def hangman(target_word):

    used_letters = []
    user_tries = []
    misses = 0

    user_word = generate_incognito(target_word)

    while misses < 8:

        if '_' not in user_word:
            print('You guessed right the word: ', user_word)
            print("Congratuations, You won!!!\n")
            return True

        print('User Tries: \t', user_tries)
        print('Used Letters: \t', used_letters)
        print('Tries Left: ', 8 - misses )
        print(user_word)
        user_try = input('try: ').lower()

        if len(user_try) == 0:
            continue

        if not user_try.isalpha():
            print("You should type a letter")
            continue

        if user_try in used_letters:
            print("You have used this letter")
            continue

        if user_try in user_tries:
            print("You have tried this word")
            continue

        if len(user_try) == 1:

            if user_try not in target_word:
                misses += 1
                used_letters.append(user_try)
                continue

            for i, guess_letter in enumerate(target_word):
                if user_try == guess_letter:
                    user_word = user_word[:i] + user_try + user_word[i + 1:]

        if len(user_try) > 1:

            if user_try == target_word:
                print('You guessed right the word: ', target_word)
                print("Congratuations, You won!!!\n")
                return True

            misses += 1
            user_tries.append(user_try)

    print("Sorry you lost, the word was: ", target_word)
    return False

def category_validation(category):

    category_list = ['Animals', 'Movies', 'Food', 'Clothes', 'Plants', 'Famous Persons', '1', '2' , '3', '4', '5' , '6']

    if category.title() in category_list:
        return True

    print ('Not a valid category, please choose a valid one \n')
    return False

def difficulty_validation():

    difficulty_list = ['Easy', 'Medium', 'Hard', '1', '2', '3']

    while True:

        print('Choose the difficulty to play: \n1) Easy \n2) Medium \n3) Hard')
        difficulty = input('Difficulty: ')

        if difficulty in difficulty_list:
            return difficulty

        print("Please choose a valid difficulty level\n")

def generate_incognito(target_word):

    user_word = ''

    for i in target_word:

        if i.isalpha():
            user_word += '_'

        if i.isspace():
            user_word += ' '

    return user_word

def category_words(category, difficulty):

    if category == '1' or category.title() == 'Animals':

        words = ['Gorilla', 'Tiger', 'Lion', 'Bear', 'Rhino', 'Turtle', 'Hummingbird', 'Snake', 'Panther', 'Walrus', 'Platypus', 'Lynx', 'Swordfish', 'Axolotl', 'Orangutan']

        if difficulty == '1' or difficulty == 'Easy':
            words = filter( lambda word: len(word) <= 5, words)
            words = list(words)

        if difficulty == '2' or difficulty == 'Medium':
            words = filter( lambda word: len(word) > 5 and len(word) < 9, words)
            words = list(words)

        if difficulty == '3' or difficulty == 'Hard':
            words = filter( lambda word: len(word) >= 9, words)
            words = list(words)

        word = random.sample(words, 1)
        return word[0].lower()

    if category == '2' or category == 'Movies':
        words = ['Batman', 'Mulan', 'Matrix', 'Dune', 'Avatar', 'Harry Potter', 'The Godfather', 'Casablanca', 'Evil Dead', 'Die Hard', 'A Clockwork Orange', 'Black Hawk Down', 'Beauty And The Beast', 'Back To The Future', 'The Adventures Of Robin Hood']

        if difficulty == '1' or difficulty == 'Easy':
            words = filter( lambda word: len(word) <= 6, words)
            words = list(words)

        if difficulty == '2' or difficulty == 'Medium':
            words = filter( lambda word: len(word) > 6 and len(word) <= 12, words)
            words = list(words)

        if difficulty == '3' or difficulty == 'Hard':
            words = filter( lambda word: len(word) > 12, words)
            words = list(words)

        word = random.sample(words, 1)
        return word[0].lower()

    if category == '3' or category == 'Food':
        words = ['Donut', 'Orange', 'Bacon', 'Kale', 'Figs', 'Apple Pie', 'Carrot Cake', 'Ice Cream', 'Lasagna', 'Milkshake', 'Cauliflower', 'Garlic Bread', 'Cranberries', 'Gingerbread', 'Pork Tenderloin']

        if difficulty == '1' or difficulty == 'Easy':
            words = filter( lambda word: len(word) <= 6, words)
            words = list(words)

        if difficulty == '2' or difficulty == 'Medium':
            words = filter( lambda word: len(word) > 6 and len(word) < 11, words)
            words = list(words)

        if difficulty == '3' or difficulty == 'Hard':
            words = filter( lambda word: len(word) >= 11, words)
            words = list(words)

        word = random.sample(words, 1)
        return word[0].lower()

    if category == '4' or category == 'Clothes':
        words = ['Beret', 'Gloves', 'Scarf', 'Jeans', 'Skirt', 'Cardigan', 'Leggins', 'Overalls', 'Pajamas', 'Uniform', 'Swimming Trunks', 'Turtleneck Sweater', 'Business Suit', 'Bermuda Shorts', 'Baseball Jersey']

        if difficulty == '1' or difficulty == 'Easy':
            words = filter( lambda word: len(word) <= 6, words)
            words = list(words)

        if difficulty == '2' or difficulty == 'Medium':
            words = filter( lambda word: len(word) > 6 and len(word) < 9, words)
            words = list(words)

        if difficulty == '3' or difficulty == 'Hard':
            words = filter( lambda word: len(word) >= 9, words)
            words = list(words)

        word = random.sample(words, 1)
        return word[0].lower()

    if category == '5' or category == 'Plants':
        words = ['Roses', 'Cactus', 'Bamboo', 'Orchid', 'Fern', 'Lavender', 'Eucalyptus', 'Sunflower', 'Rain Lily', 'Palm Tree', 'Iceland Poppy', 'Rattlesnake Plant', 'Saucer Magnolia', 'Oak Mistletoe', 'Flamingo Willow']

        if difficulty == '1' or difficulty == 'Easy':
            words = filter( lambda word: len(word) <= 6, words)
            words = list(words)

        if difficulty == '2' or difficulty == 'Medium':
            words = filter( lambda word: len(word) > 6 and len(word) < 10, words)
            words = list(words)

        if difficulty == '3' or difficulty == 'Hard':
            words = filter( lambda word: len(word) >= 10, words)
            words = list(words)
        word = random.sample(words, 1)
        return word[0].lower()

    if category == '6' or category == 'Famous Persons':
        words = ['Marilyn Monroe', 'Abraham Lincoln', 'Nelson Mandela', 'Martin Luther King', 'Winston Churchill', 'Bill Gates', 'Elvis Presley', 'Albert Einstein', 'Leonardo da Vinci', 'Walt Disney', 'Henry Ford', 'Madonna', 'Michael Jackson', 'Michael Jordan', 'Steve Jobs']
        word = random.sample(words, 1)
        return word[0].lower()

class Game_Stats:

    def __init__(self):
        self._games_won = 0
        self._words_won = []
        self._games_lost = 0
        self._words_lost = []

    def add_stat(self, game_status, word):

        if game_status:
            self._games_won += 1
            self._words_won.append(word)

        if not game_status:
            self._games_lost += 1
            self._words_lost.append(word)

    @property
    def games_won(self):
        return self._games_won

    @property
    def words_won(self):
        return self._words_won

    @property
    def words_lost(self):
        return self._games_lost

    @property
    def games_won(self):
        return self._words_lost

if __name__ == "__main__":
    main()