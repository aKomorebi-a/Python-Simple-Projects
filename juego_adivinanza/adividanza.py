'''Proyecto: Juego de Adivinanza con Pistas'''
# Crea un juego donde el jugador debe adivinar un número secreto entre 1 y 100. El juego debe:

#     Generar un número aleatorio al inicio.

#     Permitir múltiples intentos hasta adivinar o agotar 10 oportunidades.

#     Dar pistas como "más alto" o "más bajo".

#     Llevar registro de intentos anteriores.

#     Incluir una opción para reiniciar el juego sin salir.
import random


class JuegoAdivinanza:
    def __init__(self, secret_number: int, intentos: int):
        self.secret_number = secret_number
        self.intentos = intentos
        self.historial = []

    def adivinar_numero(self, numero_user: int):
        '''Malas condicionales'''
        # if self.intentos != 0:
        #     if numero_user == self.secret_number:
        #         self.intentos -= 1
        #         self.historial.append(numero_user)
        #         print(f"Es correcto el numero es {self.secret_number}")
        #     elif numero_user <= 50 and numero_user < self.secret_number:
        #         self.intentos -= 1
        #         self.historial.append(numero_user)
        #         print("mmmm, mas alto")
        #         print(f"Intentos restantes: {self.intentos}")
        #     elif numero_user <= 90 and numero_user < self.secret_number:
        #         self.intentos -= 1
        #         self.historial.append(numero_user)
        #         print("casi, mas bajo")
        #         print(f"Intentos restantes: {self.intentos}")
        #     elif numero_user <= 20 and numero_user < self.secret_number:
        #         self.intentos -= 1
        #         self.historial.append(numero_user)
        #         print("mmm, mucho mas arriba")
        #         print(f"Intentos restantes: {self.intentos}")
        #     else:
        #         self.intentos -= 1
        #         self.historial.append(numero_user)
        #         print("estas muy cerca")
        #         print(f"Intentos restantes: {self.intentos}")
        # else:
        #     print("Te quedaste sin intentos 😥")
        if self.intentos > 0:
            self.historial.append(numero_user)
            self.intentos -= 1  # Descuenta siempre al ingresar un número

            if numero_user == self.secret_number:
                print(f"¡Correcto! El número es {self.secret_number}")
            else:
                diferencia = abs(numero_user - self.secret_number)
                if numero_user < self.secret_number:
                    mensaje = "Más alto"
                else:
                    mensaje = "Más bajo"

                # Pistas basadas en proximidad
                if diferencia <= 5:
                    mensaje += " ¡Estás muy cerca!"
                elif diferencia <= 15:
                    mensaje += " ¡Caliente!"
                else:
                    mensaje += " ¡Frío!"

                print(f"{mensaje} | Intentos restantes: {self.intentos}")

    def empezar_juego(self):
        while self.intentos != 0:
            try:
                numero_user = int(input("Adivina el numero: "))

                self.adivinar_numero(numero_user)
                print("\nTu historial de intentos")
                for i in self.historial:
                    print("- ", "".join(str(i)))

                if numero_user == self.secret_number:
                    break
            except ValueError:
                print("Error, ingresa un numero")
        else:
            print(f"\nMala suerte, el numero era: {self.secret_number}")


num = random.randint(1, 100)
inten: int = 2

adiv = JuegoAdivinanza(num, inten)

adiv.empezar_juego()
