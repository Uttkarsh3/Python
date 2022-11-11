n1=int(input("Enter the number: "))
n2=int(input("Enter the number: "))
res=max(n1,n2)
print (res)
while (True):
    if ((n1%res==0) and (n2%res==0)):
        LCM = res
        break
    res=res+1
return LCM
print(LcM)
