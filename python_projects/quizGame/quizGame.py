print("welcome to this quiz!")

playing=input("Do you want to play? ")
#print(playing)

if playing.lower() != "yes":
    quit()

print("Okay ! let's play ")
score=0

answer=input("what does CPU stand for?")
if answer.lower() == 'central processing unit':
    print("correct!")
    score+=1
else:
    print("ooops!wrong answer")

answer=input("what does RAM stand for?")
if answer.lower() == 'random access memory':
    print("correct!")
    score+=1
else:
    print("ooops!wrong answer")

answer=input("what does GPU stand for?")
if answer.lower() == 'graphics processing unit':
    print("correct!")
    score+=1
else:
    print("ooops!wrong answer")

answer=input("what does PSU stand for?")
if answer.lower() == 'power supply unit':
    print("correct!")
    score+=1
else:
    print("ooops!wrong answer")

#here the num score is converted to string as a number can't be addeed directly to a string
print("you got "+str(score)+" questions correct")
print("you got "+str((score/4)*100)+"%")
