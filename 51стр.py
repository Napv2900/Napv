X = int(1)
Y = int(1)
Z = int()
p = int(input("введите p (2<p<10) :"))
print(p,"-ичная таблица умножения")
for X in range(1,p):
    z=[]
    for Y in range(1,p):
        Z = (X * Y // p)*10 + (X * Y)%p
        z.append(Z)
    print(z)
        


