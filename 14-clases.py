# Ejemplo de como se crea e implentan clases en python

# Definiendo una clase en python, los nombres de las cases
# inician por letra mayuscula!
class Restaurant:

    # constructor de clase en python
    def __init__(self,nombre, categoria, precio):
        # Nota: los atributos en python pueden definirse como, PUBLIC "self.nombreAtributo"
        # PROTECTED "self._nombreAtributo" notese el guion bajo antes del nombre del atributo
        # PRIVATE "self.__nombreAtributo" notese el doble guion bajo antes del nombre del atributo
        # teniendo en cuenta lo anterior, los atributos de nuetra clase ejmplo estan inicialmente 
        # definidos como publicos por default!! 
        self.nombre = nombre # pasando parametros a atributo de clase
        self.categoria = categoria
        self.precio = precio       

    #definimos método de clase
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}') 

#Instanciamos la clase
restaurant = Restaurant('Pizzeria Mexico','comida italiana',50)
restaurant.mostrar_informacion()
restaurant2 = Restaurant('Hamburguesas python','comida casual',20)
restaurant2.mostrar_informacion()
