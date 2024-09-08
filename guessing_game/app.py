# importing necessary libraries
import math  # for the log calculation in the further code
import numpy as np  # for generating the random number

if __name__ == '__main__':
    # General Welcome statement and input for range by the user. Handled using Exception handled for datatype cases
    print('Welcome! This is the new Guessing game. Lets see how strong your intuition is.')
    print('Choose the range (lower bound and upper bound respectively). Both should be integers separated by a space :  ')
    while True:
        try:
            l, u = map(int, input().split(' '))
        except:
            print('Seems like one of them is not an integer. Please retry entering an integer again!')
            continue
        else:
            break
    # Calculating the number of chances
    chances = int(math.log2(u-l+1))

    # Generating the random number
    r = np.random.randint(l, u)
    print(f'I have generated the number for you to guess. You have {chances} chances to guess the number. ')

    # Initializing the count value to check the number of turns completed and flag value if the user has chosen the right guess number.
    c = 0
    f = 0

    # The actual game
    while c <= chances:
        while True:
            try:
                n = int(input("Whats your guess :"))
            except:
                print('Enter an integer number...')
                continue
            else:
                break
        if n == r:
            if c < chances:
                print('Congratulations! you have guessed it right ,in less than the expected number of chances.')
                f=1
                break
            else:
                print('Congratulations! You have guessed the number right.')
        elif n < r:
            print('Your number is low !!')
        elif n > r:
            print('Your number is high !!')

        c += 1
        if c == chances:
            print('Last chance Buddy !!')

    # Conclusion statement from the flag value
    if f != 1:
        print('Sorry! Better run the program and try again.')
    else:
        print('Game Over! Run the program again to play again.')


