#I first defined the factorial function using recursive
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#I then made an input function
num = int(input("Enter a number: "))
#Display the factorial output
print(factorial(num))