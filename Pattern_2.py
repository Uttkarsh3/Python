n=int(input("Enter the number of rows:"))
number=30
for i in range(n+1,0,-1):
    for j in range(0,i-1):
        print(number,end=" ")
        number-=2
    print("\n")
