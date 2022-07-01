num=int(input("enter number"))
r=0
while r<=num:
    c=0
    while c<=r:
        print(c**2,end="")
        c=c+1
    print()
    r=r+1