class CompaniaHotel:
    def __init__(self, numero_telefono, nombre):
        self.__numero_telefono = numero_telefono
        self.__nombre = nombre
        self.__tipos_habitacion = []
        self.sucursales = []

    def get_numero_telefono(self):
        return self.__numero_telefono

    def get_nombre(self):
        return self.__nombre

    def get_tipos_habitacion(self):
        return self.__tipos_habitacion

    def agregar_sucursal(self, sucursal):
        self.sucursales.append(sucursal)