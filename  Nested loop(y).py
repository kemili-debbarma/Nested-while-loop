
a=int(input("enter number"))
i=1
while i<=a:
    c=a
    while c>=i:
        print(" ",end="")
        c=c-1
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+2