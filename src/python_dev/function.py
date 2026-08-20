def greeting(name, age=28, color="red"):
    print(
        f'Hello {name.capitalize()}, you will be {age+1} years old next birthday!')
    print(f"We hear you like the color {color.lower()}!")


name = input('Enter your name: ')
age = input('Enter your age: ')
color = input("enter your favourite color: ")
greeting(name, int(age), color)
