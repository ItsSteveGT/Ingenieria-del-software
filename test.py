import unittest
from juego import validacion

class TestJuego(unittest.TestCase):

    def test_piedra_vs_tijera(self):
        self.assertEqual(validacion("piedra", "tijera"), 1)

    def test_piedra_vs_papel(self):
        self.assertEqual(validacion("piedra", "papel"), -1)

    def test_piedra_vs_piedra(self):
        self.assertEqual(validacion("piedra", "piedra"), 0)

    def test_papel_vs_piedra(self):
        self.assertEqual(validacion("papel", "piedra"), 1)

    def test_papel_vs_tijera(self):
        self.assertEqual(validacion("pelota", "tijera"), -1)

    def test_papel_vs_papel(self):
        self.assertEqual(validacion("papel", "papel"), 0)

    def test_tijera_vs_papel(self):
        self.assertEqual(validacion("tijera", "papel"), 1)

    def test_tijera_vs_piedra(self):
        self.assertEqual(validacion("tijera", "piedra"), -1)

    def test_tijera_vs_tijera(self):
        self.assertEqual(validacion("tijera", "tijera"), 0)

if __name__ == "__main__":
    unittest.main()