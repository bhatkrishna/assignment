# 8. Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def u_list(l):
    lst=[]
    for i in l:
        if i not in lst:
            lst.append(i)
    return lst
print( u_list([1,2,3,3,3,3,4,5])) 