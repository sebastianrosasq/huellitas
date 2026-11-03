# Proyecto Huellitas 🐾

Huellitas es un proyecto en Python que usa un **QuadTree** para organizar información sobre mascotas perdidas en un mapa simulado.

La idea es poder registrar mascotas, avistamientos y refugios, y buscar después qué puntos se encuentran dentro de una zona del mapa. El proyecto es individual y se desarrolla para el curso de Estructura de Datos y Algoritmos de Tecsup.

## ¿Cómo funciona?

El mapa comienza como una sola región que puede guardar hasta cuatro puntos. Cuando se agrega otro punto, la región se divide en cuatro cuadrantes y los registros se reparten entre ellos. Si un cuadrante también se llena, puede volver a dividirse.

El programa ya permite agregar puntos, ver las divisiones del árbol, cargar un ejemplo y limpiar el mapa. La selección de una zona y la búsqueda de sus registros todavía están en desarrollo.

Los datos de ejemplo son ficticios y se mantienen mientras el programa está abierto. Las opciones **Cargar ejemplo** y **Limpiar mapa** reemplazan los puntos de la sesión.

## Usar el proyecto en Visual Studio Code

Se necesita Python 3.10 o una versión posterior, Tkinter y un entorno gráfico. El programa usa la biblioteca estándar de Python.

1. Abre Visual Studio Code y elige **Archivo → Abrir carpeta**, luego selecciona la carpeta del proyecto.
2. Instala las extensiones recomendadas de Python y Python Debugger si Visual Studio Code te lo solicita.
3. Abre la paleta de comandos con `Ctrl+Shift+P`, busca **Python: Select Interpreter** y selecciona Python 3.10 o posterior.
4. Presiona `F5` y elige **Ejecutar Huellitas** si aparece la lista de configuraciones.
5. En la ventana, elige una categoría, escribe una descripción y haz clic en el mapa. También puedes cargar un ejemplo para probar el programa.

También puedes abrir la terminal de Visual Studio Code y ejecutar:

```powershell
python -m src.huellitas
```

Si la ventana no abre, puedes usar `python -m tkinter` para ver si Tkinter está disponible.

## Pruebas

En Visual Studio Code, abre la sección **Pruebas** y ejecuta las pruebas que aparecen en la lista. También puedes usar la terminal desde la carpeta del proyecto:

```powershell
python -m unittest discover -s tests -v
```

Las pruebas revisan la inserción de puntos, las divisiones, los límites del mapa, las posiciones repetidas y el reinicio.

## Estructura del proyecto

```text
proyecto-huellitas/
├── src/huellitas/   # Aplicación y QuadTree
├── tests/           # Pruebas
├── .vscode/         # Ejecución y pruebas en Visual Studio Code
├── docs/            # Alcance, estructura y plan
├── evidencias/      # Capturas del programa y del código
└── informes/        # Informes del proyecto
```

En [docs](docs/01-alcance.md) se explica el alcance del proyecto y en [informes](informes/primer-avance-huellitas.pdf) se encuentra el informe presentado hasta ahora.

**Autor:** Pernel Sebastian Rosas Quispe.
