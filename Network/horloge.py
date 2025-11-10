import network
import ntptime
import time
from machine import Pin, PWM

# Wifi Config
WIFI_SSID = "VOO-2G7LV36" # Nom du reseau Wifi
WIFI_PASS = "cpCafHXHaGYGGLsxgf" #Mot de passe du reseau Wifi privée 

# Servo
SERVO_PIN = 16            # GPIO du servo
SERVO_FREQ = 50           # 50 Hz 
SERVO_MIN_US = 500        # pulse min en microsecondes
SERVO_MAX_US = 2500       # pulse max en microsecondes 

# Bouton
BUTTON_PIN = 18
# Liste des fuseaux 
TIMEZONES = [0, 1, -5, 2]   #UTC, UTC+1, UTC-5, UTC+2 (la belgique se trouve dans UTC+1

DOUBLE_CLICK_MS = 300       # intervalle pour considérer double clic sur le bouton
SINGLE_CLICK_DECIDE_MS = 350
# Intervalle d'update du servo 
UPDATE_INTERVAL = 10  # 10 secondes

# Fonctions utilitaires
def connect_wifi(ssid, password, timeout=15):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connexion au Wi-Fi...")
        wlan.connect(ssid, password)
        t0 = time.time()
        while not wlan.isconnected():
            if time.time() - t0 > timeout:
                raise RuntimeError("Impossible de se connecter au Wi-Fi")
            time.sleep(0.5)
    print("Connecte, config reseau :", wlan.ifconfig())
    return wlan

def sync_time(retries=3):
    for i in range(retries):
        try:
            print("Synchronisation ntp (UTC)")
            ntptime.settime()  # met l'horloge RTC à l'heure UTC
            print("NTPOK")
            return True
        except Exception as e:
            print(" erreur:", e)
            time.sleep(2)
    print("Attention : échec synchronisation NTP.")
    return False

# Convertit pulse microsecondes en duty_u16 PWM sur une période de 20 ms
def us_to_duty_u16(pulse_us, freq=SERVO_FREQ):
    period_us = int(1_000_000 / freq)
    duty_fraction = pulse_us / period_us
    duty_u16 = int(duty_fraction * 65535)
    if duty_u16 < 0: duty_u16 = 0
    if duty_u16 > 65535: duty_u16 = 65535
    return duty_u16

# Définir angle 0..180° 
def angle_to_pulse_us(angle_deg):
    if angle_deg < 0: angle_deg = 0
    if angle_deg > 180: angle_deg = 180
    # interpolation linéaire entre min et max microsecondes
    return SERVO_MIN_US + (angle_deg / 180.0) * (SERVO_MAX_US - SERVO_MIN_US)

# Calcul de l'angle selon mode 12h/24h (minutes incluses pour position intermédiaire)
def compute_angle(hours, minutes, mode24):
    frac_hour = hours + (minutes / 60.0)
    if mode24:
        # 24h -> 0..180°: 7.5°/h
        angle = frac_hour * (180.0 / 24.0)  # = *7.5
    else:
        # 12h -> 0..180°: 15°/h 
        angle = (frac_hour % 12.0) * (180.0 / 12.0)  # 15 degrees/h

    return angle


# Setup matériel

# Servo PWM
servo_pwm = PWM(Pin(SERVO_PIN))
servo_pwm.freq(SERVO_FREQ)

def set_servo_angle(angle):
    pulse = angle_to_pulse_us(angle)
    duty = us_to_duty_u16(pulse, SERVO_FREQ)
    servo_pwm.duty_u16(duty)

button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

# Variables de gestion des clics
_press_times = []  # stocke timestamps des pressions récentes

def _button_irq(pin):
    try:
        _press_times.append(time.ticks_ms())
    except Exception:
        # en cas de mémoire bloquée, ignore
        pass

# Attache IRQ sur front descendant
button.irq(trigger=Pin.IRQ_FALLING, handler=_button_irq)

# Etat application
tz_index = 0
mode24 = False

# Deroulement principale du programme
def main():
    global tz_index, mode24, _press_times

    # 1) Wi-Fi
    try:
        connect_wifi(WIFI_SSID, WIFI_PASS)
    except Exception as e:
        print("Wi-Fi failed:", e)
    # 2) Sync NTP
    sync_time(retries=5)

    last_update = 0

    print("Demarrage boucle horloge:")
    while True:
        now_ms = time.ticks_ms()

        # GESTION BOUTON 
        # Nettoyer les vieux timestamps et garder seulement les 2 plus récents
        if len(_press_times) > 2:
            _press_times = _press_times[-2:]
        # Si on a 2 pressions et qu'elles sont très proches
        if len(_press_times) >= 2:
            t1 = _press_times[-2]
            t2 = _press_times[-1]
            if time.ticks_diff(t2, t1) <= DOUBLE_CLICK_MS:
                # Double clic détecté
                mode24 = not mode24
                print("Double clic : bascule mode24 ->", mode24)
                _press_times = []
                # petite temporisation pour éviter rebonds multiples
                time.sleep_ms(200)
        # Si on a 1 pression et qu'on attend assez longtemps sans seconde pression
        elif len(_press_times) == 1:
            t0 = _press_times[0]
            if time.ticks_diff(time.ticks_ms(), t0) > SINGLE_CLICK_DECIDE_MS:
                # changement fuseau horaire par un click sur le bouton
                tz_index = (tz_index) % len(TIMEZONES)
                print("Single clic : fuseau -> UTC{:+d}".format(TIMEZONES[tz_index]))
                _press_times = []
                time.sleep_ms(150)

        # CALIBRAGE DU SERVO MOTEUR   
        
        if time.time() - last_update >= UPDATE_INTERVAL:
            last_update = time.time()
            # lire l'heure locale depuis RTC depuis UTC
            t = time.localtime()# time.localtime() retourne toutes les infos du fuseau horarire
            utc_hour = t[3]
            utc_min = t[4]
            #fuseau horaire 
            tz = TIMEZONES[tz_index]+1
            hour_local = (utc_hour + tz) % 24
            minute_local = utc_min
            # calcul angle
            angle = compute_angle(hour_local, minute_local,mode24)
            
            # Affichage sur le terminal des horaires UTC et local 
            print("Heure UTC: {:02d}:{:02d} | Fuseau UTC{:+d} -> local {:02d}:{:02d}".format(
                utc_hour, utc_min, tz, int(hour_local), int(minute_local)))
            #Affichage de l'angle en fonction des heures 
            print("Mode24:", mode24, "| angle = {:.2f} degrees".format(angle))
            set_servo_angle(angle)


        time.sleep_ms(50)

# Lancement du main()
if __name__ == "__main__":
   
        main()
  