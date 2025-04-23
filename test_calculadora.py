import pytest
from calculadora import Calculadora, OperacionesAvanzadas


@pytest.fixture
def calculadora():
    return Calculadora()


@pytest.fixture
def operaciones_avanzadas():
    return OperacionesAvanzadas()


def test_suma(calculadora):
    assert calculadora.suma(2, 3) == 5


def test_resta(calculadora):
    assert calculadora.resta(5, 3) == 2


def test_multiplicacion(calculadora):
    assert calculadora.multiplicacion(2, 3) == 6


def test_division(calculadora):
    assert calculadora.division(6, 2) == 3


def test_division_por_cero(calculadora):
    with pytest.raises(ValueError):
        calculadora.division(6, 0)


def test_potencia(operaciones_avanzadas):
    assert operaciones_avanzadas.potencia(2, 3) == 8


def test_raiz_cuadrada(operaciones_avanzadas):
    assert operaciones_avanzadas.raiz_cuadrada(9) == 3


def test_raiz_cuadrada_negativa(operaciones_avanzadas):
    with pytest.raises(ValueError):
        operaciones_avanzadas.raiz_cuadrada(-9)
