import pickle

def guardar_datos(objeto, archivo):
    with open(archivo, "wb") as f:
        pickle.dump(objeto, f)
    print(" Datos guardados exitosamente")

def cargar_datos(archivo):
    try:
        with open(archivo, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("⚠No hay datos almacenados todavía")
        return None

