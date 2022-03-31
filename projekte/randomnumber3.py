from collections import Counter
import random

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
        if userInputMax > 78:
            print("input over 78 not supported due to terminal size")
            y=1
        else:
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

def populate2dArray(input):
    b = 0 #counter for while loop
    while b <= userInputNum:#while loop runs till userInputNum is matched
        counted = 0 #resets conted in the loop before its needed again
        counted = input.count(b) #counts the number of numbers of B
        _2dArray.append([b, counted]) #attempts to append both the current number (B) and the amount it shows up in the listOfNumbers to _2dArray
        b = b + 1 #increments the counter B to go to the next number

def populate3dArray():
    currentNum = 0 #the number currently getting worked on form the first column
    _3dPos = 0 #the current position in the row
    amountX = 0 #the amount of x's that need to get added
    while currentNum <= userInputMax: #loops till all numbers have been checked
        amountX = _2dArray[currentNum][1]#amount of times the number show up in listOfNumbers
        _3dPos = 0
        while _3dPos < amountX: #loops till there are no more x's to add
            _3dArray [currentNum] [_3dPos] = 1 #replaces the 0 in the empty _3dArray with 1 in the current colum and the current row
            _3dPos = _3dPos + 1 #increass postion of _3dPos
        currentNum = currentNum + 1

#def make3dArray():
#    lengthArray = [0]*bigg2
#    print(lengthArray)
#    d = 0
#    while d <= userInputMax:
#        _3dArray.append(lengthArray)
#        d = d+1

#print idea
#print lines in order
#make array with numbers till 

def convert3dArray():
    currentNum = 0 #the number currently getting worked on form the first column
    _3dPos = 0 #the current position in the row
    while currentNum < userInputMax+1: #loops till all numbers have been checked
        _3dPos = 0
        while _3dPos < bigg2: #loops till there are no more x's to add
            #_3dArray [currentNum] [_3dPos] = 1 #replaces the 0 in the empty _3dArray with 1 in the current colum and the current row
            if _3dArray[currentNum][_3dPos] == 1:
                _3dArray[currentNum] [_3dPos] = " X"
            elif _3dArray[currentNum][_3dPos] == 0:
                _3dArray[currentNum][_3dPos] = "  "
            _3dPos = _3dPos + 1 #increass postion of _3dPos
        currentNum = currentNum + 1

def output():
    print
    posCol = 0
    posRow = 0
    while posRow < bigg2:
        while posCol <= userInputMax:
            print(rotated[posRow][posCol],"|", end='', sep='')
            posCol = posCol+1
        print()
        posRow = posRow+1
        posCol = 0
    n = 0
    while n <= userInputMax:
        if n < 10:
            print("0",n,"|", end = '', sep='')
            n = n + 1
        else:
            print(n,"|", end = '', sep='')
            n = n + 1

biggestNumber = 0
populate2dArray(listOfNumbers)
c = Counter(listOfNumbers)
biggestAmount = c.most_common(1)
bigg2 = int(biggestAmount[0][1])
_3dArray = []
_3dArray = [[0]*bigg2 for _ in range(userInputMax+1)] #https://stackoverflow.com/questions/4230000/creating-a-2d-matrix-in-python
populate3dArray()
convert3dArray()
rotated = list(reversed(list(zip(*_3dArray)))) #https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
print()
output()
print()