from CompaniaHotel import CompaniaHotel

class HotelBusiness(CompaniaHotel):
    def __init__(self, numero_telefono, nombre):
        super().__init__(numero_telefono, nombre)
        self.__tipos_habitacion = ["Sencilla"]