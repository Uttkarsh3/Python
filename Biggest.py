a,b,c,d = map(int,input("Enter four numbers: ").split())
big=a;
if b>big:
    big=b;
if c>big:
    big=c;
if d>big:
    big=d;
print("The biggest number is: ")
print(big)
