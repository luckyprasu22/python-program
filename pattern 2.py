num=int(input("enter value"))
row=0
while row<num:
    space=num_row_1
    while space>0:
        print(end="")
        space=space_1
    star=row + 1
    while star>0:
        print("*",end="")
        star-=1
    row+=1
    print("\n")
