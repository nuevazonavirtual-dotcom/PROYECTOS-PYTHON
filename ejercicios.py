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

#EJERCICIO NUEVO DATOS INICIALES
Nombre = "Mayiyuz"
Primer_apellido = "Rodriguez"
Segundo_apellido = "Valencia"
Edad = 22
Saldo = 300000

#DICCIONARIO
# USUARIOS= {
#     "Nombre": Nombre,
#     "Primer_apellido": Primer_apellido,
#     "Segundo_apellido": Segundo_apellido,
#     "Edad": Edad,
#     "Saldo": Saldo
# }
# print(USUARIOS)

# NOMBRE COMPLETO (STRING)
print(f"Cliente: {Nombre} {Primer_apellido} {Segundo_apellido}")

# MAYOR DE EDAD
if Edad >= 18:
    print("Mayor de edad y con buen saldo, cliente aprobado")
else:
    print("mMenos de edad o con bajo saldo, cliente rechazado")

# AUMENTO DEL 10% *=1.10
Saldo = Saldo + (Saldo *0.10)

print(f"Nuevo saldo: {Saldo}")


