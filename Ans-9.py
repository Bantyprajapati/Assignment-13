# Write a Python script to create a list of city names taken from the user.
num_cities = int(input("Enter the number of cities: "))
city_list = []

for i in range(num_cities):
    city = input(f"Enter city name {i+1}: ")
    city_list.append(city)

print("City list:", city_list)
