# 37. Write a Python program to multiply all the items in a dictionary.
# def mul_(dic1):
#     mul=1
#     for i in dic1:
#         mul=mul*dic1[i]
#     return dic1
# print("The multiplication is:",mul_({'a':6,'p':7,'p':8,'l':9,'e':3}))
my_dict = {'d1':10,'d2':5,'d3':4}
res=1
for i in my_dict:    
    res=res * my_dict[i]

print(res)