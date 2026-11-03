# Cómo está organizado el código

El programa separa el QuadTree de la interfaz. Así se puede probar cómo se insertan los puntos sin necesidad de abrir la ventana.

```text
src/huellitas/
├── __main__.py   # Abre el programa
├── modelo.py     # Punto, rectángulo, categoría y registro
├── quadtree.py   # Nodos, inserción y subdivisión
├── servicio.py   # Registro de puntos y reinicio
└── interfaz.py   # Ventana, mapa, botones y clics
```

Las pruebas se encuentran en `tests/`, las capturas en `evidencias/` y el informe en `informes/`.

## Cómo se agrega un punto

1. Se elige una categoría y se escribe una descripción.
2. Al hacer clic en el mapa, la interfaz envía la posición y los datos al servicio.
3. El servicio crea el registro y lo inserta en el QuadTree.
4. El mapa se vuelve a dibujar con el punto y las divisiones correspondientes.

## Cómo funciona el QuadTree

El árbol comienza con una región que representa todo el mapa. Cada región puede guardar cuatro puntos. Cuando necesita recibir otro, se divide en cuatro cuadrantes y reparte sus puntos entre ellos. Una región hija también puede dividirse si vuelve a llenarse.

Para que un punto sobre una línea divisoria no se guarde dos veces, cada cuadrante incluye sus límites iniciales y excluye los finales. El árbol también tiene una profundidad máxima: así puede trabajar con varios puntos en la misma ubicación sin dividirse indefinidamente.

La búsqueda dentro de una zona todavía está pendiente. La idea es revisar solo las regiones que se cruzan con el área seleccionada.

## Datos durante la sesión

Los registros se mantienen en memoria mientras el programa está abierto. Al cerrarlo, se pierden; por ahora no existe una opción para guardarlos en un archivo.
