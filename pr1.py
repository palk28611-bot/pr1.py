
print("**********************************************************")
print("Welcome to the interactive personal data collector!!!!!!")
print("**********************************************************")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
fav_number = int(input("Enter your favourite number: "))

birth_year = 2026 - age

print("Name:", name)
print("Type:", type(name))
print("Memory address:", id(name))

print("Age:", age)
print("Type:", type(age))
print("Memory address:", id(age))

print("Height:", height)
print("Type:", type(height))
print("Memory address:", id(height))

print("Favourite number:", fav_number)
print("Type:", type(fav_number))
print("Memory address:", id(fav_number))

print("Birth year:", birth_year)
print("*************************************************************")
print("Thank you for using this program!!")
print("*************************************************************")
