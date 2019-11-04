import math
i=2
primo=True
x=int(input("Digite um valor inteiro: " ))
y=int(input("Digite um valor inteiro: " ))
calc= x-y
print('Resultado subtração:',x-y)
while i<=math.sqrt(calc):
	if calc%i==0:
		primo=False
	i=i+1
if primo==True:
	print (calc, 'é primo')
else:
	print(calc,'não é primo')
print ('Anteriores de:', calc)
while calc > 0:
	calc-=1
	print (calc, end=" ")
print ()

