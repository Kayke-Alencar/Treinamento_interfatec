vendedor = input()
salario_fixo = float(input())
vendas = float(input())

comicao = vendas*(15/100) #PORCENTEAGEM
salario_total = salario_fixo + comicao

print(f'TOTAL = R$ {salario_total:.2f}')
