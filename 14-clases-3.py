# Cotinuamos con el ejemplo anterior ahora aplicando Herencia

# Definiendo una clase en python, los nombres de las clases
# inician por letra mayuscula!
class Restaurant:

    # constructor de clase en python
    def __init__(self,nombre, categoria, precio):
        self.__nombre = nombre # pasando parametros a atributo de clase
        self.__categoria = categoria
        self.__precio = precio        

    #definimos método de clase
    def mostrar_informacion(self):
        nombre = self.get_nombre()
        categoria = self.get_nombre()
        precio = self.get_precio()

        print(f'Nombre: {nombre}, Categoria: {categoria}, Precio: {precio}') 

    # Definiendo Metros Getter y Setter "Get = obtiene valor de atributo"
    # Set = Agrega o modifica valor de  atributos de clase 

    def get_nombre(self):
         return self.__nombre  

    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio

    def set_nombre(self,nombre):
        self.__nombre = nombre

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def set_precio(self,precio):
        self.__precio = precio        


# Definimos una clase que hereda de la clase Restaurant
class Hotel(Restaurant):
    # Creamos el constructor de la clase el cual debe tener 
    # los atritutos de la clase padre mas los nuevos atributos de 
    # nuetra nueva clase hijo en este caso Hotel 
    def __init__(self, nombre, categoria, precio, piscina):

        # colocamos el respetivo constructor que herada los atributos
        # de la clase Padre en este caso "Restaurant", cabe aclarar que 
        # sepueden excluir aquellos que no se van a utilizar! 
        super().__init__(nombre, categoria, precio)
        
        #Nuevos atributos de la clase Holtel!
        self.__piscina = piscina


    # Aplicando poliformismo a la clase reescribiendo un método propio
    # de la clase "Hotel"
    # Reescribiendo método Mostrar información de la clase padre "Restaurant"
    # Nota: los Médotos reescritos deben llamarse de la misma forma como fueron definidos
    # en la clase padre!!
    def mostrar_informacion(self):
         
         nombre = self.get_nombre()
         categoria = self.get_categoria()
         precio = self.get_precio()
         alberca = self.get_piscina()
         piscina = self.get_piscina()
         

         print(f'Nombre:{nombre}, Categoria:{categoria}, Precio:{precio} Piscina:{piscina}\r\n') 
    
    # Getter & Setter del atributo piscina
    def get_piscina(self):
        if  self.__piscina:
            return "Si"
        elif not self.__piscina:
            return "No" 

    def set_piscina(self,piscina):
        self.__piscina = piscina

   
# Instanciamos la clase
hotel = Hotel('Hotel POO','5 Estrellas',200,False)
hotel.mostrar_informacion()
hotel2 = Hotel('Hotel python','5 Estrellas',230,True)
hotel2.mostrar_informacion()

