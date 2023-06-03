# Write a python script to get the data type of a list.
def get_list_data_type(lst):
    data_type = type(lst).__name__
    return data_type


# Test the function
my_list = [1, 2, 3, 4, 5]
data_type = get_list_data_type(my_list)
print("Data type of the list:", data_type)
