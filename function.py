def greeting(name):
    print('HEllo', name)


#Main program
input_name = input("Enter your name:\n")
greeting(input_name)
print('Thanks', name)


#another way to do this
def greeting()
    print('Hello', name)

name = input ('Enter your name:\n')
    greeting()


#Local scope
def greeting(name):
    print('HEllo', name)

name1 = input('Enter your name:\n')
greeting(name1)
name2 = input('Enter another name:\n')
greeting(name2)


#################

#SIMPLE FUNCTION THAT ADDS TWO NUMBERS AND RETURNS RESULT 
#creating the addition function
def addition (a, b):
    return a + b

#Main program
num1 = float(input('Enter your 1st number:\n'))
num2 = float(input('Enter your 2nd number:\n'))

result = addition(num1, num2)
print("The result is", result )