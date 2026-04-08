num = int(input("N value? : "))
even_sum = odd_sum = 0 
n = 1 
while n <= num:
    if n % 2 == 0:
        even_sum += n
    else:
        odd_sum += n
    n += 1

print(f"""The Sum of the First N even natural numbers : {even_sum} | The Sum of the First N Odd natural numbers  : {odd_sum}""")
