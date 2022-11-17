n=int(input("How many students? "))
comp_winners={}
for a in range(n):
    key=input("Enter the name of the student : ")
    value=int(input("Total competitions won : "))
    comp_winners[key]=value
print("The dictionary now is : ")
print(comp_winners)