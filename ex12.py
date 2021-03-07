card_str=str(input())
n=int(len(card_str))

for i in range(n):
           print(i,n-(i+1))
           print(card_str[i],card_str[n-(i+1)])
           if card_str[i] == card_str[n-(i+1)]:
                      print('trow');

           else:print ('false');           

