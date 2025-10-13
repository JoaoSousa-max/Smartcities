# Objectif

Le deuxième laboratoire en Micropython a pour objectif principal de permettre à l'utilisateur de contrôler le volume d'un buzzer à l'aide d'un potentiomètre, tout en reproduisant une mélodie, qui fera varier l'état d'une LED.

# Description:
Ce programme en Micropython reproduit la mélodie  "We wish you a merry christamas".
La mélodie est constituée d'une séquence de fréquences correspondant aux différents notes musicales.

Le volume du son émis par le buzzer est ajusté en temps réel grâce a un potentiomètre, qui génère une tension analogique. Cette tension est lue par l'entrée
ADC du microcontrôleur, et ensuite transformé en une valeur de rapport cyclique PWM pour varier l'intensité du signal envoyé au buzzer.

Une LED est connectée sur une autre broche PWM, qui permet une variation de l'intensité lumineuse de la LED, qui varie en fonction de la mélodie joué par le buzzer.

# Materiel utlisé pour ce rapport:

- 1x Buzzer

- 1x LED

- 1x Potentiomètre

- Des Fils de connexion


# Liste des broches connectées:

- LED connectée à la broche D20
- Buzzer connecté à la broche D18
- Bouton Poussoir connecté à la broche A1

Bouton Poussoir connecté à la broche GP18

# Déroulemnt du code:
1 - Lors de la 1ère impulsion sur le bouton poussoir, la LED clignote avec une frequence de 5Hz.

2 - Lors de la 2ème impulsion sur le bouton poussoir, la LED clignote à une frequence de 10Hz.

3 - Lors de la 3ème impulsion sur le bouton poussoir, la LED clignote à une frequence de 16Hz.

4 - Lors de la 4ème impulsion sur le bouton poussoir, la LED s'éteint et redemarre alors le cycle.

