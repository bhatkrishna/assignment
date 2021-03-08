# 19. Write a Python program to get the smallest number from a list.
def s_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(s_list([1, 2, 3, 0]))