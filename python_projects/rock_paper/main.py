import random

def play():
    user=input(" 'r' for rock 'p' for paper 's' for scissors")
    computer=random.choice(['r','p','s'])

    if(user==computer):
        return 'tie'

    if is_win(user,computer):
        return 'You Won'

    return 'you lost!'




def is_win(player,opponent):

    if(player=='r' and opponent=='s')\
        or(player=='s' and opponent=='p')\
        or(player=='p' and opponent=='r'):
        return True

a=5
while (a>0):
    print(play())
    a=a-1
