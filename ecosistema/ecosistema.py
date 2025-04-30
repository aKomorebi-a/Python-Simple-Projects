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
    # planta_vida = 5
    reproduccion: bool = False

    def __init__(self, name: str, tipo: str):
        posible_ciclo: int = [5, 10, 15, 20, 25, 26, 28]
        planta_vida: int = random.choice(posible_ciclo)
        self.name = name
        self.tipo = tipo
        self.vida = planta_vida

    def __str__(self):
        return f" Esta planta es una: {self.name}"

    def fotosintesis(self, clima):
        fotosintesis = 0
        if clima == "soleado":
            fotosintesis += 100
            if fotosintesis == 100 or fotosintesis >= 80:
                self.vida += 2
                print(f"\n{self.name} hizo la fotosintesis")
                print(f"vive {self.vida} semanas")
        if clima == "nublado":
            fotosintesis += 50
            if fotosintesis == 50 or fotosintesis >= 45:
                self.vida -= 1
                print(f"\n{self.name} no logro hacer la fotosintesis")
                print(f"vive {self.vida} semanas")
        if clima == "tormenta":
            fotosintesis += 30
            if fotosintesis == 30 or fotosintesis >= 25:
                self.vida -= 3
                print(f"\n{self.name} no logro hacer la fotosintesis")
                print(f"vive {self.vida} semanas")


class Herbivoro:
    reproduccion: bool = True
    alimentacion: bool = True

    def __init__(self, name: str, tipoDeHerb: str):
        posible_ciclo: int = [10, 15, 20, 25, 30, 35]
        herbivoro_vida: int = random.choice(posible_ciclo)

        self.name = name
        self.tipoDeHerb = tipoDeHerb
        self.vida = herbivoro_vida

    def __str__(self):
        return f"Se llama {self.name} y es un herbivoro de tipo: {self.tipoDeHerb}"

    def comer(self, plant):

        if self.tipoDeHerb == "frugivoros" and plant == "fruta":
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


p1 = Plant("manzana", "fruta")
h1 = Herbivoro("venado", "folivoros")

h1.comer(p1.tipo)

ecosistema = [
    [0, 0, 0,],
    [0, 0, 0,],
    [0, 0, 0,]
]


for i in range(1, 20):
    ciclos = i
    climas = ["soleado", "nublado", "tormenta"]
    clima = random.choice(climas)
    if ciclos <= p1.vida:
        print(f"\n{p1.name} sigue viva")
        print(f"\nEl clima es {clima}")
        p1.fotosintesis(clima)
        print(f"espectativa de vida de la {p1.name}, {p1.vida} semanas")
        print(f"ha pasado {ciclos} semana")
    else:
        print(f"\nse murio la {p1.name}")
        print(f"ha pasado {ciclos} semana")
