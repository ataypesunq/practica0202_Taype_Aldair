# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
fecha_nac = input("Fecha de nacimiento(dd/mm/aaaa): ")
seleccion = fecha_nac.split("/")
print(f"Día: {seleccion[0]}")
print(f"Mes: {seleccion[1]}")
print(f"Año: {seleccion[2]}")