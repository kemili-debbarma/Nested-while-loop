r=1
a=1
while r<=4:
    c=4
    while c<=4-a:
        print(" ",end=" ")
        c=c+1
    j=1
    while j<=r:
        if r-c==1 or r+c==1 or r-c==1:
            print("*",end=" ")
        else:
            print(" ",end="")
        j=j+1
    print( )
    a=a+1
    r=r+2
