num=int(input("enter number"))
r=1
while r<=num:
    c=1
    while c<=num-r:
        print(" ",end=" ")
        c=c+1
    j=0
    while j<r:
        print(r-j,end=" ")
        j=j+1
    k=2
    while k<=r:
        print(k,end=" ")
        k=k+1
    print()
    r=r+1