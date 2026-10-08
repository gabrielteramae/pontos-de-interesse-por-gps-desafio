import unittest
from types import SimpleNamespace
from app.proximity import euclidean_distance, filter_by_proximity

class ProximityTest(unittest.TestCase):
    def test_distancia_do_triangulo_3_4_5(self):
        self.assertEqual(euclidean_distance(0, 0, 3, 4), 5)

    def test_filtra_quem_esta_longe(self):
        perto = SimpleNamespace(x=1, y=1)
        longe = SimpleNamespace(x=100, y=100)
        escolhidos = filter_by_proximity([perto, longe], 0, 0, 5)
        self.assertEqual(escolhidos, [perto])

if __name__ == "__main__":
    unittest.main()
