x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)
print("\n----------------\n")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
print("\n----------------\n")

x = set(["apple", "banana", "cherry"])
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)
