from datetime import date ,datetime
str = input('input date 1 "DD-MM-YYYY">')
str2 =input('input date 2 "DD-MM-YYYY">')
d1 = datetime.strptime(str, '%d-%m-%Y')
d2 = datetime.strptime(str2, '%d-%m-%Y')

delta = d1 - d2

print(delta)