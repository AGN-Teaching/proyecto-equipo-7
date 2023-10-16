class Cliente:
    def __init__(self, id_cliente, nombre, numero_telefonico, correo, tarjeta):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.numero_telefonico = numero_telefonico
        self.correo = correo
        self.tarjeta = tarjeta

    def get_id(self):
        return self.id_cliente

    def get_nombre(self):
        return self.nombre

    def get_numero_telefonico(self):
        return self.numero_telefonico

    def get_correo(self):
        return self.correo

    def get_tarjeta(self):
        return self.tarjeta
