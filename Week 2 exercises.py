#Week 2 Lab exercises

#Question 1

#1a
#A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

#A[1] [2]



#1b
#A[0][2:], A[1][2:], A[3][2:]



#1c
#list1 = [-9, -5, -1, 195, 199]
#list1


#1d
#dictionary1 = {"Key":"Value Pairs", "brand":"BMW", "Year": "2018", "colour":"red", "mileage": "30000", "fuel": "petrol"}



#Question 2

def TempConv():
    kelvin = int(input("Enter the temperature in kelvin: "))
    celsius = kelvin - 273.15
    print (celsius)

#TempConv()



#Question 3
import math

def sigmoid():
    x = 0.5
    ans = 1/(1+math.exp(1)**-x)
    print(ans)
    
#sigmoid()


#3b
def hsgn(x):
    if x > 0:
        print("1")
    elif x < 0:
        print("-1")
    else:
        print("0")
        
#hsgn(-6)



#Question 4
import random

def numGen():
    randNum = random.randint(1, 20)
    lives = 6
    while lives > 0:
        ans = int(input("Guess the number: "))
        if ans > randNum:
            print("Too High")
            lives = lives -1
        elif ans < randNum:
            print("Too Low")
            lives = lives -1
        else:
            print("You Win")
            break

#numGen()
