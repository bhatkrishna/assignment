# 36. Write a Python program to sum all the items in a dictionary.
def sum_(dic1):
    s=0
    for i in dic1:
        s+=dic1[i]
    return s
print("The sum of dictionary is:",sum_({2:5,4:5,5:8,6:8}))