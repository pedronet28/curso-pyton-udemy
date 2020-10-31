# Leer acrhvios con python
def app():
    # with open es una funcion para lectura de
    # archivos por tanto no se hace necesario
    # colocar la la "r" como como atributo de lectura
    # Nota: con "with open()" no se hace necesario cerrar el archivo 
    # el lo cierra automaticamente!     
    with open('archivo.txt') as archivo: # "as archivo" Crea un aleas para trabajar con el archivo
        for contenido in archivo:
            # print(contenido) 
              print(contenido.rstrip()) # .rstrip() elimina espacio en tre lineas!!


app()