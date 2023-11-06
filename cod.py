import os

# Obtén la variable de entorno del usuario actual
home = os.path.expanduser("~")

# Ruta completa a la carpeta de descargas
ruta_descargas = os.path.join(home, "Donwloads")

# Verifica si la carpeta de descargas existe
if os.path.exists(ruta_descargas):
    print(f"La carpeta de descargas se encuentra en: {ruta_descargas}")
else:
    print("La carpeta de descargas no se encontró en esta ubicación.")