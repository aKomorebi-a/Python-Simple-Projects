import random
from typing import List, Tuple
import time
import os

# Definición de la clase base Objeto


class Objeto:
    def __init__(self, nombre: str, simbolo: str):
        self.nombre = nombre
        self.simbolo = simbolo  # Representación visual del objeto
        self.energia = 100      # Todos los objetos comienzan con 100 de energía

    def interactuar(self, otro_objeto, posicion: Tuple[int, int], otra_posicion: Tuple[int, int]) -> str:
        """Método base para la interacción entre objetos"""
        return f"No hay interacción definida entre {self.nombre} y {otro_objeto.nombre}"

    def __str__(self) -> str:
        return self.simbolo

    def estado_detallado(self) -> str:
        """Devuelve una representación detallada del estado del objeto"""
        return f"{self.nombre} ({self.simbolo}) - Energía: {self.energia}"

# Definición de tipos específicos de objetos


class Planta(Objeto):
    def __init__(self):
        super().__init__("Planta", "🌱")
        self.edad = 0

    def interactuar(self, otro_objeto, posicion: Tuple[int, int], otra_posicion: Tuple[int, int]) -> str:
        if isinstance(otro_objeto, Sol):
            self.energia += 20
            return f"La planta absorbe energía del sol y crece (+20 energía)"
        elif isinstance(otro_objeto, Agua):
            self.energia += 15
            return f"La planta absorbe agua y se fortalece (+15 energía)"
        elif isinstance(otro_objeto, Animal):
            self.energia -= 30
            if self.energia <= 0:
                return f"La planta ha sido consumida por un animal y muere (-30 energía)"
            return f"La planta ha sido parcialmente consumida por un animal (-30 energía)"
        return super().interactuar(otro_objeto, posicion, otra_posicion)

    def estado_detallado(self) -> str:
        return f"{super().estado_detallado()} - Edad: {self.edad} días"


class Animal(Objeto):
    def __init__(self):
        super().__init__("Animal", "🐾")
        self.hambre = 50

    def interactuar(self, otro_objeto, posicion: Tuple[int, int], otra_posicion: Tuple[int, int]) -> str:
        if isinstance(otro_objeto, Planta):
            self.energia += 20
            self.hambre -= 30
            if self.hambre < 0:
                self.hambre = 0
            return f"El animal se alimenta de la planta (+20 energía, -30 hambre)"
        elif isinstance(otro_objeto, Agua):
            self.energia += 10
            return f"El animal bebe agua y recupera energía (+10 energía)"
        elif isinstance(otro_objeto, Animal):
            # Los animales pueden competir o cooperar
            if random.random() < 0.5:  # 50% probabilidad de competir
                self.energia -= 15
                otro_objeto.energia -= 15
                return f"Los animales compiten por recursos (-15 energía cada uno)"
            else:  # 50% probabilidad de cooperar
                self.energia += 5
                otro_objeto.energia += 5
                return f"Los animales cooperan en la búsqueda de alimento (+5 energía cada uno)"
        return super().interactuar(otro_objeto, posicion, otra_posicion)

    def estado_detallado(self) -> str:
        return f"{super().estado_detallado()} - Hambre: {self.hambre}"


class Agua(Objeto):
    def __init__(self):
        super().__init__("Agua", "💧")
        self.pureza = 100

    def interactuar(self, otro_objeto, posicion: Tuple[int, int], otra_posicion: Tuple[int, int]) -> str:
        if isinstance(otro_objeto, Sol):
            self.energia -= 10  # El agua se evapora
            if self.energia <= 0:
                return f"El agua se ha evaporado completamente debido al sol (-10 energía)"
            return f"El agua se evapora parcialmente debido al sol (-10 energía)"
        elif isinstance(otro_objeto, Contaminante):
            self.pureza -= 20
            self.energia -= 15
            if self.pureza <= 0:
                return f"El agua ha sido completamente contaminada (-20 pureza, -15 energía)"
            return f"El agua es contaminada parcialmente (-20 pureza, -15 energía)"
        return super().interactuar(otro_objeto, posicion, otra_posicion)

    def estado_detallado(self) -> str:
        return f"{super().estado_detallado()} - Pureza: {self.pureza}%"


class Sol(Objeto):
    def __init__(self):
        super().__init__("Sol", "☀️")
        self.intensidad = random.randint(70, 100)

    def interactuar(self, otro_objeto, posicion: Tuple[int, int], otra_posicion: Tuple[int, int]) -> str:
        if isinstance(otro_objeto, Planta):
            otro_objeto.energia += self.intensidad // 5
            return f"El sol proporciona energía a la planta (+{self.intensidad // 5} energía)"
        elif isinstance(otro_objeto, Agua):
            otro_objeto.energia -= self.intensidad // 10
            return f"El sol evapora parcialmente el agua (-{self.intensidad // 10} energía)"
        return super().interactuar(otro_objeto, posicion, otra_posicion)

    def estado_detallado(self) -> str:
        return f"{super().estado_detallado()} - Intensidad: {self.intensidad}%"


