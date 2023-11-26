import numpy as np;

costs = [
    0,  # Salida
    310,  # Brown 1
    0,  # Arca Comunal 1
    310,  # Brown 2
    0,  # Impuesto sobre ingresos
    0,  # Estación de tren 1
    350,  # Light Blue 1
    0,  # Suerte 1
    350,  # Light Blue 2
    370,  # Light Blue 3
    0,  # Cárcel
    640,  # Pink 1
    0,  # Servicio público 1 (Electricidad)
    640,  # Pink 2
    660,  # Pink 3
    0,  # Estación de tren 2
    680, # Orange 1
    0,  # Arca Comunal 2
    680, # Orange 2
    700, # Orange 3
    0,  # Estacionamiento gratuito
    970, # Red 1
    0,  # Suerte 2
    970, # Red 2
    990, # Red 3
    0,  # Estación de tren 3
    1010, # Yellow 1
    1010, # Yellow 2
    0,  # Servicio público 2 (Agua)
    1040, # Yellow 3
    0,  # Cárcel de visita
    1300, # Green 1
    0,  # Arca Comunal 3
    1300, # Green 2
    1320, # Green 3
    0,  # Estación de tren 4
    1350, # Dark Blue 1
    0,  # Suerte 3
    1400, # Dark Blue 2
    0   # Impuesto de lujo
]

COSTS = np.row_stack(costs * 3) * -1