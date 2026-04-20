
# entrenador= "kami"

# pkm1=6

# entrenador2="sabrina"
# pkm2=7

# if pkm1<=6:
#     print("Puede acceder a la liga pokemon")
# else:
#     print("tiene mas pokemon de los necesarios")


# print(len(entrenador))


# print("el entrenador", entrenador, "tiene", pkm1, "pokemons")
# print("el entrenador", entrenador, "tiene", pkm2, "pokemons")
# print(f"el entrenador {entrenador}, tiene {pkm2} pokemons)

# print(f"Hola {entrenador}"*3)
# name="ana"
# #     012
# print(name[2])
# el ultimo siempre es -1

# pedir la clave al usuario y verificar que sea shazam independiente de su case
# indiferente de mayusculas o minusculas


# contra=int(input("ingrese la contraseña"))
# passw="SHAZAM"
# if passw==contra:
#    print("ingreso correcto")
# else:
#     print("error clave invalida")
# NOMBRE DE USUARIO
user=input("ingrese su nombre de usuario")

if len(user)<4 :
    print("muy pocos caracteres, use al menos 4")
elif len(user)>10:
    print("tiene muchos caracteres,use 10 o menos")
else:
    print("usuario creado correctamente")