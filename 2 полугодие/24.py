with open('24.txt') as f:
    a=f.readline().replace('C','S').replace('D','S').replace ('F','S')
    a=a.replace('A','G').replace('O','G')
    a=a.replace('SG','*')
    k=kmax=0
    for i in a:
        if i=='*':
            k+=1
            kmax=max(kmax,k)
        else: k=0
    print(kmax)
