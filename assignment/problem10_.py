# 10. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
def same_list(list_):
    lst=[]

    for i in list_:
        if i%2==0:
            lst.append(i)
    return lst
print (same_list([1,2,3,4,5,6,7,8,9]))
