#Program to calculate if a year is a leap year

#Gregorian rules

#1 If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
#2 If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
#3 If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
#4 The year is a leap year (it has 366 days).
#5 The year is not a leap year (it has 365 days).

#Julian Rules
#1 If the year is evenly dicisible by 4, go to setp 2, Otherwise, go to step3.
#2 The year is a leap year.
#3 The year is not a leap year.

def isLeap():
    print("the year", userInput, "is a leap year")

def isNotLeap():
    print("the year", userInput, "is not a leap year")

def isLeapHuman():
    print("the year", userInput, "is a leap year beacuse of human error")


def sinceGregorian(input): #calculation according to the gregorian rules
    #if input%4==0:
    #if input%100==0:
    if input%4==0:
        if input%100==0:
            if input%400!=0:
                isNotLeap()
            elif input%400==0:
                isLeap()
        else:
            isLeap()
    else:
        isNotLeap()



def sinceJulian(input): #calculation according to the julian rules
    if input%4==0:
        isLeap()
    else:
        isNotLeap()

def humanError(input):
    #print("year of -1 or earlier")
    match input:
        #45 BC,42 BC,39 BC,36 BC,33 BC,30 BC,27 BC,24 BC,21 BC,18 BC,15 BC,12 BC,9 BC,8 AD,12 AD
        case -46:
            isNotLeap()
        case -45:
            isLeapHuman()
        case -42:
            isLeapHuman()
        case -39:
            isLeapHuman()
        case -36:
            isLeapHuman()
        case -33:
            isLeapHuman()
        case -30:
            isLeapHuman()
        case -27:
            isLeapHuman()
        case -24:
            isLeapHuman()
        case -21:
            isLeapHuman()
        case -18:
            isLeapHuman()
        case -15:
            isLeapHuman()
        case -12:
            isLeapHuman()
        case -9:
            isLeapHuman()
        case 8:
            isLeapHuman()
        case 12:
            isLeapHuman()
        case _:
            isNotLeap()


#start of main
x = 1
print("program to calculate if a given year since -45 bce is a leap year, only real numbers are accepted")
#userInput = input("please input year here: ")
while x == 1:
    try:
        userInput = int(input("please input year here: "))
        x = 0
    except ValueError:
        print("Input is not a number, please try again")
        x = 1


if userInput >= 1582:
    sinceGregorian(userInput)
elif userInput <= -47:
    print("years before 46 are not accepted")
elif userInput == 0:
    print("the year 0 didnt happen, we went from -1 to +1")
elif userInput <= 12:
    humanError(userInput)
elif userInput >= 12:
    sinceJulian(userInput)

