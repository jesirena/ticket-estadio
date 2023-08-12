#primera parte solo fines de semana
n=0
fecha=""
tb=5
costtal=0
#solicitud de datos para el usuario
n=int(input("ingresa la cantidad de boletas a comprar"))
fecha=input("la boleta es para fin de semana?(si o no)")
#condicional para fecha
if fecha == "si":
  costtal=tb*1.20
else:
  costtal=tb
#solo fines de semana
#el ussurio ingresa el palco
palco=input("la boleta es para el palco a,b,c")
if palco=="a":
  costtal+=tb*.1    # costtal=costtal+tb*.1
elif palco=="b":
  costtal+=tb*.05

#terera parte 
#proceso por descuento por cantidad de boletas
if n>=5 and n<=10:
    costtal=costtal*.90
if n>=15 and n<=20:
    costtal=costtal*.85
if n>=25:
    costtal=costal*.80

print ("el costo total a pagar:", round(costtal*n,2))#para redondear la cifra se usa la funcion round