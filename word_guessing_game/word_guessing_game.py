"""
This program is a simple word-guessing game where the user has to guess the randomly selected word from a list of words
within a limited number of attempts. The program provides feedback after each guess,
helping the user to either complete the word or lose the game based on their guesses.

"""

import random

class guess_word:

    def __init__(self, word_list):
        self.word_list = word_list

    def play_game(self):
        name = input("Enter your name :")
        chosen_word = random.choice(self.word_list)
        print(f'Hey {name}! Welcome to the Word guessing game. Below is the list of words from which you will be guessing which word have I chosen. Lets start !')
        print(words)
        while True:
            try:
                turns = int(input("Enter the number of turns you require to play this game :"))
            except:
                print("Enter an integer number....")
                continue
            else:
                break


        flag = 0
        c = 0
        for i in range(turns):
            guess = input("Enter the word :")
            guess = guess.strip().lower()
            if guess == chosen_word:
                flag = 1
                c = i
                break
            else:
                print("Nope thats not the word. Try again !")
                continue
        else:
            if flag == 1:
                print(f"Thats the word. Congratulation you guessed it in {c + 1} turn(s)")
            else:
                print(f"Sorry! You werent able to guess the word. Better luck next time.")

        print('Do you want to play it again ? [Y/n]')
        return input()





if __name__ == '__main__':
    words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

    game_obj = guess_word(words)
    play_game = game_obj.play_game()
    while True:
        if play_game.strip().lower() in ['y', 'n']:
            if play_game.strip().lower() == 'y':
                play_game = game_obj.play_game()
                continue
            else:
                break
        else:
            print('Invalid Input. Enter only Y or n')
            play_game = input()









