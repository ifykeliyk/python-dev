with open("temperatures_c.txt", "w") as file:
    file.write("98.6\n")
    file.write("212.0\n")
    file.write("72.5\n")
    file.write("-40.0\n")

with open("temperatures_f.txt", "w") as file, open("temperatures_c.txt", "r") as c_file:
    for line in c_file:
        celsius = float(line.strip())
        fahrenheit = (celsius * 9/5) + 32
        file.write(f"{fahrenheit}F\n")

with open("temperatures_f.txt", "r") as file:
    temperatures = file.readlines()
    for temp in temperatures:
        print(temp.strip())
