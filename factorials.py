# Author: Nguyen L.
# Date:   April 25th, 2020 
# Finding factorial of a number input by the user

# formula: n! = n * (n-1)
# Example: 10! = 10 * 9 * 8 * 7 * ....

# define a function to find factorial
def findFactorial(num):

    # declare variable to hold values
    my_factorial = 1

    # going through a for loop until reaching num
    for i in range(my_factorial, num+1):
        my_factorial = my_factorial * i

    return my_factorial

print("Input a number: ", end='')
number = int(input())
my_factorial = findFactorial(number)
print("My factorial is: " + str(my_factorial))

