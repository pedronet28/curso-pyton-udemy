# los iteradores son la forma mas adecuada
# para recorrer una lista en python

#Ejemplo1 recorriedo un arreglo de texto 

lenguajes = ['Java','Python','JavaScrip','Ruby','Php','Kotlin','Go']
#interator
#en variable lenguaje se asignara el valor del registro en 
# cada ciclo del iterator  
for lenguaje in lenguajes:
    print(f'Estoy aprendiendo {lenguaje}')


#Ejemplo2 Iterator por rango de numeros 
#en este ejemplo se muestra la forma de generar una serie 
#de numeros determinados por un rango inicial y uno final
# Nota: la serie solo contendra números partiendo del ragon 
# inicial y menores que el rango final!!
for numero in range(0,10):
    print(numero)
    
#Ejemplo3 Iterator de numero con parametro de incremento
#en este ejemplo a diferencia del anterior se le agrega un tercer
#parametro que indica el valor de ingremento en la serie veamos!!

#el numero 2 indica el incremento en cada ciclo
print('Ejemplo con parametro de incremento')
for numero in range(0,10,2): 
    print(numero)                         

lun 28 sep 2020 12:39:43 -05
