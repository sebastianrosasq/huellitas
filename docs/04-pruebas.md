# Pruebas

El proyecto tiene siete pruebas automatizadas. En Visual Studio Code puedes abrir la sección **Pruebas** y ejecutarlas desde allí, o usar la terminal en la carpeta del proyecto:

```powershell
python -m unittest discover -s tests -v
```

## Lo que se ha probado

- Que los puntos se conserven cuando una región se divide.
- Que no se acepten puntos fuera del mapa.
- Que un punto sobre una línea divisoria quede en un solo cuadrante.
- Que se puedan agregar varios puntos en la misma ubicación.
- Que el programa rechace datos inválidos y que el reinicio limpie los registros.

Las siete pruebas pasaron tanto desde la terminal como desde el panel de pruebas de Visual Studio Code, la [captura del resultado](../evidencias/06-vscode-pruebas.jpg) muestra el contador 7/7 y la salida con OK.

## Pruebas en la interfaz

| Acción | Resultado |
| --- | --- |
| Agregar cuatro registros desde el formulario y el mapa | Aparecen los cuatro puntos y la región sigue sin dividirse |
| Agregar el quinto registro | Aparecen los cuatro cuadrantes y se conservan los cinco puntos |
| Ocultar las divisiones | Las líneas desaparecen y los puntos se mantienen |
| Cargar el ejemplo | El mapa muestra ocho registros de las tres categorías |
| Limpiar el mapa | Desaparecen los puntos y las divisiones, el contador queda en cero |

Las [capturas del informe](05-informe.md) muestran la comparación de cuatro y cinco registros, el ejemplo y el resultado de las pruebas del código.

## Pruebas pendientes

Cuando agregue la búsqueda por zona, probaré que encuentre los puntos correctos, no repita resultados y funcione con zonas vacías o situadas en los bordes del mapa.
