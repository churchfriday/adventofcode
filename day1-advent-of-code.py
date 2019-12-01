fuel = 0
flag = "true"
#input_mass = int(input())
mass = 0
sumofallmodules = 0
currentmodule = 0
sum_of_fuel_current = 0
#komentar ahahha

filepath = 'numbers.txt'
try:  
    with open(filepath) as fp:
        line = fp.readline()
        while line.isdigit:
            line = fp.readline()      
            line1 = int(line)
            fuel_current=int(line1/3)-int(2)
            #fuel+=fuel_current
            print ("fuel current: {}".format(fuel_current))

            while(int(fuel_current/3)>0):
                #fuel_current=int(fuel_current/3)-int(2)
                sum_of_fuel_current+=fuel_current
                fuel_current=int(fuel_current/3)-int(2)
                print ("fuel current: {}".format(fuel_current))
            if((int(fuel_current/3)-2<0)and(fuel_current > 0)):
                sum_of_fuel_current+=fuel_current
                continue
except:
    print("overall fuel {}".format(sum_of_fuel_current))
finally:
    fp.close()
