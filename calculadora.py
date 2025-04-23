class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b


class OperacionesAvanzadas(Calculadora):
    def potencia(self, a, b):
        return a ** b

    def raiz_cuadrada(self, a):
        if a < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        return a ** 0.5