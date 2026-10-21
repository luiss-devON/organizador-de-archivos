from pathlib import Path
import shutil

# 1. La carpeta que vamos a ordenar
carpeta = Path("desorden")

# 2. Qué tipo de archivo va a qué carpeta
tipos = {
    ".jpg": "Imagenes",
    ".png": "Imagenes",
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".txt": "Documentos",
    ".pptx": "Presentaciones",
    ".ppt": "Presentaciones",
    ".xlsx": "Excel",
    ".xls": "Excel",
    ".csv": "Excel",
    ".mp3": "Audio",
    ".mp4": "Videos",
}

# 3. Revisar cada archivo y moverlo
for archivo in carpeta.iterdir():
    if archivo.is_file():
        destino = tipos.get(archivo.suffix.lower(), "Otros")
        (carpeta / destino).mkdir(exist_ok=True)
        shutil.move(str(archivo), str(carpeta / destino / archivo.name))
        print(f"{archivo.name} -> {destino}")