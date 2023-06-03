# Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using list
items = ["Java", "Python", "SQL", "C"]

# Accessing the items in the list
print("Items in the list:")
for item in items:
    print(item)

# Adding a new item to the list
items.append("JavaScript")

# Removing an item from the list
items.remove("SQL")

# Accessing a specific item in the list
print("Item at index 1:", items[1])

# Updating an item in the list
items[2] = "Ruby"

# Displaying the updated list
print("Updated list of items:")
for item in items:
    print(item)
