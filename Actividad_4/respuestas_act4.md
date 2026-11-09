ENLACE REPOSITORIO: 

¿Qué pasaría con test_frecuencias_mayusculas si en analizador.py sacaras el .lower()?
Sacar el .lower() implicaría que la misma palabra escrita con diferencias en mayúsculas o minúsculas (como Sol y sol) no se analizará como la misma. En cambio, Sol y sol se analizarían como palabras distintas y se contarán por separado. 
Al probarlo, se marca un AssertionError que indica que el diccionario obtenido contiene tres claves separadas ('Sol', 'sol', 'SOL') con frecuencia 1 cada una, en lugar de una sola clave 'sol' con frecuencia 3. 

¿Por qué contar_frecuencias recibe un string directamente en vez de una ruta de archivo, como en la Clase 2? 
Recibir un string directamente aplica la separación de responsabilidades: la función solo procesa el texto. Esto facilita la realización de pruebas en test_analizador.py, ya que permite evaluar múltiples casos (cadenas vacías, mayúsculas, espacios) de forma aislada e instantánea, sin depender del sistema de archivos ni crear archivos .txt auxiliares en disco.

Para la cuarta prueba, el caso borde elegido tiene que ver con múltiples espacios en blanco, tabulaciones y saltos de línea. La función actual lo resuelve correctamente debido a que el método .split() de Python sin argumentos ignora automáticamente cualquier secuencia de espacios en blanco contiguos.