import math
i=2
j=2
primo=True
x=int(input("Digite um valor inteiro: " ))
y=int(input("Digite um valor inteiro: " ))
calc= x-y
resultado=calc
print('Resultado subtração:',x-y)
while i<=math.sqrt(calc):
	if calc%i==0:
		primo=False
	i=i+1
if primo==True:
	print (calc, 'é primo')
else:
	print(calc,'não é primo')
print ('Anteriores :')
while resultado > 2:
	if resultado%j == 0:
		primo=False
	else: 
		print (resultado, end=" ")
	resultado-=1
print ()

