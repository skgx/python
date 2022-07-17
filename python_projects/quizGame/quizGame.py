print("welcome to this quiz!")

playing=input("Do you want to play? ")
#print(playing)

if playing != "yes":
    quit()

print("Okay ! let's play ")

answer=input("what does CPU stand for?")
if answer == 'central processing unit':
    print("correct!")
else:
    print("ooops!wrong answer")
