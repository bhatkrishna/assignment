# 9. Write a Python function that takes a number as a parameter and check the
# number is prime or not.
def prime_(num):
    if num >1:
        for i in range(2,num):
            if num%i==0:
                return "not prime number"
                
        else:
            return "prime number"

print(prime_(7))