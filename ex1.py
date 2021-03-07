print('insrt num1')
num=int(input())
print('insrt num2')
num2=int(input())
print('select 1="+" 2="-" 3="*" 4="/"')
s=int(input())

if s==1:
           print(num + num2)
elif s==2:
           print(num-num2)
elif s==3:
           print(num*num2)
elif s==4:
           print(num/num2)
