import unittest
from core.funciones import calcular_propiedades_funcion

class TestFunciones(unittest.TestCase):
    def test_dominio_lineal(self):
        funcion = lambda x: 2 * x + 1
        propiedades = calcular_propiedades_funcion(funcion, "Lineal")
        self.assertEqual(propiedades["Dominio"], "(-∞, ∞)")

if __name__ == "__main__":
    unittest.main()