import subprocess

def execute_python_script(script_file):
    try:
        subprocess.run(['python', script_file], check=True)
        print(f"Ejecutado correctamente el script '{script_file}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script '{script_file}': {e}")

try:
    # Ejecutar los scripts en orden secuencial
    scripts = ['CrimeData.py', 'extraccion.py', 'cargaDim.py', 'cargaFact.py']
    
    for script_file in scripts:
        execute_python_script(script_file)

except Exception as e:
    print(f"Error general: {str(e)}")

print("Proceso completado.")
