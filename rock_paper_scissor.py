import numpy as np

class Rock_Paper_Scissor:

    def computer(self, choice):
        arr = np.array(['rock', 'paper', 'scissor'], dtype=str)
        return np.random.choice(arr[arr != choice])


if __name__ == '__main__':
    print("This is the Rock Paper Scissor Game.")
    rps = Rock_Paper_Scissor()
    cs = 0
    us = 0
    print('There will be 3 rounds!!')
    for _ in range(3):
        while True:
            user = input('Enter your choice :').strip().lower()
            if user in ['rock', 'paper', 'scissor']:
                break
            else:
                print("Didn't enter rock , paper, scissor. Enter any one of them!")
                continue

        comp = rps.computer(user)
        print("My choice :", comp)

        display_user = 'User won'
        display_comp = 'I won'
        if user == 'rock' and comp == 'paper':
            us += 1
            print(display_user)
        elif user == 'paper' and comp == 'rock':
            cs += 1
            print(display_comp)
        elif user == 'scissor' and comp == 'paper':
            us += 1
            print(display_user)
        elif user == 'paper' and comp == 'scissor':
            cs += 1
            print(display_comp)
        elif user == 'rock' and comp == 'scissor':
            us += 1
            print(display_user)
        elif user == 'scissor' and comp == 'rock':
            cs += 1
            print(display_comp)
    else:
        if us > cs:
            print('User won the game')
        elif us < cs:
            print('Computer won the game')
        else:
            print("Its a Tie")


