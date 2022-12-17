def fx():
    p = int(input("введите основание системы, p = "))
    Np = int(input(f"Исходное число N{p} = "))
    k = int(1)
    N10 = int(0)
    while not Np==0:
        N10 = N10 + (Np % 10) * k
        k = k * p
        Np = Np // 10
    print("N10 = ", N10)
 def fy():
     N10=int(input("N10="))
     p=int(input("p="))
     k=int(1)
     Np=int(0)
     while not N10==0:
         Np=Np+(N10%p)*k
         k=k*10
         N10=N10//p
    print(f"Np={Np}")
def fz():
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
def fs():
    a="абвгдежзийк"
    x=""
    alf=list(a)
    print(alf)
    mors=".- -... .-- --. -.. . ...- --.. .. .--- -.-"
    alfm=mors.split()
    print (alfm)
    morze=input("текст: ")
    for i in morze:
        x=x+' '+alfm[alf.index(i)]
    print(x)
def fd():
        a='0123456789'
        nums=list(a)
        print(nums)
        b='0000000 0001111 0010110 0011001 000101 0101010 0110011 0111100 1000011 1001100'
        hem=b.split()
        print(hem)
        for i in range(len(hem)):
            hem[i]=int(hem[i])
        print(hem)
        def distance(x,y):
            k=7
            for i in range(7):
                if x%10==y%10:
                    k=k-1
                x=x//10
                y=y//10
            return k
        cod=int(input("код"))
        min=distance(cod,hem[0])
        imin=0
        for i in range(10):
            D=distance(cod,hem[i])
            if D<min:
                min=D
                imin=i
        if min==0:
            print(f"код верный: символ {nums[imin]}")
        elif min==1:
            print(f"код исправлен: символ {nums[imin]}")
        else:print("Код неверный")
def f():
    a=int(input())
    if a==1:
        fx()
    elif a==2:
        fy()
    elif a==3:
        fz()
    elif a==4:
        fs()
    elif a==5:
        fd()
f()
    
    
    
