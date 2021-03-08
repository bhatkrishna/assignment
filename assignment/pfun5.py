# 5. Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.
def factorial(a):
    if a==0:
        return 1
    else:
        return a*factorial(a-1)
n=int(input("input number:"))
print("the factorial isa:",factorial(n))
