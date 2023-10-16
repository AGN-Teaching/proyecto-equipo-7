import csv
import os
from CadenaHotelera import CadenaHotelera
from CompaniaHotel import CompaniaHotel
from Cliente import Cliente
from CompaniaHotel import CompaniaHotel
from Sucursal import Sucursal
from HotelAllinclusive import HotelAllInclusive
from HotelBusiness import HotelBusiness
from HotelFiveStars import HotelFiveStars


class Asesor:

    def __init__(self):
            self.clientes = {}# Diccionario para almacenar clientes (nombre, correo) como clave y ID de cliente como valor
            self.registro_clientes = "clientes.txt"
            # Cargar registros de clientes existentes
            if os.path.isfile(self.registro_clientes):
                with open(self.registro_clientes, "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        parts = line.strip().split(", ")
                        if len(parts) >= 4:
                            id_cliente, nombre, correo, tarjeta = parts[:4]  # Asegúrate de que haya al menos 4 partes
                            self.clientes[(nombre, correo)] = id_cliente

            self.contador_clientes = len(self.clientes) + 1  # Inicializar contador de clientes

    def registrar_usuario(self):
        nombre = input("Nombre del cliente: ")
        numero_telefonico = input("Número de teléfono del cliente: ")
        correo = input("Correo del cliente: ")

        while True:
            tarjeta = input("Tarjeta de crédito del cliente (16 dígitos sin espacios): ")
            if len(tarjeta) == 16 and tarjeta.isdigit():
                # El número de tarjeta tiene 16 dígitos sino se ingresan
                break
            else:
                print("El número de tarjeta no es válido. Debe tener exactamente 16 dígitos.")
                #Manda un mensaje de que no se introdujeron correctamente

        # Generar un nuevo ID para el cliente
        id_cliente = str(self.contador_clientes)
        # Incrementar el contador de clientes
        self.contador_clientes += 1

        cliente = Cliente(id_cliente, nombre, numero_telefonico, correo, tarjeta)

        with open("clientes.txt", "a") as file:
            file.write(
                f" {cliente.get_id()}, Nombre: {cliente.get_nombre()}, Número de Teléfono: {cliente.get_numero_telefonico()}, Correo: {cliente.get_correo()}, Tarjeta de Crédito: {cliente.get_tarjeta()}\n")

        self.x = print(
            f"Cliente registrado exitosamente. Su ID es: {cliente.get_id()} ")

    def reservacion(self):
        id_cliente = input("Ingresa tu ID de cliente (De la forma 'ID: #'): ")

        # Verificar si el ID del cliente es válido
        if id_cliente not in self.clientes.values():
            print("ID de cliente no válido. Por favor, regístrate primero.")
            return  # Salir del método si el ID de cliente no es válido

        fecha = input("Fecha de la reservación (dd/mm/aaaa): ")

        print("Elige una compañía de hotel:")
        print("1. All Inclusive")
        print("2. Business Class")
        print("3. Five Star")

        opcion_compania = input("Selecciona una opción (1/2/3): ")

        if opcion_compania == "1":
            compania = compania_all_inclusive
            tipos_habitacion = ["Suite", "Doble", "Sencilla"]
        elif opcion_compania == "2":
            compania = compania_business_class
            tipos_habitacion = ["Sencilla"]
        elif opcion_compania == "3":
            compania = compania_five_star
            tipos_habitacion = ["Familiar", "Estándar"]
        else:
            print("Opción no válida. Selecciona una opción válida.")
            return  # Salir del método si la opción no es válida

        # Bucle para seleccionar una sucursal
        while True:
            # Mostrar los tipos de habitación disponibles
            print("Tipos de habitación disponibles:")
            for i, tipo in enumerate(tipos_habitacion, start=1):
                print(f"{i}. {tipo}")

            opcion_tipo_habitacion = input("Selecciona un tipo de habitación (Ingrese el número): ")

            # Verificar si la opción del tipo de habitación es válida
            if opcion_tipo_habitacion.isnumeric() and 1 <= int(opcion_tipo_habitacion) <= len(tipos_habitacion):
                tipo_habitacion = tipos_habitacion[int(opcion_tipo_habitacion) - 1]
            else:
                print("Opción no válida. Selecciona un tipo de habitación válido.")
                continue  # Continuar con el bucle para seleccionar una sucursal

            print("Direcciones de las sucursales disponibles:")
            for sucursal in compania.sucursales:
                print(sucursal.get_direccion())

            sucursal_direccion = input("Dirección de la sucursal: ").strip().lower()  # Convertir a minúsculas

            # Buscar la sucursal en la compañía
            sucursal = None
            for s in compania.sucursales:
                if s.get_direccion().strip().lower() == sucursal_direccion:
                    sucursal = s
                    break

            if sucursal is not None:
                # Preguntar al cliente por el número de habitaciones y los huéspedes en cada habitación
                num_habitaciones = int(input("Número de habitaciones que necesitas: "))
                num_huespedes_por_habitacion = int(input("Número de huéspedes por habitación: "))
                edades_huespedes = input("Edades de los huéspedes (separadas por comas): ")

                # Actualizar la disponibilidad de la sucursal con la información de la reservación
                sucursal.agregar_disponibilidad(tipo_habitacion, num_habitaciones, num_huespedes_por_habitacion,
                                                edades_huespedes)

                # Resto del código como lo tenías, agregando el tipo de habitación y los detalles de los huéspedes
                with open("reservaciones.csv", mode='a', newline='') as file:
                    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([fecha, id_cliente, sucursal_direccion, compania.get_nombre(), tipo_habitacion,
                                     num_habitaciones, num_huespedes_por_habitacion, edades_huespedes])

                print("Reservación realizada exitosamente.")
                break  # Salir del bucle para seleccionar una sucursal
            else:
                print("La dirección de la sucursal no existe. Inténtalo de nuevo.")

    def verificar_cliente_registrado(self, nombre, correo):
            # Verificar si el cliente está registrado
            if (nombre, correo) in self.clientes:
                return f"El usuario está registrado. ID del cliente: {self.clientes[(nombre, correo)]}"
            else:
                return "El usuario no se encuentra registrado. Por favor, realiza su registro."

    def disponibilidad_fechas(self):
        if os.path.isfile("reservaciones.csv"):
            with open("reservaciones.csv", mode='r') as file:
                reader = csv.reader(file)
                reservaciones = list(reader)
            if reservaciones:
                print("Reservaciones existentes:\n")
                for fila in reservaciones:
                    if len(fila) >= 6:  # Verificar si hay suficientes valores en la fila (incluyendo la compañía y tipo de habitación)
                        fecha = fila[0]
                        cliente_nombre = fila[1]
                        sucursal_direccion = fila[2]
                        compania = fila[3]
                        tipo_habitacion = fila[4]
                        # Nuevos campos
                        num_habitaciones = fila[5]
                        num_huespedes_por_habitacion = fila[6]
                        edades_huespedes = fila[7]

                        print(
                            f"Fecha: {fecha}, Cliente: {cliente_nombre}, Sucursal: {sucursal_direccion}, Compañía: {compania}, Habitación: {tipo_habitacion}")
                        print(
                            f"Número de Habitaciones: {num_habitaciones}, Número de Huéspedes por Habitación: {num_huespedes_por_habitacion}, Edades de Huéspedes: {edades_huespedes}")
                    else:
                        print("Fila de reservación no válida:", fila)
                    print()  # Separador entre reservaciones
            else:
                print("No hay reservaciones existentes.")
        else:
            print("No hay reservaciones existentes.")

    def agregar_sucursal(self):
        direccion = input("Dirección de la sucursal: ")

        # Mostrar las compañías disponibles
        print("Compañías disponibles:")
        print("1. Business Class")
        print("2. Five Stars")
        print("3. All Inclusive")
        opcion_compania = input("Selecciona una compañía (1/2/3): ")

        if opcion_compania == "1":
            compania = compania_business_class
        elif opcion_compania == "2":
            compania = compania_five_star
        elif opcion_compania == "3":
            compania = compania_all_inclusive
        else:
            print("Opción no válida. No se ha agregado la sucursal.")
            return

        telefono = input("Número de teléfono de contacto: ")

        sucursal = Sucursal(direccion, telefono, compania)

        # Agregar la nueva sucursal a la lista de sucursales de la compañía
        compania.agregar_sucursal(sucursal)

        with open("sucursales.txt", "a") as file:
            file.write(
                f"Compañía: {compania.get_nombre()}, Dirección: {sucursal.get_direccion()}, Teléfono de contacto: {telefono}\n")

        print(f"Sucursal agregada exitosamente a la compañía {compania.get_nombre()}")

    def obtener_id_cliente(self):
        nombre = input("Nombre del cliente: ")
        correo = input("Correo del cliente: ")

        # Verificar si el cliente está registrado
        with open("clientes.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.split(", ")
                if len(parts) >= 4:
                    id_cliente = parts[0].strip()
                    nombre_registrado = parts[1].split(": ")[1].strip()
                    correo_registrado = parts[3].split(": ")[1].strip()
                    if nombre == nombre_registrado and correo == correo_registrado:
                        return f"El usuario está registrado. ID del cliente: {id_cliente}"

        return "El usuario no se encuentra registrado. Por favor, realiza su registro."
compania_all_inclusive = CompaniaHotel("Teléfono de All Inclusive", "All Inclusive")
compania_business_class = CompaniaHotel("Teléfono de Business Class", "Business Class")
compania_five_star = CompaniaHotel("Teléfono de Five Star", "Five Star")

cadena_hotelera = CadenaHotelera("Aqua Horizon Hotels", "AquaHoriHotls@cadenahotelera.com")
companias_hotel = cadena_hotelera.get_companiashotel()
companias_hotel.extend([compania_all_inclusive, compania_business_class, compania_five_star])
# Crear objetos de las compañías HotelAllInclusive, HotelBusiness, y HotelFiveStars
compania_all_inclusive = HotelAllInclusive("Teléfono de All Inclusive", "All Inclusive")
compania_business_class = HotelBusiness("Teléfono de Business Class", "Business Class")
compania_five_star = HotelFiveStars("Teléfono de Five Star", "Five Star")

# Crear objetos de Sucursal para cada compañía
sucursal_all_inclusive = Sucursal("Calle de la Playa #123, Ciudad del Sol", "+1 (123) 456-7890",
                                  compania_all_inclusive)
sucursal_all_inclusive1 = Sucursal("Avenida del Paraíso #456, Costa Hermosa", "+1 (234) 567-8901",
                                   compania_all_inclusive)
sucursal_all_inclusive2 = Sucursal("Paseo de las Palmas #789, Playa Serena", "+1 (345) 678-9012",
                                   compania_all_inclusive)
sucursal_all_inclusive3 = Sucursal("Bulevar del Mar #1011, Puerto Pleno", "+1 (456) 789-0123",
                                   compania_all_inclusive)
sucursal_all_inclusive4 = Sucursal("Bahía del Descanso #1314, Villa Tranquila", "+1 (567) 890-1234",
                                   compania_all_inclusive)
sucursal_all_inclusive5 = Sucursal("Calle de las Olas #1517, Bahía Azul", "1 (678) 901-2345",
                                   compania_all_inclusive)
sucursal_all_inclusive6 = Sucursal("Avenida del Coral #1819, Playa Serena", "+1 (789) 012-3456",
                                   compania_all_inclusive)
sucursal_all_inclusive7 = Sucursal("Avenida del Mar #2123, Costa Hermosa", "+1 (890) 123-4567",
                                   compania_all_inclusive)
sucursal_all_inclusive8 = Sucursal("Paseo del Sol #2425, Villa Tranquila", "+1 (901) 234-5678",
                                   compania_all_inclusive)
sucursal_all_inclusive9 = Sucursal("Bulevar de las Palmas #2729, Ciudad del Sol", "+1 (012) 345-6789",
                                   compania_all_inclusive)

sucursal_business_class = Sucursal("Calle del Centro #123, Ciudad de Negocios", "+1 (234) 567-8901", compania_business_class)
sucursal_business_class1 = Sucursal("Avenida Ejecutiva #456, Distrito Empresarial", "+1 (345) 678-9012", compania_business_class)
sucursal_business_class2 = Sucursal("Paseo de la Oportunidad #789, Plaza Corporativa", " +1 (456) 789-0123", compania_business_class)
sucursal_business_class3 = Sucursal("Bulevar Ejecutivo #1011, Centro Empresarial", "+1 (567) 890-1234", compania_business_class)
sucursal_business_class4 = Sucursal("Calle de las Oficinas #1314, Zona Ejecutiva", "+1 (678) 901-2345", compania_business_class)
sucursal_business_class5 = Sucursal("Avenida de las Reuniones #1517, Distrito Empresarial", "+1 (789) 012-3456", compania_business_class)
sucursal_business_class6 = Sucursal("Paseo de los Ejecutivos #1819, Ciudad de Negocios", "+1 (890) 123-4567", compania_business_class)
sucursal_business_class7 = Sucursal("Bulevar de las Empresas #2123, Plaza Corporativa", "+1 (901) 234-5678", compania_business_class)
sucursal_business_class8 = Sucursal("Calle de las Reuniones #2425, Distrito Ejecutivo", "+1 (012) 345-6789", compania_business_class)
sucursal_business_class9 = Sucursal("Avenida del Éxito #2729, Centro de Negocios", "+1 (123) 456-7890", compania_business_class)

# Repite el proceso para otras compañías
sucursal_five_star = Sucursal("Calle del Lujo #123, Ciudad Estelar", "+1 (345) 678-9012", compania_five_star)
sucursal_five_star1 = Sucursal("Avenida de las Estrellas #456, Distrito de Elegancia", "+1 (456) 789-0123", compania_five_star)
sucursal_five_star2 = Sucursal("Paseo del Glamour #789, Villa de Lujo", "+1 (567) 890-1234", compania_five_star)
sucursal_five_star3 = Sucursal("Bulevar de la Grandeza #1011, Resort Exclusivo", "+1 (678) 901-2345", compania_five_star)
sucursal_five_star4 = Sucursal("Calle de las Suites #1314, Mansión Brillante", "+1 (789) 012-3456", compania_five_star)
sucursal_five_star5 = Sucursal("Avenida de la Opulencia #1517, Villa de las Estrellas", "+1 (890) 123-4567", compania_five_star)
sucursal_five_star6 = Sucursal("Paseo de la Lujuria #1819, Distrito de Elegancia", "+1 (901) 234-5678", compania_five_star)
sucursal_five_star7 = Sucursal("Bulevar del Esplendor #2123, Ciudad Estelar", "+1 (012) 345-6789", compania_five_star)
sucursal_five_star8 = Sucursal("Calle del Glamour #2425, Villa Brillante", "+1 (123) 456-7890", compania_five_star)
sucursal_five_star9 = Sucursal("Avenida de las Suites #2729, Resort de Lujo", "+1 (234) 567-8901", compania_five_star)

# Organizar las sucursales en las compañías
compania_all_inclusive.agregar_sucursal(sucursal_all_inclusive)
compania_all_inclusive.agregar_sucursal(sucursal_all_inclusive1)
compania_all_inclusive.agregar_sucursal(sucursal_all_inclusive2)
compania_all_inclusive.agregar_sucursal(sucursal_all_inclusive3)
compania_all_inclusive.agregar_sucursal(sucursal_all_inclusive4)
compania_all_inclusive.agregar_sucursal(sucursal_all_inclusive5)
compania_all_inclusive.agregar_sucursal(sucursal_all_inclusive6)
compania_all_inclusive.agregar_sucursal(sucursal_all_inclusive7)
compania_all_inclusive.agregar_sucursal(sucursal_all_inclusive8)
compania_all_inclusive.agregar_sucursal(sucursal_all_inclusive9)
# Repite el proceso para otras compañías
compania_business_class.agregar_sucursal(sucursal_business_class)
compania_business_class.agregar_sucursal(sucursal_business_class1)
compania_business_class.agregar_sucursal(sucursal_business_class2)
compania_business_class.agregar_sucursal(sucursal_business_class3)
compania_business_class.agregar_sucursal(sucursal_business_class4)
compania_business_class.agregar_sucursal(sucursal_business_class5)
compania_business_class.agregar_sucursal(sucursal_business_class6)
compania_business_class.agregar_sucursal(sucursal_business_class7)
compania_business_class.agregar_sucursal(sucursal_business_class8)
compania_business_class.agregar_sucursal(sucursal_business_class9)
compania_five_star.agregar_sucursal(sucursal_five_star)
compania_five_star.agregar_sucursal(sucursal_five_star1)
compania_five_star.agregar_sucursal(sucursal_five_star2)
compania_five_star.agregar_sucursal(sucursal_five_star3)
compania_five_star.agregar_sucursal(sucursal_five_star4)
compania_five_star.agregar_sucursal(sucursal_five_star5)
compania_five_star.agregar_sucursal(sucursal_five_star6)
compania_five_star.agregar_sucursal(sucursal_five_star7)
compania_five_star.agregar_sucursal(sucursal_five_star8)
compania_five_star.agregar_sucursal(sucursal_five_star9)

asesor = Asesor()

while True:
    print(f"\nBienvenido a {cadena_hotelera.get_nombre()}")
    print(f"Contacto: {cadena_hotelera.get_contacto()}")
    print("\nMenu:")
    print("1. Registrar usuario")
    print("2. Disponibilidad de fechas")
    print("3. Agregar sucursal")
    print("4. Reservación")
    print("5. Obtener ID de cliente")
    print("6. Salir\n")
    print("Compañías hoteleras en la cadena:")
    for compania in companias_hotel:
        print(compania.get_nombre())

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        asesor.registrar_usuario()
    elif opcion == "2":
        asesor.disponibilidad_fechas()
    elif opcion == "3":
        asesor.agregar_sucursal()
    elif opcion == "4":
        asesor.reservacion()
    elif opcion == "5":
        resultado = asesor.obtener_id_cliente()
        print(resultado)
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
