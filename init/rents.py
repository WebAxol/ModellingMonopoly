import numpy as np;

rents = [
    0,  # Salida
    250,  # Brown 1
    0,  # Arca Comunal 1
    450,  # Brown 2
    0,  # Impuesto sobre ingresos
    0,  # Estación de tren 1
    550,  # Light Blue 1
    0,  # Suerte 1
    550,  # Light Blue 2
    600,  # Light Blue 3
    0,  # Cárcel
    750,  # Pink 1
    0,  # Servicio público 1 (Electricidad)
    750,  # Pink 2
    900,  # Pink 3
    0,  # Estación de tren 2
    950, # Orange 1
    0,  # Arca Comunal 2
    950, # Orange 2
    1000, # Orange 3
    0,  # Estacionamiento gratuito
    1050, # Red 1
    0,  # Suerte 2
    1050, # Red 2
    1100, # Red 3
    0,  # Estación de tren 3
    1150, # Yellow 1
    1150, # Yellow 2
    0,  # Servicio público 2 (Agua)
    1200, # Yellow 3
    0,  # Cárcel de visita
    1275, # Green 1
    0,  # Arca Comunal 3
    1275, # Green 2
    1400, # Green 3
    0,  # Estación de tren 4
    1500, # Dark Blue 1
    0,  # Suerte 3
    2000, # Dark Blue 2
    0   # Impuesto de lujo
]

colors = [
    'brown',
    'lightblue',
    'pink',
    'orange',
    'red',
    'yellow',
    'green',
    'darkblue'
]

RENTS = np.diag(rents * 3)