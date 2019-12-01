fuel = 0
flag = "true"
input_mass = int(input())
mass = 0
while input_mass != 0:

    fuel+=(int(((input_mass/3)-2)))
    print(fuel)
    input_mass = int(input())
print(fuel)