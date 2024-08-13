Blackjack Game in Python
Descripción
Este es un simple juego de Blackjack implementado en Python. El juego se juega entre un jugador y el dealer (crupier). El objetivo es que el jugador obtenga una mano de cartas con un valor total lo más cercano posible a 21 sin pasarse.

Reglas del Juego
Las cartas numeradas (del 2 al 10) tienen su valor nominal.
Las cartas de figuras (J, Q, K) valen 10 puntos cada una.
Los Ases (A) pueden valer 1 u 11 puntos, dependiendo de cuál valor beneficie más al total de la mano sin exceder 21.
El jugador comienza con dos cartas visibles.
El dealer también comienza con dos cartas, pero solo una de ellas es visible para el jugador.
El jugador tiene la opción de "quedarse" (mantener su mano) o "pedir" (tomar otra carta) para intentar acercarse a 21.
Si el jugador o el dealer alcanzan exactamente 21 puntos con las dos primeras cartas, es un "Blackjack" y ganan automáticamente, a menos que ambos tengan 21, en cuyo caso es un empate.
Si el jugador supera los 21 puntos, "se pasa" y pierde automáticamente.
El dealer debe seguir pidiendo cartas hasta que su mano valga al menos 17 puntos.
El que tenga la mano más cercana a 21 puntos sin pasarse gana.
Requisitos
Python 3.x
Cómo Jugar
Clona este repositorio o descarga los archivos.

Ejecuta el script blackjack.py en tu entorno Python.

bash
Copiar código
python blackjack.py
Sigue las instrucciones en pantalla. Se te pedirá que elijas entre "1" para quedarte o "2" para pedir una carta adicional.

El juego continuará hasta que se determine un ganador o perdedor.

Estructura del Código
dealCards(turn): Distribuye una carta aleatoria a la mano especificada.
total(turn): Calcula el valor total de una mano, teniendo en cuenta los valores de las cartas y la flexibilidad del As.
revealDealerHand(): Revela la primera carta de la mano del dealer.
Bucle del juego: Controla el flujo del juego, desde la distribución inicial de cartas hasta la determinación del ganador.
Manejo de Errores
El juego incluye una validación de entrada para evitar que se bloquee si el usuario ingresa una opción no válida. Si el usuario ingresa algo distinto de "1" o "2", se le pedirá que lo intente de nuevo hasta que se ingrese una opción válida.

Futuras Mejoras
Implementar una interfaz gráfica de usuario (GUI) para hacer el juego más interactivo.
Añadir la opción de jugar varias rondas con un sistema de apuestas.
Mejorar la lógica del dealer para seguir las reglas de la casa de manera más realista.
Contribuciones
Las contribuciones son bienvenidas. Si tienes ideas para mejorar este proyecto, siéntete libre de hacer un fork del repositorio y enviar un pull request.
