list = [1,2,3,5]

print("Your current list is:", list)

list[0] = list[-1]
list[-1] = list[0]
print("New list is:", list)
