# Pruebas

El primer avance tiene siete pruebas automatizadas. Para ejecutarlas en PowerShell, desde la carpeta del proyecto:

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```

## Lo que se ha probado

- Que los puntos se conserven cuando una región se divide.
- Que no se acepten puntos fuera del mapa.
- Que un punto sobre una línea divisoria quede en un solo cuadrante.
- Que se puedan agregar varios puntos en la misma ubicación.
- Que el programa rechace datos inválidos y que el reinicio limpie los registros.

En la ventana también probé agregar puntos con clic, cargar el ejemplo, ocultar las divisiones y limpiar el mapa.

## Pruebas pendientes

Cuando agregue la búsqueda por zona, probaré que encuentre los puntos correctos, no repita resultados y funcione con zonas vacías o situadas en los bordes del mapa.
