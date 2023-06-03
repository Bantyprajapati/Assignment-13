# Write a python program to append elements from another list to the current list.(firstlist = ["Java", "Python", "SQL"]t = ["C", "Cpp", "NoSQL"] )
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]

# Append elements from secondlist to firstlist
firstlist.extend(secondlist)

# Display the updated list
print("Updated list:", firstlist)
