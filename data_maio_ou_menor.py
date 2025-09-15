d1, m1, a1 = input('1ª data? ').split('/')
d1, m1, a1 = int(d1), int(m1), int(a1)
 
d2, m2, a2 = input('2ª data? ').split('/')
d2, m2, a2 = int(d2), int(m2), int(a2)
 
print('Ocorre primeiro: ', end='')
 
if a1 < a2:
    print(f'{d1:02}/{m1:02}/{a1}')
else:
    if a2 < a1:
        print(f'{d2:02}/{m2:02}/{a2}')
    else:
        if m1 < m2:
            print(f'{d1:02}/{m1:02}/{a1}')
        else:
            if m2 < m1:
                print(f'{d2:02}/{m2:02}/{a2}')
            else:
                if d1 < d2:
                    print(f'{d1:02}/{m1:02}/{a1}')
                else:
                    print(f'{d2:02}/{m2:02}/{a2}')
