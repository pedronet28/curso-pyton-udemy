
cerrar = True
pregunta = ('Ingresa un numero y te dire si es para o impar \n\r')
pregunta += ('escribe "cerrar" para salir!\n\r') # Forma de concatenar en variables "+="
while cerrar:
    num = input(pregunta)
    if num == 'cerrar':
        cerrar = False
        print('Gracias vuelva pronto!!\n\r')
    else:    
         num = int(num) # Convertimos a el valor de la variable "num" a entero!!
         if(num % 2 == 0 ):
            print(f'El numero {num} es par\n\r')
         elif(num % 2 == 1):
                print(f'El numero {num} es impar\r\n')
