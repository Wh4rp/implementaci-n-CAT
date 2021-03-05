from algoritmo import TestCAT, Pregunta
import lorem


class TestPropio(TestCAT):
    def __init__(self, problemas, t):
        super().__init__(problemas, t)

    def seguir_prueba(self):
        if self.L == 10:
            return False
        else:
            return True


if __name__ == '__main__':
    preguntas = [Pregunta(lorem.sentence(), ["a", "b", "c"], "abc"[i % 3], i) for i in range(20)]
    test = TestPropio(preguntas, 5)
    # print(preguntas)
    if test.tomar_prueba():
        print("APROBASTE")
    else:
        print("REPROBASTE")
