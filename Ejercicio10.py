# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
productos_cesta = input("Escribe tu lista de la compra(con comas(,)): ")
cesta = productos_cesta.split(",")
print("\n".join(cesta))