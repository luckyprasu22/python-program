#program for calculating electricity bill in python
units = int(input("please enter the number of units you consumed in a unit"))
PayAmount = 0
if (units<=200):
    PayAmount = units*3.0
elif(units<=250):
    PayAmount = (600)+(units-200)*4.5
elif(units<=300):
    PayAmount = (600)+(250-200)*4.5+(units-250)*5.2
elif(units<400):
    PayAmount = (600)+(250-200)*4.5+(300-250)*5.2+(units-300)*6.5
else:
    PayAmount = (600)+(250-200)*4.5+(300-250)*5.2+(400-300)*6.5+(units-400)*7.0
Total = PayAmount
print("Electricity bill = %f",Total)
                
