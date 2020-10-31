#Los Diccionarios en Python son la base para la creacion de objetos
#un diccionario esta compuesto por un nombre y sus atributos estan definidos dentro de unas llaves
 

#Ejemplo de creacion de diccionario

cancion = {
        'Artista': 'Diomedes Diaz',  # Atributo y valor, para mas de un atributo se agrega una coma !       
        'Album': 'Diomedes Diaz una historia Disco 2',
        'Titulo': 'Lucero espiritual',
        'Autor': 'Juancho Polo Valencia',
        'Genero': 'Vallenato',
        'Pista': 14,
        'Duración': 3.53
}

#Mostrar datos de  diccionario
print(cancion)


#Mostrar atributos especificos del diccionario
print(cancion['Titulo'])

#Mostrar atributos combinados con texto
#Nota Apreciar en el ejercicio el uso de la combinación de comillas simples y dobles 
# para diferenciar entre el texto nomar y atributos!!  
print(f'El titulo de la cacion es:{cancion["Titulo"]}')

# Agregar atributo a diccionario
cancion['Likes'] = 300
print(cancion)

# Modificar valor de atributo existente en diccionario
cancion['Likes'] = 500
print(cancion)

# Eliminar Atributo de diccionario
del cancion['Likes']
print(cancion)

