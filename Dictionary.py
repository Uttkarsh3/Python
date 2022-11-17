d1 = {5: "Number",
      "a": "String",
      (1, 2): "Tuple"}

# Traversing a dictionary
for key in d1:
    print(key, ":", d1[key])

# Adding elements to dictionary
print("\n\nAfter adding elements to dictionary")
d1[1, ] = "tuple"
for key in d1:
    print(key, ":", d1[key])

# Deleting element in dictionary
print("\n\nAfter deleting element in dictionary")
del d1[1,]
d1.pop("a")
for key in d1:
    print(key, ":", d1[key])