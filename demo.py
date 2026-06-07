


file = open("sample.txt", "w")

file.write("Hello Python")
file = open("sample.txt", "r")
file.close()

file = open("sample.txt", "r")
print(file.read())
file.close()


file = open("sample.txt", "a")
file.write("\nWelcome")
file.close()


with open("student.txt", "w") as file:
    file.write("Name : Vignesh")
    file.write("\nDepartment : ECE")

with open("student.txt", "r") as file:
    print(file.read())


file = open("sample.txt", "r")

print(file.readlines())

file.close()

file = open("sample.txt", "r")

print(file.readline())

file.close()