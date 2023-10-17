class CadenaHotelera:
    def __init__(self, nombre, contacto):
        self.__nombre = nombre
        self.__contacto = contacto
        self.companiashotel = []

    def get_nombre(self):
        return self.__nombre

    def get_contacto(self):
        return self.__contacto

    def get_companiashotel(self):
        return self.companiashotel

