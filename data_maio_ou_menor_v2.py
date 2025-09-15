d1, m1, a1 = input('1ª data? ').split('/')
d1, m1, a1 = int(d1), int(m1), int(a1)
 
d2, m2, a2 = input('2ª data? ').split('/')
d2, m2, a2 = int(d2), int(m2), int(a2)
 
print('Ocorre primeiro: ', end='')
 
data1 = a1*10000 + m1*1000 + d1*1
data2 = a2*10000 + m2*1000 + d2*1


if data1 < data2:
    print(f"{d1}/{m1}/{a1}")
else:
    print(f"{d2}/{m2}/{a2}")
