# Cotinuamos con el ejemplo anterior ahora aplicando Encapsulamiento

# Definiendo una clase en python, los nombres de las cases
# inician por letra mayuscula!
class Restaurant:

    # constructor de clase en python
    def __init__(self,nombre, categoria, precio):
        self.__nombre = nombre # pasando parametros a atributo de clase
        self.__categoria = categoria
        self.__precio = precio        

    #definimos método de clase
    def mostrar_informacion(self):
        print(f'Nombre: {self.__nombre}, Categoria: {self.__categoria}, Precio: {self.__precio}\r\n') 

    # Definiendo Metros Getter y Setter "Get = obtiene valor de atributo"
    # Set = Agrega o modifica valor de  atributos de clase 

    def get_nombre(self):
         return self.__nombre  

    def get_categoria(self):
        return self.__categoria

    def get__precio(self):
        return self.__precio

    def set_nombre(self,nombre):
        self.__nombre = nombre

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def set_precio(self,precio):
        self.__precio = precio        

#Instanciamos la clase
restaurant = Restaurant('Pizzeria Mexico','comida italiana',50)
restaurant.mostrar_informacion()
restaurant2 = Restaurant('Hamburguesas python','comida casual',20)
restaurant2.mostrar_informacion()

#Ejemplo de utilizacion de métodos de clase
restaurant.set_categoria('Comida Mexicana')
restaurant.set_precio(80)
restaurant.mostrar_informacion()

restaurant2.set_categoria('Comida organica')
restaurant2.set_precio(40)
restaurant2.mostrar_informacion()

nombre = restaurant2.get_nombre()
categoria = restaurant2.get_categoria()
precio = restaurant2.get__precio()

print(f'Nombre Restaurante: {nombre}')
print(f'Categoria: {categoria}')
print(f'Precio: {precio}')


