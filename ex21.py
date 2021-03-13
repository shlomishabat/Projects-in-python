def list_a(list_i):
    list_r = []
    for i in list_i:

        if int(i) % 3 ==0:
            list_r.append(i)
    return (list_r)
list_1= input()

print(list_a(list_1))