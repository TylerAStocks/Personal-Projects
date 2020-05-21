#Takes a number and an exponent and tells you if it comports with the yeet theorem

import math

BASE_MIN = 1
EXP_MIN = 1
BASE_CAP = 100
EXP_CAP = 100

option = False 
base = 0
exp = 0

def listYeet():
    yeetList = ""
    for x in range(BASE_MIN, BASE_CAP):
        for y in range(EXP_MIN, EXP_CAP):
            base = x
            exp = y

            yeet = float(str(exp) + str(base))
            actual = float(math.pow(base, exp))

            if yeet == actual:
                yeetList += str(base) + ',' + str(exp) + '\n'
    print(yeetList)



def testYeet():

    try:
        base = int(input('base: '))
    except:
        print ("Invalid input. It's 0 now")
        base = 0

    try:
        exp = int(input('exponent: '))
    except:
        print ("Invalid input. It's 0 now")
        exp = 0

    yeet = float(str(exp) + str(base))
    print('yeet theorem result: ' + str(yeet))
    actual = float(math.pow(base, exp))
    print('actual result: ' + str(actual))

    if yeet == actual:
        print("These values comport with the yeet theorem")
    else:
        print("You picked incorrect numbers")



while option == False:
    choice = 0
    print("Enter 1 for a list of Yeet legal values")
    choice = input("Enter 2 to input your own: ")

    if choice == '1':
        listYeet()
        option = True
    elif choice == '2':
        testYeet()
        option = True
    else:
        print('Invalid choice')







