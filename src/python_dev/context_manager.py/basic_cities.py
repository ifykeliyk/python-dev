with open("cities.txt", "w") as file:
    file.write("Tokyo\n")
    file.write("Paris\n")
    file.write("New York\n")
    file.write("Sydney\n")

with open("cities.txt", "r") as file:
    cities = file.readlines()
    n = len(cities)
    for city in cities:
        print(city.strip())

    print(f"Number of cities: {n}")
