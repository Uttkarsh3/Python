n1=int(input("Enter the number: "))
n2=int(input("Enter the number: "))
res=min(n1,n2)
print (res)
while res>0:
    if (n1%res==0 and n2%res==0):
        break
    res=res-1
print(res)
