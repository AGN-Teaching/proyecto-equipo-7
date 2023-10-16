from CompaniaHotel import CompaniaHotel

class HotelFiveStars(CompaniaHotel):
    def __init__(self, numero_telefono, nombre):
        super().__init__(numero_telefono, nombre)
        self.tipos_habitacion = ["Familiar", "Estándar"]