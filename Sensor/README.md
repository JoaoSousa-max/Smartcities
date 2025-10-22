# Contrôle de température avec Raspberry Pi Pico

# Objectif
Ce projet a pour but de surveiller la température ambiante à l'aide d'un capteur DHT20 et comparer la température ambiante a une température de consigne réglable par un potentiomètre, 
en fonction de la position du potentiomètre.
Lorsque la température ambiante dépasse la température de consigne, 
une led clignote a une fréquence de 5Hz et si la température va au-dela de +3 degrees alors led clignote plus vite que 5hz et un buzzer est activé avec un message "alarme" sur un écran lcd 16x2 qui affiche toutes les températures en temps réel.


# Description:

Le système fonctionne en boucle continue :

- Lecture de la température ambiante via le capteur DHT20.
- Lecture de la valeur du potentiomètre, qui défini la température de consigne entre 15°C et 35°C.
- Affichage des deux températures.
- Déclenchement d’alertes lorsque:
- La température de la consigne dépasse la température ambiante, led clignote à 5 Hz .
- Température en dessous de la consigne la led est éteinte.
- Si la température est au-dessus de +3°C alors la led à 10 Hz et le buzzer est actif avec un message d’alerte sur le LCD.


# Materiel utlisé pour ce rapport:

- Raspberry Pi Pico
- DHT20
- LCD1602
- Potentiomètre
- LED        
- Buzzer      
- Fils de connexion
     
# dht20:

Le dht20 est un capteur de température et d'humidité.

La communication est faite par I2C avec le Raspberry PI Pico.

Pour pouvoir configurer le dht20 j'ai utilisé la librairie: dht20.py  

# lcd1602:

Le lcd1602 est un écran LCD de 2lignes x 16 caractères.

La communication est faite par I2C avec le Raspberry Pi Pico.

Pour pouvoir configurer le lcd j'ai utilisé la librairie: lcd1602.py  


# Déroulement du code:

Déroulement du code
- Initialisation.
- Configuration des broches I2C, ADC, PWM.
- Initialisation du LCD et du capteur DHT20.
- Lecture du potentiomètre.
- Conversion de la valeur analogique en température de consigne de 15 à 35°C.
- Lecture du capteur DHT20.
- Récupération de la température ambiante.
- Gestion des erreurs de lecture.
- Affichage des données.
- Affichage sur le LCD.
- Affichage dans la console pour le débogage.
- Logique de contrôle :
- Si température est supérieure à celle de consigne, mais inférieur a température de consigne +3 alors: "la led clignote à 5 Hz".
- Si température est inférieure à celle de consigne alors: "led est off".
- Si température est supérieure à celle de consigne de + 3°C alors: la led clignote à envierons 10 Hz, le buzzer est actif et un message d’alerte apparait sur le lcd.

# Fichiers nécessaires

- lcd1602.py (lib_écran)
- dht20.py (lib_capteur)
- Capteur_de_temperature_DHT20_LABO3.py (main)

# Image du projet

![WhatsApp Image 2025-10-22 à 18 35 55_7ac997bc](https://github.com/user-attachments/assets/e5547a7d-6ae3-48c8-afcf-badf893c188c)





