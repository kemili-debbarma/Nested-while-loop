i=0
while i<5:
    c=0
    while c<5:
        if i+c==2 or c-i==2 or i-c==2 or i+c==6 or i-c==2 or i==2 or c==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        c=c+1
    print()
    i=i+1