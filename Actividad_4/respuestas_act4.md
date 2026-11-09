ENLACE REPOSITORIO: https://github.com/MartinaTeloni/duct-2026-actividades.git 

# ¿Qué pasaría con test_frecuencias_mayusculas si en analizador.py sacaras el .lower()?
Sacar el .lower() implicaría que una palabra escrita con diferencias en mayúsculas o minúsculas (como Sol y sol) no se analizará como la misma. En cambio, se analizarían como palabras distintas y se contarán por separado. 
Al probarlo, se marca un AssertionError que indica que el diccionario obtenido contiene tres claves separadas ('Sol', 'sol', 'SOL'), contando 1 frecuencia para cada una, en lugar de una sola clave 'sol' con un conteo de frecuencias 3. 

# ¿Por qué contar_frecuencias recibe un string directamente en vez de una ruta de archivo, como en la Clase 2? 
contar_frecuencias recibe un string directamente para aplicar la separación de responsabilidades, ya que la función solo cuenta las frecuencias de las palabras en un texto ya leído anteriormente. Esto facilita la realización de pruebas en test_analizador.py al permitir evaluar múltiples casos (cadenas vacías, mayúsculas, espacios, puntuación) de forma aislada e instantánea, sin la necesidad de usar archivos externos.

Para la cuarta prueba, el caso borde elegido tiene que ver con espacios en blanco de más, tabulaciones y saltos de línea. La función actual lo resuelve debido a que el método .split() divide las palabras e ignora los espacios en blanco contiguos. Entonces, la función pasaría esta prueba. 