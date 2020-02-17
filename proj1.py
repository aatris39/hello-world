

print("Hello and welcome to the easiest math quiz ever! YAY!!!")

answer1 = input("Okay, first question is 1+0!")

if answer1 == ("1"):
    print("correct! good job :')")
    q1p = 5
else: 
    print("just drop out at this point :'(")
    q1p = 0

answer2 = input("Alrighty next quesion is 2+2!")

if answer2 == ("4"):
    print("woohoo!! you're right")
    q2p = 5
else:
    print("NOPE!")
    q2p = 0

score = q1p + q2p 
print("Your final score is " + score)
