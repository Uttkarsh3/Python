n=int(input("Enter the number: "))
fact=1
res=0
for i in range(2,n+1):
    fact=fact*i
    i=i+1
print("Factorial is: ")
print(fact)
while (fact%10==0):
    res=res+1
    fact=fact/10
print(res)







