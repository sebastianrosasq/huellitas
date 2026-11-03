from collections.abc import Iterator
from dataclasses import dataclass, field

from .modelo import Rectangulo, Registro


@dataclass(slots=True)
class Nodo:
    region: Rectangulo
    profundidad: int
    registros: list[Registro] = field(default_factory=list)
    hijos: tuple["Nodo", ...] = ()

    @property
    def es_hoja(self) -> bool:
        return not self.hijos


class QuadTree:
    def __init__(
        self, region: Rectangulo, capacidad: int = 4, profundidad_maxima: int = 12
    ) -> None:
        if capacidad < 1 or profundidad_maxima < 0:
            raise ValueError("La capacidad debe ser positiva y la profundidad no negativa.")
        self.raiz = Nodo(region, profundidad=0)
        self.capacidad = capacidad
        self.profundidad_maxima = profundidad_maxima
        self._cantidad = 0

    def __len__(self) -> int:
        return self._cantidad

    def insertar(self, registro: Registro) -> bool:
        if not self.raiz.region.contiene(registro.posicion):
            return False
        self._insertar_en_nodo(self.raiz, registro)
        self._cantidad += 1
        return True

    def _insertar_en_nodo(self, nodo: Nodo, registro: Registro) -> None:
        if nodo.hijos:
            self._insertar_en_hijo(nodo, registro)
        elif (
            len(nodo.registros) < self.capacidad
            or nodo.profundidad >= self.profundidad_maxima
        ):
            nodo.registros.append(registro)
        else:
            self._subdividir(nodo)
            self._insertar_en_hijo(nodo, registro)

    def _insertar_en_hijo(self, nodo: Nodo, registro: Registro) -> None:
        for hijo in nodo.hijos:
            if hijo.region.contiene(registro.posicion):
                self._insertar_en_nodo(hijo, registro)
                return
        raise RuntimeError("El punto no pertenece a ninguno de los cuadrantes.")

    def _subdividir(self, nodo: Nodo) -> None:
        region = nodo.region
        mitad_ancho = region.ancho / 2
        mitad_alto = region.alto / 2
        x, y = region.izquierda, region.superior
        profundidad = nodo.profundidad + 1
        nodo.hijos = (
            Nodo(Rectangulo(x, y, mitad_ancho, mitad_alto), profundidad),
            Nodo(Rectangulo(x + mitad_ancho, y, mitad_ancho, mitad_alto), profundidad),
            Nodo(Rectangulo(x, y + mitad_alto, mitad_ancho, mitad_alto), profundidad),
            Nodo(Rectangulo(x + mitad_ancho, y + mitad_alto, mitad_ancho, mitad_alto), profundidad),
        )
        registros_anteriores = nodo.registros
        nodo.registros = []
        for registro in registros_anteriores:
            self._insertar_en_hijo(nodo, registro)

    def recorrer_nodos(self) -> Iterator[Nodo]:
        yield from self._recorrer_desde(self.raiz)

    def _recorrer_desde(self, nodo: Nodo) -> Iterator[Nodo]:
        yield nodo
        for hijo in nodo.hijos:
            yield from self._recorrer_desde(hijo)
