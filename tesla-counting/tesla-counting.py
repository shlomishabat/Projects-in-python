
def tax_electric(price):
    tax1=(price*1.45)*1.17
    tax2=(tax1-price)*0.90
    return (tax2+price)

def tax(price):
    return (price*1.45)*1.17

def companycar(price):
    return price*0.0248

car_price=int(input('please insart the price of tesla car>'))
electric_car=int(input('Is this vehicle electric?'))
Mobilai=int(input('There is a Mobilai system?'))
Company_car=int(input('There is a Company car?'))

if electric_car==2 and Mobilai==2:
    print(tax(car_price))
    if Company_car==1:
        print(companycar(tax(car_price)))

elif electric_car==1 and Mobilai==1:
    print(tax_electric(car_price)-4000)
    if Company_car==1:
        print(companycar(tax_electric(car_price)-4000))

elif electric_car==2 and Mobilai==1:
    print(tax(car_price)-4000)
    if Company_car==1:
        print(companycar(tax(car_price)-4000))

elif electric_car==1 and Mobilai==2:
    print(tax_electric(car_price))
    if Company_car==1:
        print(companycar(tax_electric(car_price)))


