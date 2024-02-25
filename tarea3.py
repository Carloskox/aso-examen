import os
def crear_carpetas_y_ficheros():
    escritorio = '/home/carlos/Escritorio'  # Ruta al escritorio

    # Iteramos 5 veces para crear 5 carpetas
    for i in range(1, 6):
        nombre_carpeta = f"folder{i}"
        ruta_carpeta = os.path.join(escritorio, nombre_carpeta)
        os.makedirs(ruta_carpeta, exist_ok=True)  # Creamos la carpeta
        
       # Dentro de cada carpeta, creamos 10 ficheros
        for j in range(1, 11):
            nombre_fichero = f"fichero{j}.txt"
            contenido = f"Este es el contenido del fichero {j}"
            ruta_fichero = os.path.join(ruta_carpeta, nombre_fichero)

            # Escribimos el contenido en el fichero
            with open(ruta_fichero, 'w') as f:
                f.write(contenido)

if __name__ == "__main__":
    crear_carpetas_y_ficheros() 
