# Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
def mul(number):
    m=1
    for i in number:
        m*=i
    return m
print(mul((8,2,3,-1,7)))