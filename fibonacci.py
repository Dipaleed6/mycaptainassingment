a=0
b=1
no=0
n=(eval(input("Enter n")))


if n==1:
    print(a)
    
    
elif n==2:
    print(a)
    print(b)
    
else:
    print(a)
    print(b)
    for i in range(3,n+1):
        
        no=a+b
        a=b
        b=no
        print(no," ")
