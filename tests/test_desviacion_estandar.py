import unittest
from src.logica.desviacion_estandar import DesviacionEstandar

class TestDesviacionEstandar(unittest.TestCase):

    def test_lista_vacia(self):
        with self.assertRaises(ValueError):
            DesviacionEstandar.calcular([])  # Se espera que se lance una excepción

    def test_un_dato(self):
        resultado = DesviacionEstandar.calcular([5])  # Solo un dato
        self.assertAlmostEqual(resultado, 0.0)  # La desviación estándar debe ser 0.0

    # Otros tests...

if __name__ == "__main__":
    unittest.main()
