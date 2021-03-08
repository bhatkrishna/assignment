# 17. Write a Python program to multiplies all the items in a list.
def mul_list(myList_):
    result = 1
    for x in myList_:
         result = result * x 
    return result 
list_1=[1,2,3]
print(mul_list(list_1))