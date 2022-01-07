import random

def guess(x):
    random_num=random.randint(1,x)
    guess=0

    while guess!=random_num:
        guess=int(input(f"guess a number between 1 and {x}:"))
        if guess<random_num:
          print("guess too low")
        elif guess>random_num:
          print("guess too high")

    print(f"yay you got got the number:{random_num} correctly!")


def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low

        feedback=input(f'Is {guess} tooo high(h),too low(l), or correct(c)')
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1

    print(f'computer guessed it correctly {guess}')



guess(10)
computer_guess(10)