class Contaminante(Objeto):
    def __init__(self):
        super().__init__("Contaminante", "🏭")
        self.toxicidad = random.randint(50, 100)

    def interactuar(self, otro_objeto, posicion: Tuple[int, int], otra_posicion: Tuple[int, int]) -> str:
        if isinstance(otro_objeto, Planta):
            otro_objeto.energia -= self.toxicidad // 5
            if otro_objeto.energia <= 0:
                return f"La planta ha muerto debido a la contaminación (-{self.toxicidad // 5} energía)"
            return f"La planta sufre por la contaminación (-{self.toxicidad // 5} energía)"
        elif isinstance(otro_objeto, Agua):
            otro_objeto.pureza -= self.toxicidad // 4
            if otro_objeto.pureza <= 0:
                return f"El agua ha sido completamente contaminada (-{self.toxicidad // 4} pureza)"
            return f"El agua es contaminada (-{self.toxicidad // 4} pureza)"
        elif isinstance(otro_objeto, Animal):
            otro_objeto.energia -= self.toxicidad // 7
            if otro_objeto.energia <= 0:
                return f"El animal ha muerto debido a la contaminación (-{self.toxicidad // 7} energía)"
            return f"El animal sufre por la contaminación (-{self.toxicidad // 7} energía)"
        return super().interactuar(otro_objeto, posicion, otra_posicion)

    def estado_detallado(self) -> str:
        return f"{super().estado_detallado()} - Toxicidad: {self.toxicidad}%"

# Clase principal para la simulación


