[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/XixB-tii)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=12372569)
# Proyecto
## Antecedentes:

Una cadena hotelera consta de varias compañías de hoteles y cada compañía de hoteles tiene varias sucursales. Los hoteles que forman esta cadena se clasifican como all inclusive, business class o five stars. Los hoteles all inclusive tienen 3 tipos de habitaciones: suites, doble y sencilla. Los hoteles business class tienen un solo tipo de habitación. Los hoteles five stars tienen dos tipos de habitaciones: familiar y estándar.
Un cliente puede hacer una reservación para cualquier sucursal de cualquier hotel, pero tiene que registrarse proporcionando su nombre, un número telefónico y una dirección de correo electrónico.
Las reservaciones son hechas por un asesor, quien solicitará al cliente las fechas de hospedaje, el tipo y cantidad de habitaciones, y el número y edades de los huéspedes. Para que la reservación esté garantizada, el cliente deberá proporcionar los datos de una tarjeta de crédito.


De acuerdo con los antecedentes se creó el siguiente diagrama UML con el fin de resolver el  problema:


![Proyecto-Página-6 drawio](https://github.com/AGN-Teaching/proyecto-equipo-7/assets/125332082/388e777b-fc0c-4373-a374-01fe73292bd8)



# Análisis del problema:
Para dar solución al 'problema', debemos tener en cuenta a dónde queremos llegar y cómo lo vamos a lograr. Para ello, debemos considerar el uso de clases.


### ¿Qué clases se ocuparan y por que?


#### Clase CadenaHotelera:

La clase CadenaHotelera tiene como atributos un nombre de tipo String, un número de contacto de tipo entero (int). Este número de contacto se refiere al número de las compañías de hoteles. Y un arreglo que guarde los nombres de las compañías de Hotel []. En los métodos, tendríamos getters de los respectivos atributos.


#### Clase CompañiaDeHoteles:


La clase CompañíaDeHoteles tiene los siguientes atributos: número telefónico de tipo entero (int) y nombre de tipo String. El método de la clase sería un getter, el cual nos proporcionará el número telefónico correspondiente al número de teléfono del hotel.


#### Clase Hotel_All_Inclusive:


Creamos la clase Hotel_All_Inclusive, la cual va a heredar de la clase padre los atributos: número telefónico y el nombre, que se va a referir al nombre del hotel. Sus atributos en particular son los tipos de habitaciones que se mencionan en los antecedentes, con sus respectivos getters.


#### Clase Hotel_business:


La clase Hotel_business de igual manera va a heredar los atributos de la clase padre, y sus atributos son los tipos de habitaciones que ya fueron establecidos en los antecedentes. En este caso, solo es uno y, por ende, tendría un método getter.


#### Clase Hotel_fiveStars:


La clase Hotel_fiveStars hereda los atributos de la clase padre, y sus atributos en particular serían los tipos de habitaciones con sus respectivos getters.



#### Clase Sucursal:

Para poder realizar la clase Sucursal, debemos tomar en cuenta lo que nos mencionan los antecedentes. Si consideramos que los tres hoteles tienen cada uno una sucursal, podemos hacer una clase que tenga como atributos una dirección de tipo String, un teléfono para cada sucursal de tipo entero (int) y una clasificación de tipo String, junto con sus métodos getters.


#### Clase Cliente:

La clase Cliente tiene como atributos: ID de tipo entero (int), nombre del cliente de tipo String, el número de teléfono de tipo entero (int), el correo electrónico de tipo String y un atributo donde se almacenarán los datos de la tarjeta, el cual tiene el nombre de tarjeta: []. Los métodos de la clase Cliente son getters de los respectivos atributos.


#### Clase Asesor:


Funciones de la clase Asesor: Gestiona las interacciones con los clientes, permitiendo el registro de usuarios, reservas, consulta de disponibilidad y adición de sucursales.

La clase Asesor no cuenta con atributos, y solo tiene un método, el cual almacenará los datos del cliente mediante un arreglo.


#### Clase Reservacion:


La clase Reservación tiene como método las fechas de reservación y dos métodos: uno es un getter, para saber qué días están disponibles para hacer una reservación, y el otro se encarga de agregar la reservación.


### Tipos de relaciones

#### *Herencia*


Como mencionamos anteriormente, existen tres tipos de clases que establecen una relación de herencia, ya que heredan atributos de la clase base 'CompañíaDeHoteles'. Estos tipos de clases son subclases que extienden las propiedades y comportamientos de la clase padre, aprovechando la estructura jerárquica para compartir atributos y métodos comunes.


![Herencia drawio](https://github.com/AGN-Teaching/proyecto-equipo-7/assets/125332082/4ef5ba62-2cf8-47be-8971-39800f5ab8e0)

#### *Asociación*


Las tres clases, Hotel_All_Inclusive, Hotel_Business y Hotel_FiveStars, tienen asociación con Sucursal, ya que los tres hoteles le brindan servicio a las sucursales. Sucursal y Cliente tienen asociación con Asesor, ya que estas dos clases le proporcionan servicio a la clase Asesor para que este último brinde servicio a la clase Reservación, la cual se encargará de solucionar la problemática inicial.


#### *Manejo de errores*


![Captura de pantalla 2023-10-15 224147](https://github.com/AGN-Teaching/proyecto-equipo-7/assets/125332082/34575157-f2ce-4846-9f28-62cc4b214f79)


Aquí mostramos uno de los manejos de errores:
La función cargar_clientes_registrados maneja el caso en el que el archivo de registros no se encuentra, evitando un error FileNotFoundError. La función guardar_registro_cliente se encarga de guardar los registros del cliente en el archivo.


![Asociacion drawio](https://github.com/AGN-Teaching/proyecto-equipo-7/assets/125332082/364f1def-43f9-46dc-a97f-338284de18a8)


El manejo de errores debe ser específico para cada situación en la que se pueda producir un error y debe proporcionar mensajes de error claros y descriptivos para que el usuario comprenda lo que salió mal.
## Conclusiones:


### Conclusión de Uriel

La implementación del diagrama UML a un lenguaje de programación es esencial para convertir el diseño visual y conceptual de un sistema en un producto de software funcional y ejecutable. La conclusión clave aquí es que el proceso de traducir un diagrama UML a código no es solo un acto mecánico, sino una fase crítica que requiere comprensión, habilidad y precisión ya que debemos de tener cuidado con diversos temas de la Programación Orientada a Objetos, como lo pueden ser la creación de clases y la manera en la que se relacionan y con este proyecto se pone a prueba todo lo visto en la UEA Programación Orientada a Objetos.


### Conclusión de Eduardo

La Programación Orientada a Objetos (POO) es crucial en el desarrollo de software por varias razones. En primer lugar, permite organizar el código de manera más efectiva al agrupar datos y comportamientos relacionados en objetos, lo que facilita su comprensión y mantenimiento. Además, fomenta la reutilización del código a través de conceptos como la herencia y la encapsulación, lo que reduce la duplicidad y mejora la eficiencia del desarrollo.


### Conclusión de Irving

En conclusión, los diseños UML (Lenguaje de Modelado Unificado) son herramientas fundamentales en la Programación Orientada a Objetos (POO) porque nos permiten visualizar, planificar y resolver problemas de manera efectiva y estructurada. Estos diagramas proporcionan una representación gráfica y conceptual de sistemas complejos, lo que facilita la comprensión de los requisitos del usuario y el diseño de soluciones eficientes en el contexto de la POO.
