x=int(input("Digite um valor inteiro"))
z=int(input("Digite um valor inteiro"))
print(x-z)
import math
numero1=int(input('Informe um valor:'))
numero2=int (input ('Informe o segundo valor:'))
calc=numero1/numero2
calc1=numero1//numero2
calc2=numero1%numero2
i=2
primo=True
print('Divisão:',calc)
while i<=math.sqrt(calc):
	if calc2%i==0:
		primo=False
	i=i+1
if primo==True:
	print (calc, 'é primo')
else:
	print(calc,'não é primo')
print ('Anteriores de:', calc)
while calc1 > 0:
	calc1-=1
	print (calc1, end=" ")
print ()

