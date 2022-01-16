cities = {"Dhaka", "KL", "Mumbai", "Johor"}

with open("cities.txt", 'w') as cities_file:
    for city in cities:
        print(city, file=cities_file)
