# funciones con numeros

#ejemplo 1
#definiendo la funcion 
def suma():
    print(f'resultado de la suma = {2+3}')
    # la letra f al inicio dentro de los parentesis indica que
    # se va a unir el texto siguiente con lo que esta
    # dentro de las llaves, que en este caso es una suma  de dos 
    # valores numerios que bien pueden ser la suma de dos variables! 

#llamando la funcion
suma() 

#ejemplo 2
# definiendo funcion con parametros
# Nota: se asigna un valor por defecto, para que así la operacion
# se realise incluso con la ausencia de uno de los dos parametros
# y no se produzca ningun error!  

def operacionesMaatematicas(num1=0,num2=0):
    print(f'Resultado de la suma = {num1+num2}')
    print(f'Resultado de la resta = {num1-num2}')
    print(f'Resultado de la multiplicacion = {num1*num2}')
    print(f'Resultado de la division = {num1/num2}')

operacionesMaatematicas(5,8)
