class CryptoMonedas:
    def __init__(self, nombre, simbolo, precio, volumen, capitalizacion, supply):
        self.nombre = nombre
        self.simbolo = simbolo
        self.__precio = precio
        self.__volumen = volumen
        self.__capitalizacion = capitalizacion
        self.__supply = supply

    def get_precio(self):
        return self.__precio

    def get_supply(self):
        return self.__supply

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Precio inválido")
    
    def mostrar_info(self):
        print(f"{self.nombre} ({self.simbolo}) - Precio: ${self.__precio}")

    def convertir_a_mxn(self, tipo_cambio):
        print(f"Precio en MXN: ${self.__precio * tipo_cambio}")

    
