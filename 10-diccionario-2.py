# Ejemplo 2 Iniciando diccionario vacio!!

juego = {}
print(juego)

# Agregando un jugador 
juego['Nombre'] = 'Pedro'
juego['Puntaje'] = 0
print(juego)

# Incrementado puntaje
juego['Puntaje'] = 100
print(juego)

juego['Puntaje'] = 200
print(juego)

# Accediendo a un valor de un atributo en el diccionario
# Nota: si el nombre del atributo no exite, se puede lanzar un mensaje 
# predefinido como manejo de error, si no se incluye el mensaje
# phyton lanzara "None", para indicarnos que no encontro el atributo 
print(juego.get('Consola','No existe el Atributo'))


#Agregando atributo consala para una segunda prueba
juego ['Consola'] = 'PS4'
print(juego)
print(juego.get('Consola','No existe el Atributo'))



#Iterar un diccionario

for llave, valor in juego.items():
    print(llave)
    print(valor)

# Eliminar Atributos del diccionario 

del juego['Nombre']
del juego['Puntaje']
del juego['Consola']
print(juego)
