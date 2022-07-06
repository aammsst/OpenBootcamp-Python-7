import time

# suponiendo 8 hrs de trabajo, salida a las 19,
# entrada a las 11 

#hora = time.localtime().tm_hour
hora = 18
minutos = time.localtime().tm_min

if 11 <= hora <= 18:
    print("Quedan", 18 - hora, "hora/s y", 59 - minutos, "minuto/s de trabajo")
else:
    print("Ya deberías estar en tu casa!")
