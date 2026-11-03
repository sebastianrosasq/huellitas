import unittest

from huellitas.modelo import Categoria, Punto, Rectangulo, Registro
from huellitas.quadtree import QuadTree


def registro(numero: int, x: float, y: float) -> Registro:
    return Registro(numero, Categoria.AVISTAMIENTO, f"Punto {numero}", Punto(x, y))


def registros_del_arbol(arbol: QuadTree) -> list[Registro]:
    return [registro for nodo in arbol.recorrer_nodos() for registro in nodo.registros]


class PruebasQuadTree(unittest.TestCase):
    def setUp(self) -> None:
        self.arbol = QuadTree(Rectangulo(0, 0, 100, 100), capacidad=2, profundidad_maxima=6)

    def test_subdivision_conserva_los_registros_una_sola_vez(self) -> None:
        puntos = [registro(1, 10, 10), registro(2, 75, 10), registro(3, 10, 75)]
        for punto in puntos:
            self.assertTrue(self.arbol.insertar(punto))
        self.assertEqual(len(self.arbol.raiz.hijos), 4)
        self.assertCountEqual(registros_del_arbol(self.arbol), puntos)
        self.assertEqual(len(self.arbol), 3)

    def test_rechaza_puntos_fuera_y_en_borde_abierto(self) -> None:
        for x, y in [(-1, 10), (100, 0), (0, 100), (101, 101)]:
            self.assertFalse(self.arbol.insertar(registro(1, x, y)))
        self.assertEqual(len(self.arbol), 0)

    def test_lineas_divisorias_asignan_un_solo_hijo(self) -> None:
        puntos = [registro(1, 0, 0), registro(2, 50, 0), registro(3, 0, 50), registro(4, 50, 50)]
        for punto in puntos:
            self.arbol.insertar(punto)
        self.assertCountEqual(registros_del_arbol(self.arbol), puntos)
        self.assertEqual([len(hijo.registros) for hijo in self.arbol.raiz.hijos], [1, 1, 1, 1])

    def test_coordenadas_identicas_terminan_en_profundidad_maxima(self) -> None:
        puntos = [registro(i, 25, 25) for i in range(1, 21)]
        for punto in puntos:
            self.arbol.insertar(punto)
        self.assertCountEqual(registros_del_arbol(self.arbol), puntos)
        self.assertEqual(max(n.profundidad for n in self.arbol.recorrer_nodos()), 6)

    def test_configuracion_invalida(self) -> None:
        with self.assertRaises(ValueError):
            QuadTree(Rectangulo(0, 0, 1, 1), capacidad=0)
        with self.assertRaises(ValueError):
            QuadTree(Rectangulo(0, 0, 1, 1), profundidad_maxima=-1)


if __name__ == "__main__":
    unittest.main()
