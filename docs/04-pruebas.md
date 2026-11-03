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

También se revisaron en la ventana la inserción con clic, el ejemplo, la opción para ocultar las divisiones y la limpieza del mapa.

## Pruebas pendientes

Cuando se implemente la búsqueda por zona, se comprobará que encuentre los puntos correctos, que no repita resultados y que funcione con zonas vacías o que estén en los bordes del mapa.
