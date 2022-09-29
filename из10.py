N10=int(input("N10="))
p=int(input("p="))
k=int(1)
Np=int(0)
while not N10==0:
    Np=Np+(N10%p)*k
    k=k*10
    N10=N10//p
print(f"Np={Np}")
