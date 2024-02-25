import psutil

def obtener_porcentaje_uso():
    particiones = psutil.disk_partitions()
 
    # Iteramos sobre cada partición
    for particion in particiones:
        try:
            # Obtenemos el espacio utilizado en la partición
            espacio = psutil.disk_usage(particion.mountpoint)
            # Calculamos el porcentaje de espacio ocupado en la partición
            porcentaje = espacio.percent
            # Mostramos el nombre de la partición y el porcentaje de espacio ocupado
            print(f"{particion.device} {porcentaje:.1f}%")
        except PermissionError:
            # Ignoramos las particiones a las que no tenemos permiso de acceder
            continue

# Si el script es ejecutado directamente, llamamos a la función para obtener el porcentaje de uso

if __name__ == "__main__":

    obtener_porcentaje_uso() 
