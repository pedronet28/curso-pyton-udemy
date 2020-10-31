# Evaluado formas de condicionales
balance = 200
if balance > 0:
    print('Puedes Pagar')
else:
    print('No tienes Saldo!!')

#Ejemplo2  condicionales conm operador <= o >= equivalente para ambos casos!!
balance2 = 0
if balance2 <= 0:
   print('Saldos insuficientes!!')    
else:
    print(f'Su saldo disponible es {balance2}')
    


#Ejemplo3 condicionales con operador ==
likes = 200
if likes == 20:
    print(f'Excelente Ya tienes {likes} likes')
else:
    print(f'Vale ya casi llegas a 200 likes')

#Ejemplo4 condicionales con operador == con texto
lenguaje = 'Java'
if lenguaje == 'Python':
    print(f'{lenguaje} es una buena eleccion!!') 
else:
    print(f'Hay peores lenguajes que {lenguaje}!!')       

#Ejemplo5 condicionales con booleanos 
#Nota: en los  casos que se evaluan variables con valores
#booleanos no es necesario colocar el signo =

usuario_Activo = False
if usuario_Activo:
    print('Puede Acceder al sistema')
else:
    print('Debe Iniciar sesion')

#Ejemplo6 Arreglos y  condicionales
lenguales = ['PHP','JAVA','PYTHON','JAVASCRIP','RUBY','GO'] 
for lenguaje2 in lenguales:   
    if lenguaje2 == 'PYTHON':
        print(f'{lenguaje2} es una excelente elección!!')
    else:
        print(f'Hay peores lenguales que {lenguaje2}') 

#Ejemplo7 Otro con Arreglos

if 'GO' in lenguales:
    print(f'el Leguane GO, se encuentra en la lista')
else:
    print('el Lenguaje GO, no se encontro en la lista!!')    

#Ejemplo8 if Anidados 

usuario_Activo = True
administrador = True
if usuario_Activo:
    if administrador:
        print('Acceso Tatal!!')
    else:
        print('Acceso a la Aplicación!!')
else:
    print('Debe Iniciar sesion primero!!')            



