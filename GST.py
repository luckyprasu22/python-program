#prepare net amount payable by customer
amount = int(input("Enter the cost of SSD:"))
n = int(input("Enter the no.of SSD devices:"))
N = float(input("Enter the discount percentage: "))
discountamount = (amount*N/100)
m = int(input("Enter the GST percentage: "))
GST = amount*(m/100)
finalamounttopay = amount-discountamount+GST
print("the final amount is %d", finalamounttopay)
