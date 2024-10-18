# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
producto = input("Nombre del producto: ")
precio = float(input("Precio del producto: "))
num_ud = int(input("Numero de unidades: "))
coste_total = precio * num_ud
print((
    f"{producto} tiene el precio de {precio:6.2f}, "
    f"el numero de unidades es {num_ud:3d}, "
    f"con un coste total de {coste_total:8.2f}"
))