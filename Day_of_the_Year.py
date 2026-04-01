day = int(input("enter the day : "))
month = int(input("enter the Month : "))
year_no = 1 #current year
day_of_the_year = (month-1)*30 + day
if day_of_the_year > 360:
    year_no = day_of_the_year // 360 
    day_of_the_year = day_of_the_year % 360

print(f"{day_of_the_year}th day of the {year_no} number Year")
