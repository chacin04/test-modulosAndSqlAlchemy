import subprocess
import sys
import os

def deactivate_all_virtualenvs():
    # Obtener una lista de todos los entornos virtuales activos
    output = subprocess.check_output(['pip', 'list', '--format=columns']).decode(sys.stdout.encoding)
    envs = [line.split()[0] for line in output.split('\n')[2:] if line.strip()]

    # Desactivar cada entorno virtual
    for env in envs:
        # Si el entorno virtual tiene un script deactivate, ejecútalo
        deactivate_script = os.path.join(env, 'Scripts' if os.name == 'nt' else 'bin', 'deactivate')
        if os.path.exists(deactivate_script):
            subprocess.call([deactivate_script])
        else:
            print(f"No se pudo encontrar el script deactivate en el entorno virtual {env}")

if __name__ == "__main__":
    deactivate_all_virtualenvs()
