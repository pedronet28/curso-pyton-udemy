#Ejemplo de condicionales empleando operadores and y or 

usuario = 'Particular'
usuario_Activo = False
if usuario_Activo and usuario == 'Estudiante':
     print('descuento del 35%')
elif usuario_Activo and usuario == 'Maestro':
     print('descuento del 20%')     
elif usuario == 'Estudiante' or usuario == 'Maestro' or usuario_Activo : 
     print('descuento del 5%')
else:
     print ('debe pagar el 100%')            