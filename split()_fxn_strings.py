def split(str, char):
    #i/p : split("ryan","a") ---> o/p : ['ry', 'n']
    #i/p : split("xysdfearyan", "a") ---> o/p : ['xysdfe', 'ry', 'n']
    #1 make an empty list : splitted_list in which the splitted string will be stored
    splitted_list = []
    #2 make an empty string : splitted_string through which we'll add that splitted_string inside the splitted_list
    splitted_string = ""
    #3 iterate string to check for char in string and store the only part in which the string doesnt have "a" (via splitted_string) inside the splitted_list and then reset the splitted_string for doing it for more block of string after this encounter.
    for i in str: 
        if i != char: # char = a 
            splitted_string += i
        else:
            if not splitted_string == "":
                splitted_list.append(splitted_string)
            splitted_string = ""
            
    if not splitted_string == "":
        splitted_list.append(splitted_string)
    #4 return splitted_list
    return splitted_list


def join_split_string(str, char):
    # join_split_string("aryansoni","a") -> rynsoni
    # join_split_string("aryansoni","s") -> aryanoni
    # step 1 : split the string with respect to the character(it'll be a list)
    split_string = split(str, char)#list
    # step 2: form the string(as in str datatype) from the list
    string_without_char = ""
    for i in split_string:
        string_without_char += i
    # step 3: return the respective string 
    return string_without_char
    
#ACTUAL I/P-> "ARYAN SONI" ::: O/P->"rynsoni"  
#1 : input -> string.lower() and char -> char.lower()
input_string = input("Enter desired string : ").lower()
input_char = input("Enter the desired character : ").lower()
#2 : call join_split_string(input_string, "a") from this we'll get  a_splitted_string
a_splitted_string = join_split_string(input_string, input_char)
#3 : now we'll take the a_splitted_string and call 'def join_split_string(a_splitted_string, " ")' --> from this we'll get the final string that we wanted! 
print(join_split_string(a_splitted_string, " "))


    
