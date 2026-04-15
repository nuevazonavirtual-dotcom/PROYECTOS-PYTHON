# 1. USO DE COMILLAS "" Y CONCATENACION MAS SIMBOLO +

# DATOS CLIENTES
# nombre = "Ryan"
# apellido = "Burn"
# edad = 26
# cargo = "Contador publico"
# saldo = 200000
# telefono = 3130934567
# email = "polloloko@gmail.com"

#print("Cliente: " + nombre +" " + apellido)

# 2. USO DE LA COMA ,
#print("nombre:", nombre, "apellido:", apellido)

# 3. USO DE F-STRINGS {}
#print(f"Hola, soy {nombre} {apellido} y tengo {edad} años")

# 4. OPERADORES MATEMATICOS SIGNOS +-*/
#saldo = saldo + 50000
#print("Nuevo saldo:", saldo)

# saldo = saldo * 24
# print("Nuevo saldo:", saldo)

# OPERACIONES DE COMPARACION ==,<>
#print("Tienes mucho dinero", saldo < 7000000)   # SIMBOLO < SIGNIFICA MAS, MAYOR QUE... TRUE
#print("Tienes mucho dinero", saldo > 7000000)   # SIMBOLO > SIGNIFICA MENOS, MENOR QUE... FALSE

#CONDICIONALES USO DEL SIMBOLO IF :
#if saldo > 650000:
#    print("Cliente Vip")
#else:
#    print("Cliente normal")


#DICCIONARIO CITAR DATOS COMPLETOS TIPO DE CLIENTE USAN ={"":,} 
# Cliente = {
#      "Nombre": nombre,
#      "apellido": apellido,
#      "Edad": edad,
#      "Cargo": cargo,
#      "Saldo": saldo
# }

# print(Cliente["Edad"])

#LISTAS, CITAR DATOS ESPECIFICOS DE UNA LISTAS ["",]
#Clientes = ["Ryan", "Carlos", "Anna"]

#print (Clientes[2])


# #OPERADORES LOGICOS AND, OR, NOT
# if saldo > 400000 and edad > 28:
#     print("CLIENTE APROBADO :)" )
# else:
#     print("CLIENTE RECHAZADO :(")

#EJERCCIOS PRACTICOS DE REPASO LOGICO MAYOR QUE O MENOS QUE, if y else, operadores matematicos, f-strings, diccionarios y listas

# print(f"Cliente:{nombre}{apellido}")
# if saldo > 200000:
#     print("Tiene buen saldo")
# else:
#     print("Tiene bajo saldo")
# saldo = saldo + 100000

# print(f"Saldo actualizado: {saldo}")


# EJERCICIOS PRACTICOS #
# DATOS INICIALES #
# Nombre = "Mayiyuz"
# Primer_apellido = "Rodriguez"
# Segundo_apellido = "Valencia"
# Edad = 22
# Saldo = 300000


# DICCIONARIO
# USUARIOS= {
#     "Nombre": Nombre,
#     "Primer_apellido": Primer_apellido,
#     "Segundo_apellido": Segundo_apellido,
#     "Edad": Edad,
#     "Saldo": Saldo
# }
# print(USUARIOS)


# NOMBRE COMPLETO (STRING)
#print(f"Cliente: {Nombre} {Primer_apellido} {Segundo_apellido}")


# FORMULA MAYOR QUE > (EN ESTE CASO MAYOR DE EDAD)
# if Edad >= 18:
#     print("Mayor de edad y con buen saldo, cliente aprobado")
# else:
#     print("mMenos de edad o con bajo saldo, cliente rechazado")

# AUMENTO DEL 10% *=1.10
#Saldo = Saldo + (Saldo *0.10)

#print(f"Nuevo saldo: {Saldo}")



# 🎯 OBJETIVO
# Crear un programa que:

# Guarde varios usuarios
# Muestre la información de cada uno
# Evalúe si son mayores de edad
# Aplique aumento del 10% al saldo
# Muestre el saldo actualizado

#### 📝DESARROLLO DE ACTIVIADAD.
# USUARIOS, CUANDO SON VARIOS ACCIONES DEBEN SER LISTAS, DICCIONARIOS O UNA COMBINACION DE AMBOS
# EN ESTE CASO SE USARAN DICCIONARIOS DENTRO DE UNA LISTA, PARA GUARDAR VARIOS USUARIOS CON SUS RESPECTIVOS DATOS

#DICCIONARIO
Cliente = [
    {
    "Primer_nombre": "Miguel",
    "Segundo_nombre": "Santiago",
    "Primer_apellido": "Rodriguez",
    "Segundo_apellido": "Panto",
    "Edad": 23,
    "Saldo": 100000
    },
    {
    "Primer_nombre": "Laura",
    "Segundo_nombre": "Isabel",
    "Primer_apellido": "Gomez",
    "Segundo_apellido": "Lopez",
    "Edad": 25,
    "Saldo": 150000
    },
    {
    "Primer_nombre": "Andres",
    "Segundo_nombre": "Felipe",
    "Primer_apellido": "Martinez",
    "Segundo_apellido": "Garcia",
    "Edad": 17,
    "Saldo": 80000
    }
]

print ("Informacion de los clientes:")
for Cliente in Cliente: # FORMULA PARA RECORRER LA LSITA DE CLIENTES
    print(f"Cliente: {Cliente['Primer_nombre']} {Cliente['Segundo_nombre']} {Cliente['Primer_apellido']} {Cliente['Segundo_apellido']}")
    
    # EVALUAR SI ES MAYOR DE EDAD  
    if Cliente ["Edad"] >=18:
        print("Mayor de edad, Cliente aprobado")
    else: 
        print("Menos de edad, Cliente rechazado")

# AUMENTO DEL 10% AL SALDO
Saldo = Cliente ['Saldo'] + (Cliente ['Saldo'] * 0.10)
print(f"Saldo actualizado con el 10%: {Saldo}")



