#coleta de dados
n1 = float(input('digite um numero\n'))
n2 = float(input('digite outro numero\n'))
#menu inicial
print("""escolha uma das opçōes abaixo: 
[1]adição
[2] subtração
[3] multiplicação
[4] divisão""")
op = str(input('qual sua escolha?\n '))
print("/////"*10)
#adição dos numeros
if op == "1":
	soma = n1+n2
	print(f'O resultado de {n1} + {n2} é: {soma}')
#subtração dos numeros
elif op == "2":
	sub = n1-n2
	print(f'O resultado de {n1} - {n2} é: {sub}')
#multiplicação dos numeros
elif op == "3":
	multi = n1*n2
	print(f'O resultado de {n1} * {n2} é: {multi}')
#divisão dos numeros
elif op == "4":
	divi = n1/n2
	print(f'O resultado de {n1} / {n2} é: {divi}')
#resposta falsa
else:
	print('o terminal não recebeu uma resposta verdadeira')
