import os
arch="Archivo.txt"
if os.path.exists(arch):
    os.remove(arch)
    print(f'Archivo {arch} eliminado')
else:
    print(f'{arch} no existe')