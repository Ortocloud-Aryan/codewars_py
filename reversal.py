num = input("Number? :")
string = ""
for i in range(-1, -len(num)-1, -1):
    string += num[i]
print(string)  
