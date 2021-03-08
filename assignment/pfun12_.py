# 12. Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number
def fund1(n):
    return lambda x:x*n
result=fund1(2)
print("the multiplication is",result(10))
