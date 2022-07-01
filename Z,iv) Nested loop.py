r=0
while r<5:
    c=0
    while c<5:
        if r+c==2 or c-r==2 or r+c==6 or r-c==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        c=c+1
    print()
    r=r+1
        
