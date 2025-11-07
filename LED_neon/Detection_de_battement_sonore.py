from ws2812 import WS2812 
from machine import Pin, ADC
import utime
import random

RED    = (255,0,0)
YELLOW = (255,150,0)
GREEN  = (0,255,0)
CYAN   = (0,255,255)
BLUE   = (0,0,255)
PURPLE = (180,0,255)
WHITE  = (255,255,255)
COLORS = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]

led = WS2812(18, 1)  # 1 LED sur GPIO18

mic = ADC(0)  # microphone connecté à GP0

SEUIL = 120       #seuil du micro
TEMPS_MIN = 0     
dernier_battement = 100

def detect_beat(valeur):
    global dernier_battement
    temps_actuel = utime.ticks_ms()
    if valeur > SEUIL and (temps_actuel - dernier_battement) > TEMPS_MIN:
        dernier_battement = temps_actuel
        return True
    return False

while True:
    valeur = mic.read_u16()/256
    if detect_beat(valeur):
        couleur = random.choice(COLORS)
        led.pixels_set(0, couleur) 
        led.pixels_show()            
    utime.sleep(0.05)
