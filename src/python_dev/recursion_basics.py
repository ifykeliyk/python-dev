# factorial
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)


def fibonacci(n):
    if n == 1:
        return 0

    if n == 2:
        return 1

    return (fibonacci(n-2)+fibonacci(n-1))


n = int(input("enter the value of n: "))
print(f"factorial of {n} is: {factorial(n)}")
print(f"fibonacci of {n} is: {fibonacci(n)}")
