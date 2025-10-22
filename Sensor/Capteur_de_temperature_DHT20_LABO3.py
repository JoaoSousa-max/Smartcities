# Librairies
from machine import I2C, Pin, ADC, PWM
from utime import sleep
from lcd1602 import LCD1602
from dht20 import DHT20

# Configuration des Pins
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
i2c2 = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
Pot = ADC(1)          # Déclaration de la broche du potentiomètre A1
led = Pin(20, Pin.OUT) # Déclaration de la broche de la LED D20
buzzer = PWM(Pin(18)) # Déclaration de la broche du buzzer D18

# Initialisation du LCD1602 
lcd = LCD1602(i2c2, 2, 16)
lcd.display()

# Initialisation du DHT20 
dht = DHT20(i2c)
note = 392  # fréquence du buzzer (Hz)

# Configuration initiale PWM

buzzer.freq(note)
buzzer.duty_u16(0)    # buzzer éteint au démarrage

# Boucle principale
while True:
    # --- Lecture du potentiomètre (0 à 65535) ---
    val = Pot.read_u16()
   
    # Conversion de la valeur du potentiomètre en température de consigne 15 à 35°C
    Température_de_consigne = 15 + (val / 65535) * (35 - 15)

    # --- Lecture du capteur DHT20 ---
    try:
        dht.read_dht20()
        temp = dht.dht20_temperature()
    except Exception as e:
        print("Erreur lecture DHT20:", e)
        continue  # on saute cette boucle si lecture échoue

    # --- Affichage sur le LCD (mise à jour temps réel) ---
    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.print("T.Ambient: {:.1f}C".format(temp))
    lcd.setCursor(0, 1)
    lcd.print("T.Set: {:.1f}C".format(Température_de_consigne))

    # --- Affichage console pour debug ---
    print("T_mesuree: {:.1f}C | T_consigne: {:.1f}C".format(temp, Température_de_consigne))
    # --- Logique de contrôle ---
    # Cas 1 : proche de la consigne
    if (temp >= Température_de_consigne) and (temp < Température_de_consigne + 3):
      
       
        buzzer.duty_u16(0)   # buzzer OFF
        print("LED clignote à 5 Hz")
        led.value(1)      
        sleep(0.1)        
        led.value(0)      
        sleep(0.1)        

    # Cas 2 : température en dessous de la consigne
    elif temp < Température_de_consigne:
        
        buzzer.duty_u16(0)   # buzzer OFF
        print("LED OFF")

    # Cas 3 : température bien au-dessus (+3°C)
    elif temp > (Température_de_consigne + 3):
    
        
        buzzer.freq(note)  
        buzzer.duty_u16(20000)  
        lcd.clear()
        lcd.setCursor(0, 0)
        lcd.print("ALERTE: {:.1f}C".format(temp))
        print("ALERTE: LED 10 Hz + buzzer actif")
        led.value(1)     
        sleep(0.05)       
        led.value(0)      
        sleep(0.05)
        lcd.clear()  
        led.value(1)     
        sleep(0.05)       
        led.value(0)     
        sleep(0.05)           
        lcd.print("ALERTE: {:.1f}C".format(temp))
        print("ALERTE: LED 10 Hz + buzzer actif")
