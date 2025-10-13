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

# PWM:

Le PWM (Pulse widht Modulation) permet de faire varier l'intensité moyenne d'un signal numérique lorsqu'on modifie le rapport cyclique.
- Le buzzer utilise le PWM pour varier le volume.
- La LED utilise le PWM pour varier son intensité lumineuse.

# Déroulement du code:

1 - Le code commence avec l'initialisation de la gestion des broches GPIO, GPIO PWM et l'ADC.

2 - Configuration des broches: La LED et le buzzer sont définies comme des pins PWM. Tandis que le potentiomètre a été configuré comme pin ADC.

3 - Ensuite la variable notes a été déclaré, cette variable comprend une liste de fréquences correspondant aux notes de la mélodie " We wish you a merry Christmas".

4 - Ensuite une boucle for démarre, cette boucle est responsable de parcourrir toutes les fréquences de la mélodie, une par une de maniére séquentielle.

5 - La lecture répétée de la valeur du potentiomètre pour obtenir en temps réel la position du potentiomètre, pour ajuster le volume.

6 - Conversion de la valeur analogique du potentiomètre en rapport cyclique PWM pour contrôler le volume du buzzer, 

7 - L'intensité de la LED va varier en fonction de la mélodie.

8 - Ensuite il y a la lecture et affichage du volume sur le terminal en temps réel.

9 - Ensuite une pause de est produite entre chaque reproduction des fréquences.

10 - Et à la fin il a une pause plus prolongée pour séparer chaque cycle qui redemarre a 0 à nouveau.






