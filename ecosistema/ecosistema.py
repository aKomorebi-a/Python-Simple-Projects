# Crea un simulador simple de un ecosistema donde diferentes especies de animales y plantas interactúan entre sí a lo largo del tiempo.
# El programa debería incluir:

# Diferentes tipos de organismos (herbívoros, carnívoros, plantas)
# Un sistema de reproducción y ciclo de vida para cada especie
# Interacciones entre especies (alimentación, competencia por recursos)
# Condiciones ambientales variables (clima, estaciones) que afecten al ecosistema
# Visualización del estado del ecosistema en cada ciclo (puede ser simplemente texto)
# Estadísticas que muestren la evolución de las poblaciones

# Frugívoros. Aquellos que se alimentan principalmente de frutas, ya sea constantemente (generalmente en el trópico) o de manera estacional (en las latitudes templadas).
# Folívoros. Aquellos que se alimentan de las hojas y tallos de las plantas, a menudo con la ayuda de bacterias simbióticas que les permiten absorber los nutrientes y descomponer la abundante celulosa.
# Xilófagos. Aquellos que se alimentan de madera, en su gran mayoría artrópodos.
# Granívoros. Aquellos que se alimentan de semillas o granos.
# Rizófagos. Aquellos que se alimentan de raíces.

import random


class Plant:

    def __init__(self, name: str, tipo: str):
        posible_ciclo: int = [5, 8, 10, 12, 15]
        planta_vida: int = random.choice(posible_ciclo)
        self.name = name
        self.tipo = tipo
        self.vida = planta_vida

    def __str__(self):
        return f" Esta planta es una: {self.name}"

    def fotosintesis(self, clima):
        fotosintesis = 0
        if clima == "soleado":
            x = random.randint(1, 10)
            fotosintesis += 100 - x
            if fotosintesis >= 100 or fotosintesis >= 80:
                self.vida += 5
                print(f"\n{self.name} hizo la fotosintesis")
                print(f"vive {self.vida} semanas")
            else:
                self.vida -= 5
                print(f"vive {self.vida} semanas")
        if clima == "nublado":
            x = random.randint(1, 20)
            fotosintesis += 50 - x
            if fotosintesis >= 50 or fotosintesis >= 40:
                self.vida += 2
                print(f"\n{self.name} hizo la fotosintesis")
                print(f"vive {self.vida} semanas")
            else:
                self.vida -= 5
                print(f"vive {self.vida} semanas")

        if clima == "lluvioso":
            x = random.randint(1, 30)
            fotosintesis += 50 - x
            if fotosintesis >= 50 or fotosintesis >= 40:
                self.vida -= 1
                print(f"\n{self.name} no logro hacer la fotosintesis")
                print(f"vive {self.vida} semanas")
            else:
                self.vida -= 6
                print(f"vive {self.vida} semanas")

        if clima == "tormenta":
            x = random.randint(1, 25)
            fotosintesis += 30 - x
            if fotosintesis == 30 or fotosintesis >= 25:
                self.vida -= 2
                print(f"\n{self.name} no hizo la fotosintesis")
                print(f"vive {self.vida} semanas")
            else:
                self.vida -= 10
                print(f"vive {self.vida} semanas")

        if clima == "nevado soleado":
            x = random.randint(1, 15)
            fotosintesis += 30 - x
            if fotosintesis == 30 or fotosintesis >= 27:
                self.vida += 1
                print(f"\n{self.name} hizo la fotosintesis")
                print(f"vive {self.vida} semanas")
            else:
                self.vida -= 5
                print(f"vive {self.vida} semanas")

        if clima == "nevado nuboso":
            x = random.randint(1, 18)
            fotosintesis += 20 - x
            if fotosintesis == 20 or fotosintesis >= 10:
                self.vida -= 10
                print(f"\n{self.name} no hizo la fotosintesis")
                print(f"vive {self.vida} semanas")
            else:
                self.vida -= 10
                print(f"vive {self.vida} semanas")


class Herbivoro:

    def __init__(self, name: str, tipoDeHerb: str):
        posible_ciclo: int = [10, 15, 20, 25, 30, 35]
        herbivoro_vida: int = random.choice(posible_ciclo)

        self.name = name
        self.tipoDeHerb = tipoDeHerb
        self.vida = herbivoro_vida

    def __str__(self):
        return f"Se llama {self.name} y es un herbivoro de tipo: {self.tipoDeHerb}"

    def comer(self, plant):

        if self.tipoDeHerb.lower() == "frugivoros" and plant.lower() == "fruta":
            self.vida += 2
            print(f"{self.name} comio {plant}")
            print(f"vivira una {self.vida} semana mas")
        elif self.tipoDeHerb == "folivoros" and plant == "planta":
            self.vida += 2
            print(f"{self.name} comio {plant}")
            print(f"vivira una {self.vida} semana mas")
        elif self.tipoDeHerb == "rizofagos" and plant == "raiz":
            self.vida += 2
            print(f"{self.name} comio {plant}")
            print(f"vivira una {self.vida} semana mas")
        else:
            print("no pudo comer")
            self.vida -= 5
            print(f"Ahora vive {self.vida}")


class Carnivoros:
    def __init__(self, name: str):
        posible_ciclo = [10, 20, 30, 40, 50]
        carnivoro_vida = random.choice(posible_ciclo)

        self.name = name
        self.vida = carnivoro_vida

    def __str__(self):
        return f"El carnivoro se llama {self.name}"


def ecosistema_weather(estacion):
    primavera: str = ['soleado', 'soleado', 'nublado', 'lluvioso']
    verano: str = ['soleado']
    otoño: str = ['nublado', 'lluvioso', 'nublado', 'nublado', 'tormenta']
    invierno: str = ['nevado nuboso', 'nevado soleado',
                     'nevado nuboso', 'nevado soleado']

    if estacion.lower() == 'primavera':
        return random.choice(primavera)
    elif estacion.lower() == 'verano':
        return random.choice(verano)
    elif estacion.lower() == 'otoño':
        return random.choice(otoño)
    elif estacion.lower() == 'invierno':
        return random.choice(invierno)
    else:
        return None


def ecosis() -> list:
    eco = [
        ['1', '2', '3', '4'],
        ['5', '6', '7', '8']
    ]
    return eco


p1 = Plant("manzana", "planta")
h1 = Herbivoro("venado", "folivoros")
c1 = Carnivoros("tigre")


def interaccionesComer(plant, herb) -> str:
    if plant.tipo == "fruta" and herb.tipoDeHerb == "folivoros":
        plant.vida - plant.vida
        print("La planta fue comida")
    else:
        print(f"{herb.name} no quiso comerse la {plant.name}")

# for i in range(1, 20):
#     ciclos = i
#     estaciones = ["primavera", "verano", "otoño", "invierno"]
#     clima = ecosistema_weather(random.choice(estaciones))
#     if ciclos <= p1.vida:
#         print(f"\n{p1.name} sigue viva")
#         print(f"\nEl clima es {clima}")
#         p1.fotosintesis(clima)
#         print(f"espectativa de vida de la {p1.name}, {p1.vida} semanas")
#         print(f"ha pasado {ciclos} semana")
#     else:
#         print(f"\nse murio la {p1.name}")
#         print(f"ha pasado {ciclos} semana")
