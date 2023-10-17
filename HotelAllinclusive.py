from CompaniaHotel import CompaniaHotel

class HotelAllInclusive(CompaniaHotel):
    def __init__(self, numero_telefono, nombre):
        super().__init__(numero_telefono, nombre)
        self.tipos_habitacion = ["Suite", "Doble", "Sencilla"]
