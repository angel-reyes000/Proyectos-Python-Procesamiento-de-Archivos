import logging 
import random
import time

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler(r"C:\\Users\\Luis Reyes\\Downloads\\battery_temperature.log", mode="w")
handler.setLevel(logging.DEBUG)

consola = logging.StreamHandler()
consola.setLevel(logging.DEBUG)

formato = "%(levelname)s - %(message)s - %(asctime)s - %(name)s"
formatter = logging.Formatter("%(levelname)s - ".ljust(10) + "%(message)s - %(asctime)s - %(name)s")
handler.setFormatter(formatter)
consola.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(consola)

tiempo = 0

while tiempo <= 59:
    time.sleep(1)
    numero_random = random.randint(15, 45)
    tiempo+=1
    if numero_random < 20:
        logger.debug(f"TEMPERATURE_IN_CELSIUS: {numero_random}°C")
    elif numero_random >=20 and numero_random < 30:
        logger.info(f"TEMPERATURE_IN_CELSIUS: {numero_random}°C")
    elif numero_random >= 30 and numero_random <= 35:
        logger.warning(f"TEMPERATURE_IN_CELSIUS: {numero_random}°C")
    elif numero_random > 35 and numero_random <=39:
        logging.error(f"TEMPERATURE_IN_CELSIUS: {numero_random}°C")
    else:
        logging.critical(f"TEMPERATURE_IN_CELSIUS: {numero_random}°c")
