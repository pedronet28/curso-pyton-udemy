import archivo_agenda as ag

def app():
    menu  = True

    while menu:
        mostrar_menu()
        opcion = input('¿Digite el número de la  opción...?:  ')
        if opcion.isnumeric():
               if int(opcion) == 1: 
                    ag.crear_contacto()
               elif int(opcion) == 2:
                    nombre = ag.pregunta_nombre()
                    if  ag.buscar_contacto(nombre):
                         ruta = ag.get_ruta(nombre)
                         ag.mostrar_contato(ruta)
                    else:
                         ag.mensaje_error(2,nombre)     
               elif int(opcion) == 3:
                    ag.editar_contato()
               elif int(opcion) == 4:
                    ag.eliminar_contacto()   
               elif int(opcion) == 5:
                    ag.listar_contactos()
               elif int(opcion) == 6:
                    print('\r\nGracias por usar nuestra aplicación..!!\r\n')
                    menu = False     
               else:
                    print('\r\n!Opción invalida...\r\n')
        else:
            print('\r\n!NOTIFICACION: Solo números del (1 - 6)...!!\r\n')


def mostrar_menu():
    print('\r\n')
    print('*********************************************************')
    print('*             !Bienvenido al menu principal.             *')
    print('*********************************************************\r\n')
    print('Elija la opción del menu que desea realizar:\r\n ')
    print('1)--> Crear contacto...')
    print('2)--> Bucar contacto...')
    print('3)--> Editar contacto...')
    print('4)--> Eliminar contacto...')
    print('5)--> Listar contactos...')
    print('6)--> Salir de la aplicación!...\r\n')


app()
