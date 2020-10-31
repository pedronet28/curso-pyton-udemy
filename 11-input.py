#Ejemplo de entra de datos en python
'''
nombre = input('Ingresa su nombre..? \r\n') # Nota..\r\n  es la forma de hacer retorno de carro en python!! 
sexo = input('tu sexo es: "F" o "M"..?\n\r')

if(sexo.upper() == 'F'): #la funcion Upper() combierte el texto a mayusculas!!
   print(f'Bienvenida {nombre}')
elif   (sexo.upper() == 'M'):
    print(f'Bienvenido {nombre}')
else: 
    print('Algo salio mal (*_*)!!')    

'''
# Ejemplo etrada de datos con numeros

# En python todas las entradas de datos se toman como string, 
# por lo tanto si los datos  ingresados son numeros se deben convertir 
# previamente al formato correspondiente ya sea ento o flotante para evitar 
# tener errores al momento de trabajar con ellos 
# para convertir de string a entero se usa la funcion int(NUMERO), 
# y para  datos decimales o flotantes flo float(NUMERO)
num =  input('Ingrese un numero y le dire si es par o no..?\r\n')
num = int(num) # Convertimos a el valor de la variable "num" a entero!!
if(num % 2 == 0 ):
    print(f'El numero {num} es par\r\n')
elif(num % 2 == 1):
    print(f'El numero {num} es impar\r\n')
else:
    print(f'El datos {num} no es un numero!')