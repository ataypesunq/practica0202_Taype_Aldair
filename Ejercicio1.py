# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por  pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
usuario = input("Nombre de usuario: ")
num = int(input("Numero entero: "))
rep = (usuario + "\n") * num
print(rep)