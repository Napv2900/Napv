spisok=[]
for num in range(2,1000):
    if all(num%delit!=0 for delit in range(2,num)):
        spisok.append(num)
for y in range(100):
    if y*4+117 in spisok:
        print(y)
        break
