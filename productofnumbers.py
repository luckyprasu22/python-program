num = int(input("enter a number"))
n = num
product = 1
while n!=0:
    tem = n%10
    product = product*tem
    n = n//10
    print("product is %d",product)
