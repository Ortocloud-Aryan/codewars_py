# Only used if-elif-else statement.

x = int(input("Number 1: "))
y = int(input("Number 2: "))
z = int(input("Number 3: "))

l_num, m_num, s_num = None, None, None 

# for x is the largest number
if x>y and x>z:
    l_num = x
    if y>z:
        m_num = y
        s_num = z
    else:
        m_num = z
        s_num = y

# for y is the largest number
elif y>x and y>z:
    l_num = y
    if x>z:
        m_num = x
        s_num = z
    else:
        m_num = z
        s_num = x

# for z is the largest number
else:
    l_num = z
    if x>y:
        m_num = x
        s_num = y
    else:
        m_num = y
        s_num = x


print(s_num, m_num, l_num)
