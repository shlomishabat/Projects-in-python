def list5(list1):
           newlist=[]
           for i in range(len(list1)):
                          if list1[i] % 2 !=0:
                                     newlist.append(list1[i])

           return(newlist)
                                     
                                     



list_a=[121,212,313,444524,1255,654126]
print(list5(list_a))


