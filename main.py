def op_check(user_name,user_money,operation):
    try:
        if operation == 1:
            attracting = input('How much money are you interested in attracting?')
            user_money -= int(attracting)
            return (user_money)
        elif operation == 2:
            return (user_money)
        elif operation == 3:
            depositing = input('How much money are you interested in depositing?')
            user_money += int(depositing)
            return (user_money)
        elif operation == 4:
            print(user_name)
    except: print('Operation failed')


user_name_m=input('please insart your name>')
user_money_m=int(input('please insart your money amount>'))
operation_m=int(input('What action would you like to take? \n 1 for withdrawing money \n 2 for balance checking \n 3 Money deposit \n 4 Account holder name \n 5 exit \n >>'))

while operation_m!=5:
    user_money_m=op_check(user_name_m, user_money_m, operation_m)
    print(user_money_m)
    operation_m = int(input('What action would you like to take? \n 1 for withdrawing money \n 2 for balance checking \n 3 Money deposit \n 4 Account holder name \n 5 exit \n >>'))

else:print('goodbay')