class CryptoMonedas:
    def __init__(self, nombre, simbolo, precio, volumen, capitalizacion, supply):
        self.nombre = nombre
        self.simbolo = simbolo
        self.__precio = precio
        self.__volumen = volumen
        self.__capitalizacion = capitalizacion
        self.__supply = supply