class Simulacion:
    def __init__(self, filas: int, columnas: int):
        self.filas = filas
        self.columnas = columnas
        self.grid = [[None for _ in range(columnas)] for _ in range(filas)]
        self.dia_actual = 0
        self.historico = []  # Para almacenar el histórico de eventos

        # Inicializar el grid con objetos aleatorios
        self.inicializar_grid()

    def inicializar_grid(self):
        """Inicializa el grid con objetos aleatorios"""
        tipos_objeto = [Planta, Animal, Agua, Sol, Contaminante]
        # Probabilidades para cada tipo
        probabilidades = [0.3, 0.2, 0.2, 0.15, 0.15]

        for i in range(self.filas):
            for j in range(self.columnas):
                # Decidir si crear un objeto o dejar vacío (20% probabilidad de vacío)
                if random.random() < 0.8:
                    tipo_objeto = random.choices(
                        tipos_objeto, probabilidades)[0]
                    self.grid[i][j] = tipo_objeto()

    def obtener_vecinos(self, fila: int, columna: int) -> List[Tuple[Objeto, Tuple[int, int]]]:
        """Obtiene los vecinos de una posición dada (arriba, abajo, izquierda, derecha)"""
        vecinos = []
        # Arriba, abajo, izquierda, derecha
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for df, dc in direcciones:
            nueva_fila, nueva_columna = fila + df, columna + dc

            # Verificar si está dentro de los límites
            if 0 <= nueva_fila < self.filas and 0 <= nueva_columna < self.columnas:
                # Verificar que haya un objeto en esa posición
                if self.grid[nueva_fila][nueva_columna] is not None:
                    vecinos.append(
                        (self.grid[nueva_fila][nueva_columna], (nueva_fila, nueva_columna)))

        return vecinos

    def simular_dia(self) -> List[str]:
        """Simula un día de interacciones entre los objetos"""
        self.dia_actual += 1
        eventos = []

        # Copia temporal del grid para actualizar sin afectar las interacciones
        nuevo_grid = [[self.grid[i][j]
                       for j in range(self.columnas)] for i in range(self.filas)]

        # Para cada posición en el grid
        for i in range(self.filas):
            for j in range(self.columnas):
                objeto_actual = self.grid[i][j]

                # Si hay un objeto en esta posición
                if objeto_actual is not None:
                    # Envejecimiento y procesos naturales
                    if isinstance(objeto_actual, Planta):
                        objeto_actual.edad += 1
                        # Las plantas ganan energía naturalmente con el tiempo
                        objeto_actual.energia += 5
                        eventos.append(
                            f"Posición ({i},{j}): La planta crece y gana energía (+5)")

                    elif isinstance(objeto_actual, Animal):
                        # Los animales pierden energía y aumentan su hambre con el tiempo
                        objeto_actual.energia -= 5
                        objeto_actual.hambre += 10
                        eventos.append(
                            f"Posición ({i},{j}): El animal pierde energía y aumenta su hambre (-5 energía, +10 hambre)")

                        # Si el animal tiene mucha hambre, pierde más energía
                        if objeto_actual.hambre > 80:
                            objeto_actual.energia -= 10
                            eventos.append(
                                f"Posición ({i},{j}): El animal está muy hambriento y pierde energía extra (-10)")

                    # Obtener vecinos
                    vecinos = self.obtener_vecinos(i, j)

                    # Si hay vecinos, interactuar con uno aleatorio
                    if vecinos:
                        vecino, pos_vecino = random.choice(vecinos)
                        resultado = objeto_actual.interactuar(
                            vecino, (i, j), pos_vecino)
                        eventos.append(
                            f"Posición ({i},{j}) -> ({pos_vecino[0]},{pos_vecino[1]}): {resultado}")

                    # Verificar si el objeto debe ser eliminado (muerte)
                    if objeto_actual.energia <= 0:
                        nuevo_grid[i][j] = None
                        eventos.append(
                            f"Posición ({i},{j}): {objeto_actual.nombre} ha muerto o desaparecido")

        # Actualizar el grid
        self.grid = nuevo_grid

        # Eventos de generación aleatoria (nacimientos, clima, etc.)
        self.eventos_aleatorios(eventos)

        return eventos

    def eventos_aleatorios(self, eventos: List[str]):
        """Genera eventos aleatorios como nacimientos, cambios climáticos, etc."""
        # Probabilidad del 10% de que nazca una nueva planta en un espacio vacío
        if random.random() < 0.1:
            espacios_vacios = [(i, j) for i in range(self.filas)
                               for j in range(self.columnas) if self.grid[i][j] is None]
            if espacios_vacios:
                i, j = random.choice(espacios_vacios)
                self.grid[i][j] = Planta()
                eventos.append(
                    f"Posición ({i},{j}): Ha nacido una nueva planta")

        # Probabilidad del 5% de que haya una lluvia que beneficie a todas las plantas y aguas
        if random.random() < 0.05:
            eventos.append(
                "¡Ha comenzado a llover! Todas las plantas ganan energía y el agua aumenta su pureza")
            for i in range(self.filas):
                for j in range(self.columnas):
                    if self.grid[i][j] is not None:
                        if isinstance(self.grid[i][j], Planta):
                            self.grid[i][j].energia += 15
                        elif isinstance(self.grid[i][j], Agua):
                            self.grid[i][j].pureza += 10
                            if self.grid[i][j].pureza > 100:
                                self.grid[i][j].pureza = 100

    def mostrar_grid(self):
        """Muestra el estado actual del grid"""
        print(f"\n=== Día {self.dia_actual} ===")

        # Imprimir encabezado de columnas
        print("  ", end="")
        for j in range(self.columnas):
            print(f" {j} ", end="")
        print()

        for i in range(self.filas):
            print(f"{i} ", end="")
            for j in range(self.columnas):
                if self.grid[i][j] is None:
                    print(" · ", end="")
                else:
                    print(f" {self.grid[i][j]} ", end="")
            print()

    def mostrar_estadisticas(self):
        """Muestra estadísticas sobre los objetos en el grid"""
        tipos = {
            "Planta": 0,
            "Animal": 0,
            "Agua": 0,
            "Sol": 0,
            "Contaminante": 0
        }

        # Contar objetos por tipo
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.grid[i][j] is not None:
                    tipos[self.grid[i][j].nombre] += 1

        print("\n=== Estadísticas ===")
        for tipo, cantidad in tipos.items():
            print(f"{tipo}: {cantidad}")

        # Calcular porcentaje de ocupación
        total_celdas = self.filas * self.columnas
        celdas_ocupadas = sum(tipos.values())
        porcentaje_ocupacion = (celdas_ocupadas / total_celdas) * 100
        print(
            f"Ocupación: {celdas_ocupadas}/{total_celdas} ({porcentaje_ocupacion:.2f}%)")

    def mostrar_detalles_objeto(self, fila: int, columna: int):
        """Muestra detalles de un objeto específico"""
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            objeto = self.grid[fila][columna]
            if objeto is not None:
                print(f"\nDetalles del objeto en ({fila},{columna}):")
                print(objeto.estado_detallado())
            else:
                print(f"\nNo hay objeto en la posición ({fila},{columna})")
        else:
            print("\nPosición fuera de los límites del grid")

    def ejecutar_simulacion(self, dias: int, mostrar_eventos: bool = True, delay: float = 1.0):
        """Ejecuta la simulación por un número determinado de días"""
        print(f"Iniciando simulación para {dias} días...")
        self.mostrar_grid()

        for _ in range(dias):
            # Limpiar la pantalla en sistemas Unix/Linux/MacOS
            if os.name == 'posix':
                os.system('clear')
            # Limpiar la pantalla en Windows
            else:
                os.system('cls')

            eventos = self.simular_dia()
            self.mostrar_grid()
            self.mostrar_estadisticas()

            if mostrar_eventos:
                print("\n=== Eventos ===")
                for evento in eventos:
                    print(evento)

            # Esperar antes del siguiente día
            time.sleep(delay)

        print(f"\nSimulación completada. Transcurrieron {dias} días.")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una simulación con un grid de 6x8
    sim = Simulacion(filas=6, columnas=8)

    # Ejecutar la simulación por 10 días
    sim.ejecutar_simulacion(dias=2, mostrar_eventos=True, delay=2.0)

    # También se puede obtener información detallada de un objeto específico
    # print("\nConsulta de un objeto específico:")
    # fila = int(input("Introduce la fila del objeto a consultar: "))
    # columna = int(input("Introduce la columna del objeto a consultar: "))
    # sim.mostrar_detalles_objeto(fila, columna)
