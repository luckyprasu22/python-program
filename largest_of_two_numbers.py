#python program to find Largest of Two Numbers
a = float(input("Please Enter the First Value a: "))
b = float(input("Please Enter the Second Value b: "))
if (a>b):
    print("{0} is Greater than {1}".format(a,b))
    print("value of a",a)
    print("value of a%d"%a)
elif (b>a):
    print("{0} is Greater than {1}".format(b,a))
else:
    print("Both a and b are equal")
