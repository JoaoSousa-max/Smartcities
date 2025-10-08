import machine
from utime import sleep

bouton = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(20, machine.Pin.OUT)

clic = 0     
frequence = 0 

while True:
  
    if bouton.value() == 1:
        clic = clic + 1   
        sleep(0.3)       

        if clic == 1:
            frequence = 5
        elif clic == 2:
            frequence = 10
        elif clic == 3:
            frequence = 16    
        elif clic == 4:
            frequence = 0
            clic = 0       

    if frequence == 5:
        led.toggle()
        sleep(1 / (2 * 5))  

    elif frequence == 10:
        led.toggle()
        sleep(1 / (2 * 10)) 

    elif frequence == 16:
        led.toggle()
        sleep(1 / (2 * 16)) 
        
    else:
        led.value(0)         
        sleep(0.1)
