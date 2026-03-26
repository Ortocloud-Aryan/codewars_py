#Write a code which prints these stats : 
# 1. Number of upper case ltters 
# 2. no fo lower 
# 3. no of letters 
# 4. no of digits 
def stats(string):
    lowercase_no = uppercase_no = alpha_no = digit_no = 0
    for l in string:
        if l.isalpha():
            alpha_no += 1
            if l.islower():
                lowercase_no += 1
            else:
                uppercase_no += 1
        elif l.isdigit():
            digit_no += 1
    print(f"""No of alphabets : {alpha_no}
         No of Upper-Cased alphabets : {uppercase_no}
         No of Lower-Cased alphabets :{lowercase_no}
         No of Digits : {digit_no}""")

string = input("ENTER THE STRING :") #user input 

stats(string)

    