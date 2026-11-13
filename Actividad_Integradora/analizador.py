import matplotlib.pyplot as plt


def contar_frecuencias(ruta):
    """
    Lee un archivo de texto y devuelve un diccionario con la
    frecuencia de cada palabra. Si el archivo no existe, devuelve None.

    Parametros:
        ruta (str): ruta al archivo de texto a analizar

    Retorna:
        dict o None: pares {palabra: frecuencia}
    """
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            texto = archivo.read()
    except FileNotFoundError:
        print(f"Error: no se encontro el archivo '{ruta}'.")
        return None

    palabras_texto = texto.lower().split()

    STOP_WORDS = {
        "de", "la", "el", "y", "a", "en", "que", "los", "las",
        "un", "una", "se", "pero", "mi", "o", "es", "con", "por",
        "para", "del", "no", "su", "al", "lo"
    }

    frecuencias = {}
    for palabra in palabras_texto:
        if palabra not in STOP_WORDS:
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    return frecuencias

def graficar_frecuencias(frecuencias, top_n=10):
    """
    Genera y guarda un grafico de barras con las top_n
    palabras mas frecuentes.

    Parametros:
        frecuencias (dict): diccionario {palabra: frecuencia}
        top_n (int): cantidad de palabras a graficar
    """
    top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:top_n]

    palabras = [par[0] for par in top10]
    valores = [par[1] for par in top10]

    plt.figure(figsize=(10, 6))
    plt.bar(palabras[::-1], valores[::-1], color="steelblue")
    plt.title(f"Top {top_n} palabras mas frecuentes")
    plt.xlabel("Palabras")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.savefig("grafico_frecuencias.png", dpi=150, bbox_inches="tight")
    plt.show()


def main():
    frecuencias = contar_frecuencias("texto_integradora.txt")

    if frecuencias is not None:
        print(f"Cantidad de palabras totales: {sum(frecuencias.values())}")
        print(f"Cantidad de palabras distintas: {len(frecuencias)}")
        print("\nLas 10 palabras mas frecuentes:")

        top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:10]
        for palabra, frecuencia in top10:
            print(f"  {palabra}: {frecuencia}")

        graficar_frecuencias(frecuencias)


if __name__ == "__main__":
    main()