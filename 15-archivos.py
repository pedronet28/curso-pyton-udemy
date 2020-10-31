def app():
    archivo = open('archivo.txt','w') # "w" hace referencia al permiso de escritura en archivo 
    # la instruccion open abre o crea un archivo si este no existe!!
    
    # Generar numeros en archivo!!
    for i in range (0,20):
        archivo.write('Esta es la linea:'+str(i)+"\r\n")

   # Cerrar el archivo
    archivo.close()     
app()    