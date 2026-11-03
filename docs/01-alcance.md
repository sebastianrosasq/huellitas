# Alcance del proyecto

Huellitas es una aplicación en Python para representar información sobre mascotas perdidas en un mapa simulado. Cada punto puede ser una mascota perdida, un avistamiento o un refugio.

La idea es usar un QuadTree para organizar esos puntos y, más adelante, seleccionar una zona del mapa y ver cuáles se encuentran dentro. Las divisiones también se muestran en pantalla para que sea más fácil entender cómo funciona el árbol.

## Lo que ya funciona

- Agregar puntos con una categoría y una descripción.
- Dividir una región en cuatro cuando supera su capacidad.
- Mostrar u ocultar las divisiones del árbol.
- Cargar un ejemplo y limpiar el mapa.

## Lo que falta

- Buscar los puntos que se encuentran dentro de una zona seleccionada.
- Probar esa búsqueda y completar la revisión del programa.
- Evaluar si se agregan las opciones de deshacer y recorrer el árbol por niveles.
- Completar el informe y grabar el video para la entrega final.

## Temas del curso

El proyecto utiliza árboles y recursión para dividir el mapa e insertar puntos. También usa listas para guardar los registros de cada región. La idea de deshacer puede trabajarse con una pila; un recorrido por niveles podría usar una cola.

## Límites del proyecto

El mapa es ficticio y los datos se guardan solo durante la sesión. No se están usando mapas reales, cuentas de usuario ni datos compartidos por internet. Un avistamiento es un registro de prueba y no confirma por sí solo que se haya encontrado una mascota.

El trabajo es individual. Según la indicación del curso, el proyecto final debe incluir un QuadTree con interfaz gráfica, un informe en PDF y un video con la explicación y demostración.
