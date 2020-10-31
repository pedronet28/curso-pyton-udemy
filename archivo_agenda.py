import os
#import contacto as ct
from contacto import Contacto 


CARPETA = 'agenda/'
EXTENSION = '.txt'
   
def crear_carpeta():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)
    

# El parametro bandera recibe dos valores posibles 1 == Creacion && 4 == actualizacion
def crear_contacto():
    crear_carpeta()
    existe = True
    while existe:
          nombre = pregunta_nombre()
          existe = buscar_contacto(nombre)
          if not existe: 
             # la función ".capitalize()", convierte la primera letra de la cadena en mayúscula y 
             # la función ".upper()", convierte toda la cadena en mayúscula
             telefono = input('\r\nIngrese teléfono: ')
             categoria = input('\r\nIngrese categoria: ')
             ruta = get_ruta(nombre)  
             contacto = Contacto(nombre.capitalize(),telefono,categoria.capitalize(),ruta)
             break
          else:
              mensaje_error(1,nombre)              
    registrar_datos(contacto)
    # Mensaje Exito operación!
    mensaje_exito(1,contacto.get_nombre())


def editar_contato():
             
    nombreActual = pregunta_nombre()
    if buscar_contacto(nombreActual):
        iterar = True
        while iterar:
            nuevoNombre = input('\r\nNuvo nombre de contacto:  ')
            if nuevoNombre == nombreActual:
               break 
            elif not buscar_contacto(nuevoNombre):
                break
            else:
                mensaje_error(1,nuevoNombre)             
    else:
        mensaje_error(2,nombreActual)
    
    # renombramos archivo con nuevo nombre
    # NOTA: la funcion "os.rename" rembra un archivo, solicitando dos parametros
    # que son: el nombre anterior, y el nuevo nombre, con sus rutas completas 
    # respectivamente.
    os.rename(get_ruta(nombreActual),get_ruta(nuevoNombre))    
    
    # Recolilando resto de informacion de contacto!
    telefono = input('\r\nIngrese nuvo teléfono: ')
    categoria = input('\r\nIngrese nueva categoría: ')
    ruta = get_ruta(nuevoNombre)
    contacto = Contacto(nuevoNombre.capitalize(), telefono, categoria.capitalize(), ruta)
    registrar_datos(contacto)    
    # Mostramos mensaje exito de la operación!
    mensaje_exito(3,contacto.get_nombre())     


def registrar_datos(contacto):      
    # creando archivo archivo!!    
     with open(contacto.get_ruta(),'w') as archivo:
         # Escribiendo en archivo
         archivo.write(contacto.get_nombre()+'\r\n')
         archivo.write(contacto.get_telefono()+'\r\n')
         archivo.write(contacto.get_categoria()+'\r\n')
         archivo.write(contacto.get_ruta()+'\r\n')
      


def buscar_contacto(nombre):
    ruta = get_ruta(nombre)   
    if os.path.isfile(ruta):
        return True
    else:
        return False    



def mostrar_contato(ruta):
    
        # "whit open" abre el archivo y lo cierra automaticamente, cuando se va a escribir sobre
        # el archivo hay que ponert el paremetro 'w' a parte del la ruta inicial
        lis_contenido = []
        with open(ruta) as archivo: # "as archivo" Crea un aleas para trabajar con el archivo
            
            for contenido in  archivo:
                # NOTA: ".rstrip('\n')" elimina espacio en tre lineas!!
                lis_contenido.append(contenido.rstrip('\n'))

        contacto = Contacto(lis_contenido[0],lis_contenido[1],lis_contenido[2],lis_contenido[3])
        contacto.ver_contacto()
                  


def listar_contactos():
    print('\r\n.........................................................')
    print('.              LISTA DE CONTACTOS ALMACENADOS           .')
    print('.........................................................\r\n')
    # la función "os.listdir(nom_carpeta)" carga una lista con todos los
    # los archivos de la carpeta
    archivos = os.listdir(CARPETA)

    # la funcion siguiente carga un arreglo con los archivos que tengan
    # extension ".txt" 
    archivosTxt = [i for i in archivos if i.endswith(EXTENSION)]
     
    # Reconrriendo arreglo "archivosTxt" y mostrando informacion con la 
    # función "monstrar_contacto(nomobre)"
    for contacto in  archivosTxt:
        ruta = CARPETA + contacto
        mostrar_contato(ruta)  

def eliminar_contacto():
     nombre = pregunta_nombre()
     if buscar_contacto(nombre):
        os.remove(get_ruta(nombre))
        mensaje_exito(4,nombre) 
     else:
         mensaje_error(2,nombre)


# La funcion "mostrar_notificacion" recibe dos parámetros el primero 
# es una bandera que indetifica el mensaje que se debe mostrar y el segundo
# corresponde al nombre de contacto que puede ser incluido en el mensaje  
def mensaje_exito(bandera,nombre):
    if bandera == 1:
        print(f'\r\nNOTIFICACION: Nuevo contacto {nombre.capitalize()} creado correctamente...!!\r\n')     
    elif bandera == 2:
        print(f'\r\nNOTIFICACION: Contacto {nombre.capitalize()} encontrado...!\r\n')    
    elif bandera == 3:
        print(f'\r\nNOTIFICACION: Contacto Actualizado...!!\r\n')
            
    elif bandera == 4:
        print(f'\r\nNOTIFICACION: Contacto {nombre.capitalize()} Eliminado correctamente..!!\r\n')

def mensaje_error(bandera,nombre):
    if bandera == 1:
        print(f'\r\nNOTIFICACION: Ya existe un registro con nombre: {nombre}...\r\n')
    elif bandera == 2:
        print(f'\r\nNOTIFICACION: No se encontro ningun registro de {nombre}...\r\n')


def pregunta_nombre():
    nombre = input('\r\nIngrese nombre de contacto:  ')
    return nombre

    
def get_ruta(nombre):
    ruta = CARPETA + nombre.upper() + EXTENSION
    return ruta

