def max(a,b,c):
    if(a>=b)and(a>=c):
        lsrgest=a
    elif(b>=a)and(b>=c):
        largest=b
    else:
        largest=c
    return largest
print(max(1,3,6))