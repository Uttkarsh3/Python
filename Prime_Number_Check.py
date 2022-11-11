# To check number is prime or not
n=int(input("Enter a number: "))
count= 0
i=2;
while i<=n/2:
    if n%i==0:
        count= count+1
        break
    i=i+1
if count== 0:
    print("Prime Number")
else:
    print("Not Prime Number")
