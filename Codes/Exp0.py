#functions: 
#1. (3/2)^n
#2. n^3
#3. log(n)
#4. e^n
#5. n
#6. n*2^n
#7. log(log(n))
#8. 2^log(n)
#9. log(n)^2
#10. 2^n

import math

def threeByTwo():
    for i in range(1, 101):
        print((1.5) ** i)

def cube():
    for i in range(1, 101):
        print(i ** 3)

def logarithm():
    for i in range(1, 101):
        print(math.log(i, 2))

def eRaisedTo():
    for i in range(1, 101):
        print(math.pow(math.e, i))

def linear():
    for i in range(1, 101):
        print(i)

def nIntoTwoRaisedTo():
    for i in range(1, 101):
        print(i * math.pow(2, i))

def logOfLog():
    for i in range(2, 101):
        print(math.log(math.log(i, 2), 2))

def twoRaisedToLog():
    for i in range(1, 101):
        print(math.pow(2, math.log(i, 2)))
    
def logSquare():
    for i in range(1, 101):
        print(math.pow(math.log(i, 2), 2))

def twoRaisedTo():
    for i in range(1, 101):
        print(math.pow(2, i))


print('For the function (3/2) ^ n- \n')
threeByTwo()
print('\nFor the function n ^ 3- \n')
cube()
print('\nFor the function lg(n)- \n')
logarithm()
print('\nFor the function e ^ n- \n')
eRaisedTo()
print('\nFor the function n- \n')
linear()
print('\nFor the function n * (2 ^ n)- \n')
nIntoTwoRaisedTo()
print('\nFor the function lg(lg(n))- \n')
logOfLog()
print('\nFor the function 2 ^ (lg(n))- \n')
twoRaisedToLog()
print('\nFor the function lg(n) ^ 2- \n')
logSquare()
print('\nFor the function 2 ^ n- ')
twoRaisedTo()