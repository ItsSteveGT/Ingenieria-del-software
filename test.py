import unittest
from juego import validacion  # reemplaza 'tu_archivo' con el nombre real de tu archivo .py

class TestJuego(unittest.TestCase):

    def test_piedra_vs_tijera(self):
        self.assertEqual(validacion("piedra", "tijera"), 1)

    def test_piedra_vs_papel(self):
        self.assertEqual(validacion("piedra", "papel"), -1)

    def test_piedra_vs_piedra(self):
        self.assertEqual(validacion("piedra", "piedra"), 5)

    def test_papel_vs_piedra(self):
        self.assertEqual(validacion("papel", "piedra"), 1)

    def test_papel_vs_tijera(self):
        self.assertEqual(validacion("papel", "tijera"), -3)

    def test_papel_vs_papel(self):
        self.assertEqual(validacion("papel", "papel"), 0)

    def test_tijera_vs_papel(self):
        self.assertEqual(validacion("tijera", "papel"), 2)

    def test_tijera_vs_piedra(self):
        self.assertEqual(validacion("tijera", "piedra"), -1)

    def test_tijera_vs_tijera(self):
        self.assertEqual(validacion("tijera", "tijera"), 0)

if __name__ == "__main__":
    unittest.main()