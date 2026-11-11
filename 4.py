n=int(input("enter an odd number of rows:"))
if n<=0 or n%2==0:
print("Invalid dimension! PLease enter a positive odd number.")
else:
    mid=n//2
    for i in range(mid+1):
        print(" "*(mid-i),end="")
        for j in range(1,i+2):
            print(j,end="")
        for j in range(i,0,-1):
            print(j,end="")
        print()
        for i in range(mid-1,-1,-1):
            print(" "*(mid-i),end="")
            for j in range(1,i+2):
                print(j,end="")
            for j in range(i,0,-1):
                print(j,end="")
            print()         
