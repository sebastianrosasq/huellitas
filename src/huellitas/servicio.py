from .modelo import Categoria, Punto, Rectangulo, Registro
from .quadtree import QuadTree


class ServicioHuellitas:
    def __init__(self, region: Rectangulo, capacidad: int = 4) -> None:
        self.region = region
        self.capacidad = capacidad
        self.reiniciar()

    def reiniciar(self) -> None:
        self.arbol = QuadTree(self.region, self.capacidad)
        self.registros: list[Registro] = []
        self._siguiente_id = 1

    def registrar(self, categoria: Categoria, descripcion: str, punto: Punto) -> Registro:
        registro = Registro(self._siguiente_id, categoria, descripcion, punto)
        if not self.arbol.insertar(registro):
            raise ValueError("El punto debe estar dentro del mapa.")
        self.registros.append(registro)
        self._siguiente_id += 1
        return registro
