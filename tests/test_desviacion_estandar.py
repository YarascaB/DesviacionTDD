import unittest
from src.logica.desviacion_estandar import DesviacionEstandar

class TestDesviacionEstandar(unittest.TestCase):

    def test_lista_vacia(self):
        with self.assertRaises(ValueError):
            DesviacionEstandar.calcular([])

    # Otros tests...

if __name__ == "__main__":
    unittest.main()
