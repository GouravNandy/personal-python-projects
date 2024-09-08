import math
import numpy as np

if __name__ == '__main__':
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
    chances = int(math.log2(u-l+1))
    r = np.random.randint(l, u)
    print(f'I have generated the number for you to guess. You have {chances} chances to guess the number. ')
    c = 0
    f = 0
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

    if f != 1:
        print('Sorry! Better run the program and try again.')
    else:
        print('Game Over! Run the program again to play again.')


