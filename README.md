## Crear entorno virtual
python -m venv venv

## actualizar pip
pip install --upgrade pip

# Instalar paquetes necesarios
# ipdb permite pausar la ejecucion del codigo para evitar el uso de print
pip install ipdb

## Ejecutar pruebas unitarias
python -m unittest
python -m unittest tests/test-calculator.py 

# Le estoy indicando la carpeta en la que estan las pruebas que debe ejecutar
python -m unittest discover -s test