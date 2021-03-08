# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"
def reverse_(string_):
    estring_=""
    index=len(string_)
    while index>0:
        estring_+=string_[index-1]
        index-=1
    return estring_
print(reverse_('1234abcd'))

   

   