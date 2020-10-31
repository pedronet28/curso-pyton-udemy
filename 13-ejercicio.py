playlist = {} # Diccionario vacio
playlist['Canciones']=[] # Lista vacia

#Función Agregar Nombre Playlist
def agregarNombrePlaylist():
    # print('Desde agregarNombrePlaylist!')
    agregar_playlist = True 
    while agregar_playlist:
        nombre_playlist = input('¿Cómo deseas nombrar la playlist?..\r\n')
        if nombre_playlist:
           playlist['Album'] = nombre_playlist
           agregar_playlist = False
                
# Definiendo función para agregar cación a playlist
def agregarCancion():
    # print('Desde AgregarCancion!')
    agregar_cancion = True
    pregunta = f'\r\nAgregar canciones para la playlist {playlist["Album"]}: \r\n'
    pregunta += 'Escribe "x", para dejar de agregar canciones \r\n'
    while agregar_cancion:
        nombre_cancion = input(pregunta)        
        if nombre_cancion.upper() == 'X':
            agregar_cancion = False
        else:    
            playlist['Canciones'].append(nombre_cancion)

#Defino función para mostrar album de canciones!!                
def mostrarAlbum():
    print('Información de mi playlist!!\r\n')
    print(f'Album: {playlist["Album"]}\r\n')
    print('Lista de caciones: \r\n')
    for cancion in playlist["Canciones"]:
        print(cancion)

# Función principal
def app():
    agregarNombrePlaylist() 
    agregarCancion()
    mostrarAlbum()


app()

