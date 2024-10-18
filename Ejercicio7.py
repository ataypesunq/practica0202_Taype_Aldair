# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delantera de la arroba @) pero con dominio ceu.es.
correo_usuario = input("Escibe tu correo electronico: ")
parte2 = correo_usuario.split("@")
seleccion = parte2[0]
print(f"{seleccion}@ceu.es")