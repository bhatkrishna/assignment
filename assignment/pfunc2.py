# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
def sum (numbers):
    s=0
    for i in numbers:
        s+=i
    return s
print(sum((8,2,3,0,7)))
