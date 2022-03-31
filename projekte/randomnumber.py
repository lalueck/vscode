import random

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
for x in range (0, userInputNum):
    listOfNumbers.append(random.randint(userInputMin, userInputMax))
print(listOfNumbers, "/n")
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
    print(rotated)



goodMethod(listOfNumbers)


#print goodMethod initial idea
while c <= userInputNum:
    position = userInputNum
#    value = position from _2dArray other side
#    if value == 0 
#       print("  ")
#   else  


# good method initial idea
#while a <= num
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
