list1 = ['d', 'e', 'f']
list2 = ['g', 'h', 'i']
list3 = ['a', 'b', 'c']

print("List1 = ", list1)
print("List2 = ", list2)
print("List3 = ", list3)

list3.extend(list1)
list3.extend(list2)

print("After adding two lists on list 3 , list becomes: ")
print(list3)

list1.append(list2)
list1.insert(0, list3)


print("After adding two lists on list 1 , list becomes: ")
print(list1)



