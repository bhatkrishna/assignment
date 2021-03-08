# 38. Write a Python program to remove a key from a dictionary.
my_dict={'name':'john','age':26,'job':'developer'}
print("Dictionary item is:",my_dict)
key= input("enter key which want to you delete:")
if key in my_dict:
    del my_dict[key]
else:
    print("Given key is not present in dictionary ")
print('\nupdate dictionary:',my_dict)