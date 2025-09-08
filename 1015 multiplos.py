valores = input().split()

n1 = int(valores[0])
n2 = int(valores[1])

if n1<n2:
    if n2%n1 > 0:
        print('Nao sao Multiplos')
    else:
        print('Sao Multiplos')
else:
    if n1%n2 > 0:
        print('Nao sao Multiplos')
    else:
        print('Sao Multiplos')
        
