import random
import numpy as np



#TODO implement warning when user would surpass 61 character limit, add 61 character limit override, do grpahics for _2dArray/turn 2d array into 3d array????
#NOTE 61 numbers are max display on the terminal when done horizontally

x = 1
y = 1
z = 1

#USER INPUT THAT DOESNT ALLOW TEXT
while x == 1:
    try:
        userInputMin = int(input("please input minimum here: "))
        x = 0
    except ValueError:
        print("Input is not a number, please try again")
        x = 1
while y == 1:
    try:
        userInputMax = int(input("please input maximum here: "))
        y = 0
    except ValueError:
        print("Input is not a number, please try again")
        y = 1
while z == 1:
    try:
        userInputNum = int(input("please input number of numbers here: "))
        z = 0
    except ValueError:
        print("Input is not a number, please try again")
        z = 1
        

listOfNumbers = []
for _ in range (userInputNum):
    rand = random.randint(userInputMin, userInputMax)
    listOfNumbers.append(rand)
print(listOfNumbers)
_2dArray = []
def badMethod(input):
#just prints it horizontally, apparently bad
    a = 0
    while a <= userInputNum:
        output = 0
        output = listOfNumbers.count(a)
        print(a,":", "x" * output)
        a = a + 1

#what curse have you brought upon me
def goodMethod(input):
    b = 0 #counter for while loop
    while b <= userInputNum:#while loop runs till userInputNum is matched
        counted = 0 #resets conted in the loop before its needed again
        counted = listOfNumbers.count(b) #counts the number of numbers of B
        _2dArray.append([b, counted]) #attempts to append both the current number (B) and the amount it shows up in the listOfNumbers to _2dArray
        b = b + 1 #increments the counter B to go to the next number
    print(_2dArray)
    rotated = list(zip(*_2dArray))[::-1]
   # print(rotated)
    
_3dArray = [[0]*max(_2dArray)]*userInputNum
#print(np.amax(_2dArray))
print(_3dArray) 
print(max(_2dArray))


goodMethod(listOfNumbers)



#thinking
# 1st, get maximum length
#then set that as maximum length for 3d list
#then check for value of 2d list
#fill 3d list with those values
#print those 

#currentNum = 0
#while currentNum <= len(listOfNumbers):
    #maximumHeight = np.amax(listOfNumbers)
    #amountX = _2dArray[currentNum[1]]
    #append 1 to 3d array amountX times, then add difference between in 0



#print goodMethod initial idea
#c = 0
#while c <= userInputNum:
#    position = userInputNum
#    value = position from _2dArray other side
#    if value == 0 
#       print("  ")
#   else  

# good method initial idea
#while a <= numS
# counted = 0
# append a
# append counted



# bad method initial idea
#userInputNum  
# while x <= num
#   output = 0
#   output.count x listOfNumbers
#   print output
#   x++
