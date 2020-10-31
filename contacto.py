class Contacto:
    def __init__(self,nombre,telefono,categoria,ruta):
       self.__nombre = nombre
       self.__telefono = telefono
       self.__categoria = categoria
       self.__ruta = ruta
      
    # Métodos de clase Gett && Sett

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self,telefono):
        self.__telefono = telefono

    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, categoria):
        self.__categoria = categoria 
   
    def get_ruta(self):
        return self.__ruta
    
    def set_ruta(self, ruta):
        self.__ruta = ruta     

    def ver_contacto(self):
        print('\r\n..........................................................')
        print(f'\r\nInformación del contacto {self.get_nombre().upper()}:\n')
        print(f'Nombre: {self.get_nombre().capitalize()}\r\n')
        print(f'Teléfono: {self.get_telefono()}\r\n')
        print(f'Categoria: {self.get_categoria().capitalize()}\r\n')
        print(f'Ruta: {self.get_ruta()}\r\n')
        print('..........................................................')

    

#contacto = Contacto('nombre',3232323,'categoria','ruta')
