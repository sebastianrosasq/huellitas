from dataclasses import dataclass
from enum import Enum
from math import isfinite


class Categoria(str, Enum):
    MASCOTA_PERDIDA = "Mascota perdida"
    AVISTAMIENTO = "Avistamiento"
    REFUGIO = "Refugio"


@dataclass(frozen=True, slots=True)
class Punto:
    x: float
    y: float

    def __post_init__(self) -> None:
        if not isfinite(self.x) or not isfinite(self.y):
            raise ValueError("Las coordenadas deben ser números finitos.")


@dataclass(frozen=True, slots=True)
class Rectangulo:
    izquierda: float
    superior: float
    ancho: float
    alto: float

    def __post_init__(self) -> None:
        valores = (self.izquierda, self.superior, self.ancho, self.alto)
        if not all(isfinite(valor) for valor in valores):
            raise ValueError("Los límites deben ser números finitos.")
        if self.ancho <= 0 or self.alto <= 0:
            raise ValueError("El ancho y el alto deben ser positivos.")

    def contiene(self, punto: Punto) -> bool:
        return (
            self.izquierda <= punto.x < self.izquierda + self.ancho
            and self.superior <= punto.y < self.superior + self.alto
        )


@dataclass(frozen=True, slots=True)
class Registro:
    identificador: int
    categoria: Categoria
    descripcion: str
    posicion: Punto

    def __post_init__(self) -> None:
        if self.identificador < 1:
            raise ValueError("El identificador debe ser positivo.")
        if not isinstance(self.categoria, Categoria):
            raise ValueError("La categoría no es válida.")
        descripcion = self.descripcion.strip()
        if not descripcion:
            raise ValueError("Escribe un nombre o una descripción.")
        object.__setattr__(self, "descripcion", descripcion)
