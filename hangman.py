import random

if __name__ == '__main__':

    #words = input("Enter 10 words for the Hangman game with spaces in between each word !!")
    words = 'apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'
    word_list = words.split(' ')
    print(word_list)

    word = random.choice(word_list)
    print("The computer has selected a random fruit ! Guess the letters of the fruit.")
    #print(word)

    chances = len(word)+2
    print(f"You have {chances} chances to guess the word.")

    blank = '_' * len(word)
    print(blank)

    letterguessed = ''
    i = 0
    while i <= chances:
        print()
        letter = str(input("Enter a letter and see if its correct or not : ")).lower()
        if letter.isalpha() == True and len(letter) == 1:
            if letter in word:
                letter_count = word.count(letter)
                for _ in range(letter_count):
                    letterguessed += letter

                temp = ''
                for char in word:
                    if char in letterguessed:
                        temp += char
                        print(char, end='')
                    else:
                        temp += '_'
                        print('_', end='')

                if len(letterguessed) == len(word):
                    print()
                    print("Congratulations you have guessed the word !!!")
                    break

            else:
                if letterguessed == '':
                    print(blank)
                else:
                    print(temp, end='')

            i += 1

        else:
            i -= 1
            if len(letter) > 1:
                print("Retry again entering a single letter and not a word. ")
            else:
                print("Retry again with an alphabet and not any other data types. ")

    print('Game Over !')








        
