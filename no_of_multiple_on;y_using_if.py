num = int(input("Enter the Number: "))
num1 = int(input("Enter the Number 1: "))
num2 = int(input("Enter the Number 2: "))
num3 = int(input("Enter the Number 3: "))
num4 = int(input("Enter the Number 4: "))
num5 = int(input("Enter the Number 5: "))

count = 0

if num1 % num == 0:
    count += 1
if num2 % num == 0:
    count += 1 
if num3 % num == 0:
    count += 1 
if num4 % num == 0:
    count += 1 
if num5 % num == 0:
    count += 1 

print(f"no of multiples : {count}")
