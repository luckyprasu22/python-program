#Take input from the user
num = int(input("Enter a number: "))
#intialize sum
sum = 0
#find the sum of the cube of each of each digit
temp = num
while temp>0:
    sum += num**3
    temp//=10
#display the result
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
