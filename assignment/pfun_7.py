# 7. Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
def up_low(string_):
    upper_=0
    lower_=0
    for i in string_:
        if i.isupper():
            upper_+=1
        elif i.islower():
            lower_+=1
        else:
            pass
        return(upper_,lower_)
       
print(up_low("How do we gain  a  basic idea about Python programming"))

  
