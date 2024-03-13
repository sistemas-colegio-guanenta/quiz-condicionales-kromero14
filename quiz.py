# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrse el valor de b: "))
c = float(input("Ingrese el valor de c: "))

# processing
if a + b > c:
   Resultado= ("si puede ser un triangulo")
   if a + c > b:
    Resultado=("si puede ser un triangulo")
    if b + c > a:
     Resultado=("si puede ser un triangulo")
else:
   Resultado=("no puede ser un triangulo")

# output
    
print("Los lados", a, ",", b, "y", c, Resultado )