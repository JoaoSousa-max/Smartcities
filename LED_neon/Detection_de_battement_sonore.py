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
mic = ADC(0)         # microphone GP0

SEUIL = 50
TEMPS_MIN = 0     
dernier_battement = 100

# BONUS BPM
liste_bpm = []
dernier_bpm_calc = utime.ticks_ms()
start_minute = utime.ticks_ms()

def detect_beat(valeur):
    global dernier_battement
    temps_actuel = utime.ticks_ms()
    if valeur > SEUIL and (temps_actuel - dernier_battement) > TEMPS_MIN:
        interval = temps_actuel - dernier_battement
        dernier_battement = temps_actuel
        return interval
    return None

while True:
    valeur = mic.read_u16()/256
    interval = detect_beat(valeur)

    if interval:
        couleur = random.choice(COLORS)
        led.pixels_set(0, couleur) 
        led.pixels_show()

        bpm = 60000 / interval  # interval en ms -> BPM
        liste_bpm.append(bpm)
        print("BPM instant:", int(bpm))

    # toutes les 60 sec -> moyenne BPM -> écrit fichier
    if utime.ticks_diff(utime.ticks_ms(), start_minute) >= 60000:
        if len(liste_bpm) > 0:
            moyenne = sum(liste_bpm)/len(liste_bpm)
            print("Moyenne minute BPM:", int(moyenne))

            try:
                with open("bpm_log.txt","a") as f:
                    f.write(str(int(moyenne))+"\n")
            except:
                print("Erreur écriture fichier")

        # reset
        liste_bpm = []
        start_minute = utime.ticks_ms()

    utime.sleep(0.05)
