#program for calculating electricity bill in python
units = int(input("Please enter the number of units you consumed in a month"))
if(units<=100):
    PayAmount = units*1.5
    fixedcharge = 25.00
elif(units<=200):
    PayAmount = (100*1.5) + (units-100)*2.5
    fixedcharge = 50.00
elif(units<=300):
    PayAmount = (100*1.5) + (200-100)*2.5 + (units-200)*4
    fixedcharge = 75.00
elif(units<=350):
    PayAmount = (100*1.5) + (200-100)*2.5 + (300-200)*4+(units-300)*5
    fixedcharge = 100.00
else:
    PayAmount = 0
    fixedcharge = 1500.00
Total = PayAmount + fixedcharge;
print("\n Electricitybill = %f"%Total)
#print("The value of Total is ",Total)
