class Sucursal:
    def __init__(self, direccion, telefono, companiahotel):
        self.__direccion = direccion
        self.__telefono = telefono
        self.__companiahotel = companiahotel
        self.disponibilidad = {}

    def get_direccion(self):
        return self.__direccion

    def agregar_disponibilidad(self, tipo_habitacion, num_habitaciones, num_huespedes_por_habitacion, edades_huespedes):
        if tipo_habitacion not in self.disponibilidad:
            self.disponibilidad[tipo_habitacion] = []

        self.disponibilidad[tipo_habitacion].append({
            'num_habitaciones': num_habitaciones,
            'num_huespedes_por_habitacion': num_huespedes_por_habitacion,
            'edades_huespedes': edades_huespedes
        })

    def get_disponibilidad(self):
        return self.disponibilidad

    def get_telefono(self):
        return self.__telefono
