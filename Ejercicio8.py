# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
precio = input("Precio del producto: ")
selec = precio.split(".")
print(f"Numero de euros: {selec[0]} ")
print(f"Numero de centimos: {selec[1]}")