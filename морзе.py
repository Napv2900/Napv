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
