P = int(input("please enter value for P:"))
Q = int(input("please enter value for Q:"))
#To swap the value of two variables using XOR
P = P^Q
Q = P^Q
P = P^Q
print("The value of P ater swaping: ",P)
print("The value of Q after swapping: ",Q)
