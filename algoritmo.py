import math


class TestCAT:
    def __init__(self, preguntas, t):
        self.D = 0.0
        self.L = 0
        self.H = 0
        self.R = 0
        self.W = 0
        self.B = 0
        self.S = 0.0
        self.T = t
        self.preguntas = preguntas
        self.banco_preguntas = preguntas

    def tomar_prueba(self):
        while self.seguir_prueba():
            pregunta = self.elegir_pregunta()
            self.L += 1
            if self.hacer_pregunta(pregunta):
                self.R += 1
                self.D += 2 / self.L
            else:
                self.D -= 2 / self.L
            self.H += self.D

        self.W = self.L - self.R
        self.B = self.H / self.L + math.log(self.R / self.W)

        if self.W == 0:
            self.B = self.H / self.L + math.log((self.R - 0.5) / (self.W + 0.5))
        if self.R == 0:
            self.B = self.H / self.L + math.log((self.R + 0.5) / (self.W - 0.5))

        self.S = math.sqrt(self.L / (self.R * self.W))
        if self.W == 0:
            self.S = math.sqrt(self.L / ((self.R - 0.5) * (self.W + 0.5)))
        if self.R == 0:
            self.S = math.sqrt(self.L / ((self.R + 0.5) * (self.W - 0.5)))

        if (self.T - self.S) < self.B < (self.T + self.S):
            self.tomar_prueba()

        if (self.B - self.S) > self.T:
            self.preguntas = self.banco_preguntas
            return True

        if (self.B + self.S) > self.T:
            self.preguntas = self.banco_preguntas
            return False

    def seguir_prueba(self):
        pass

    def elegir_pregunta(self):
        dis_min = abs(self.D - self.preguntas[0].D)
        index = 0
        i = 0
        for pregunta in self.preguntas:
            if dis_min < abs(self.D - pregunta.D):
                dis_min = abs(self.D - pregunta.D)
                index = i
            i += 1
        pregunta_elegida = self.preguntas[index]
        del self.preguntas[index]
        self.D = pregunta_elegida.D
        return pregunta_elegida

    @staticmethod
    def hacer_pregunta(pregunta):
        print(pregunta.enunciado)
        opcion = input()
        while opcion not in pregunta.opciones:
            opcion = input()
        if opcion == pregunta.opcion_correcta:
            return True
        else:
            return False


class Pregunta:
    def __init__(self, enunciado, opciones, opcion_correcta, d):
        self.enunciado = enunciado
        self.opciones = opciones
        self.opcion_correcta = opcion_correcta
        self.D = d

    def __repr__(self):
        return f"pregunta de dificultad {self.D} de opción correcta {self.opcion_correcta} y " \
               f"enunciado:\n{self.enunciado}\n\n\n"

    def __str__(self):
        return f"pregunta de dificultad {self.D} de opción correcta {self.opcion_correcta} y " \
               f"enunciado:\n{self.enunciado} "

