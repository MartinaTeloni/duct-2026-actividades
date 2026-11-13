from analizador import contar_frecuencias

def test_basico(tmp_path):
    archivo = tmp_path / "entrada.txt"
    archivo.write_text("sol luna sol estrella", encoding="utf-8")

    resultado = contar_frecuencias(str(archivo))
    assert resultado == {"sol": 2, "luna": 1, "estrella": 1}

def test_texto_vacio(tmp_path):
    archivo = tmp_path / "vacio.txt"
    archivo.write_text("", encoding="utf-8")
    resultado = contar_frecuencias(str(archivo))
    assert resultado == {}


def test_mayusculas_y_minusculas(tmp_path):
    archivo = tmp_path / "mayusculas.txt"
    archivo.write_text("luna Luna LUNA", encoding="utf-8")
    resultado = contar_frecuencias(str(archivo))
    assert resultado == {"luna": 3}