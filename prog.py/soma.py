import math
n1=int(input("Informe um valor: "))
n2=int(input("Informe um valor: "))
calc=n1+n2
i=2
primo=True
while i<=math.sqrt(calc):
	if calc%i==0:
		primo=False
	i=i+1
if primo==True:
	print (calc, 'é primo')
else:
	print(calc,'não é primo')
