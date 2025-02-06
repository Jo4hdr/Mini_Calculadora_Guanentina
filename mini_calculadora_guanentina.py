#Calculadora

# Input
print("(------------------------------)")
x = input("Digite el primer número (X): ")
Y = input("Digite el segundo número (Y)")
print("(------------------------------)")

# Covertir entradas a enteros
x = float(x)
y =float(Y)

# Menú de opciones
print("(------------------------------)")
print("1 = Sumar (X + Y)")
print("2 = Restar (X - Y)")
print("3 = Multiplicar (X * Y)")
print("4 = Dividir (X / Y)")
print("5 = Potencia (X ^ Y)")
print("6 = Logaritmación (log(X) base Y)")
print("(------------------------------)")

# Input de la opción
opcion = input("Elige una opción (1-6): ")
opcion = int(opcion)

# Procesar según la opción
if opcion == 1:
    resultado = x + y
elif opcion == 2: 
    resultado = x - y 
elif opcion == 3:
    resultado = x * y
elif opcion == 4: 
    if y != 0:
        resultado = x / y 
    else:
        resultado = "Error: Division por cero"
elif opcion == 5: 
    resultado = x ** y 
elif opcion == 6: 
    if x > 0 and y > 0:
        import math
        resultado = math.log(x, y)
    else:
        resultado = "Error: Logaritmo no válido (X y Y deben ser mayores que 0)"
else:
    resultado = "Opción no valida"

# Output 
print("(------------------------------)")
print("Resultado: ", resultado)
print("(------------------------------)")