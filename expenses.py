expenses = [10.50, 8, 5, 15, 20, 5, 3]

sum = 0

for x in expenses: 
    sum = sum + x

print("You spent $", sum, "on lunch this week" sep="")


### another way

expenses = [10.50, 8, 5, 15, 20, 5, 3]
total = sum (expenses)

print("You spent $", total, "on lunch this week" sep="")


##looping expenses

total = 0
expenses = []
for i in range(7) #range in here is the number of times the function below will be looped 
    expenses.append(float(input("Enter an expense:"))) #in here, expenses.append means every number inputted by user will be added to the loop 

total = sum (expenses)

print("You spent $", total, sep="")


#looping expenses with a definite number 
total = 0
expenses = []
num_expenses = int (input("Enter number of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

    total = sum (expenses)

print("You spent $", total, sep="")