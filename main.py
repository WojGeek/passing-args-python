"""Pasando argumentos desde consola - Python"""

import argparse


def accept_params():
    """Recibe parámetros de origen y destino"""
    parser = argparse.ArgumentParser(description="Respaldo-sincronización de archivos")

    parser.add_argument("origen", help="Ruta del directorio origen", type=str)
    parser.add_argument("destino", help="Ruta de disco destino", type=str)
    parser.add_argument(
        "-test", help="Ejecutar sin realizar cambios", action="store_true"
    )
    parser.add_argument("-verbose", help="Muestra el progreso", action="store_true")

    args = parser.parse_args()

    
    return args.origen, args.destino, args.test, args.verbose


if __name__ == "__main__":
    source_path, destination_path, mode, verbosity = accept_params()
    print(type(source_path))
    print(type(destination_path))
    print(type(mode))
    print(type(verbosity))
    
    # print(args.origen)
    # print(args.destino)
    # # print(args.v)
    # # print(args.t)

    # print("Verbosity turned on", args.verbose)

    # print("Modo: prueba", args.test)
