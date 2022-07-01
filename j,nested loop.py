num=int(input("enter num"))
r=1
while r<=num:
    c=1
    while c<=num-r:
        print(" ",end="")
        c=c+1
    p=0
    while p<r:
        print(r-p,end="")
        p=p+1
    print()
    r=r+1
