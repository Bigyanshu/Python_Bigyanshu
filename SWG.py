import random
'''
Snake = 1    Water = -1   Gun = 0
'''
computer = random.choice([-1,0,1])
user = input('Enter Your Choice... : ')
youDict = {'s':1, 'w':-1, 'g':0}
reverseDict = {1:'Snake', -1:'Water', 0:'Gun',}
you = youDict[user]

print(f"You Chose: {reverseDict[you]}\nComputer Chose: {reverseDict[computer]}")

if computer == you:
    print("It's Draw...!")
else:
    if (computer == 1 and you == -1):
        print("You Won!")
    elif (computer == 1 and you == 0):
        print("You Won")
    elif (computer == -1 and you == 1):
        print("You Won!")
    elif (computer == -1 and you == 0):
        print("Computer Won!\nYou Lost!")
    elif (computer == 0 and you == 1):
        print("Computer Won!\nYou Lost!")
    elif (computer == 0 and you == -1):
        print("You Won!")
    else:
        print("Something Went Wrong...!")
