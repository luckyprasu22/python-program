#program for displaying character from given string
name = 'Jesaa'
size = len(name)
i = 0
#iterate loop till the last character
while 1<size:
#break loop if current character is number
    if name[i]:
        break
#print current character
        print(name[i], end = "")
        i = i+1
