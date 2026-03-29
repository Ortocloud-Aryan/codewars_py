def math(a,b,c,d,f,g):
    a, b, c, d, f, g = a+b, a-b, c-d, f/d, g**2, a+b+d+c+g+f
    return a,b,c,d,f,g

outcome = math(1,2,3,4,56,5) # tuple
variable = ["a","b","c","d","f","g"]

for i in range(6):
    print(f"{variable[i]} = {outcome[i]}")