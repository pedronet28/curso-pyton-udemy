#En python los arreglos son  llamados list
#definiendo y cargando un ana list en python

#Ejemplo1
lenguajes = ['Python','Kotlin','Java','JavaScrip']
numeros = [3,5,7,2]
print(lenguajes)

#Ejemplo2  Aplicando método de ordenamiento 
#acendente y alfabetico en list de python
lenguajes.sort()
print(lenguajes)

numeros.sort()
print(numeros)

#Ejemplo3 Accediendo a registro de una lista
#Nota los lista al igual que los arreglos 
#inician en la pocicion 0 

print(lenguajes[0])
print(numeros[3])

#Ejemplo4 adicionando elementos a la lista 
lenguajes.append('Php')
numeros.append(9)
print(lenguajes)
print(numeros)

#Ejemplo5 Remplazando el valor de un registro en la lita
lenguajes[2] = 'Ruby'
numeros[2] = 6
print(lenguajes)
print(numeros)

#Ejemplo6 formas de eliminar un elemento de la lista 

#Forma1 elimina el registro por indice de pocicion
del lenguajes[1]
del numeros[0]
print(lenguajes)
print(numeros)
print(lenguajes[1])
print(numeros[0])

#Forma2 eliminar registro utilizan el metodo pop() sin parametros y com paramentros
lenguajes.pop() # elimina el ultimo registro de la lista
numeros.pop()
print(lenguajes)
print(numeros)

lenguajes.pop(1)# elimina el elemento especificado por su indice  en el parametro
numeros.pop(2)
print(lenguajes)
print(numeros)

#Forma3 elimina un registro de la lista  especifico por su valor 
# utilizando el método remove('valor')

lenguajes.remove('Java')
numeros.remove(6)
print(lenguajes)
print(numeros)