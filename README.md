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
python -m unittest -v tests/test-calculator.py 

# Le estoy indicando la carpeta en la que estan las pruebas que debe ejecutar
python -m unittest discover -v -s test

# para configurar los test desde vscode
pip install pytest

# libreria para usar api
pip install requests

# ejecutar prueba por linea de comandos
python -m unittest tests.test_api_client

python3 -m unittest tests.test_api_client.ApiClientTests.test_get_location_returns_side_effect

# para hacer una pausa en la ejecución, se pued eusar ipdb:

    import ipdb 
    ipdb.set_trace()

## por ejemplo en el codigo se colocó en la seccion de codigo siguiente:
 def get_location(ip):
    url = f'https://freeipapi.com/api/json/{ip}'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    import ipdb 
    ipdb.set_trace()
    return {
        "country":data["countryName"],
        "region": data["regionName"],
        "city": data["cityName"]
    } 






## cuando se ejecute el método se pausa la ejecución y aparece un prompt en el que podriamos colocar el 
## nombre de la varibale, en este caso data, y nos muestra el contenido de la variable:

{
    "ipVersion": 4,
    "ipAddress": "8.8.8.8",
    "latitude": 37.386051,
    "longitude": -122.083847,
    "countryName": "United States of America",
    "countryCode": "US",
    "timeZone": "-07:00",
...
}

## Side effects

Ayuda a simular comportamientos para las pruebas
