import unittest

from huellitas.modelo import Categoria, Punto, Rectangulo
from huellitas.servicio import ServicioHuellitas


class PruebasServicio(unittest.TestCase):
    def setUp(self) -> None:
        self.servicio = ServicioHuellitas(Rectangulo(0, 0, 100, 100))

    def test_registro_valido_y_reinicio(self) -> None:
        registro = self.servicio.registrar(Categoria.REFUGIO, "  Refugio  ", Punto(10, 20))
        self.assertEqual(registro.descripcion, "Refugio")
        self.assertEqual(len(self.servicio.arbol), 1)
        self.servicio.reiniciar()
        self.assertEqual(self.servicio.registros, [])
        self.assertEqual(len(self.servicio.arbol), 0)

    def test_error_no_modifica_el_estado(self) -> None:
        with self.assertRaises(ValueError):
            self.servicio.registrar(Categoria.REFUGIO, "  ", Punto(10, 20))
        with self.assertRaises(ValueError):
            self.servicio.registrar(Categoria.REFUGIO, "Refugio", Punto(100, 20))
        self.assertEqual(len(self.servicio.arbol), 0)
        self.assertEqual(self.servicio.registros, [])
        self.assertEqual(self.servicio.registrar(Categoria.REFUGIO, "A", Punto(1, 1)).identificador, 1)


if __name__ == "__main__":
    unittest.main()
