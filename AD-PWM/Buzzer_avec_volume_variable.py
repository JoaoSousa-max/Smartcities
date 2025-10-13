from machine import Pin, PWM, ADC
from time import sleep

led = PWM(Pin(20))  # Declaration de la broche de la LED D20
led.freq(1000)  # Fréquence de la LED (1 kHz)
buzzer = PWM(Pin(18)) # Declaration de la broche du buzzer D18
Pot = ADC(1)   # Declaration de la broche du potentiometre A1

  # We wish you a Merry Christmas
notes = [392, 523, 523, 587, 523, 494, 440, 440, 587, 587, 659, 587, 523, 494, 494, 659, 659, 698, 659, 587, 523, 523, 440, 392, 440, 587, 494, 523  ]

while True:   

 for freq in notes:
    buzzer.freq(freq)

    for _ in range(10):  # Lire la valeur du potentiomètre plusieurs fois pour une meilleure stabilité
      
      val = Pot.read_u16()  # Lecture de la valeur du potentiomètre (0-65535)
      volume = int(val/32) # Conversion en pourcentage (0-255)
      print(volume) # Affichage de la valeur du potentiomètre
      buzzer.duty_u16(volume)  # Mettre le buzzer au silence
      led.duty_u16(int(freq * 36))  # Ajuster la luminosité de la LED en fonction de la fréquence (0-65535)

      sleep(0.030) # Pause entre chaque frequence des notes
      
 sleep(1) # Pause entre les cycles des notes
            

        




    
