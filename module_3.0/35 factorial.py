# Write a Python function to calculate the factorial of a number


def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

n = int(input("enter a number : "))

print(factorial(n))