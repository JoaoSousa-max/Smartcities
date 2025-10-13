# Objectif

Le deuxième labo en Micropython a comme objectif principal de permetre a l'utilisateur de contrôler le volume d'un buzzer grâce a un potentiomètre.

# Description:

Pour ce labo en Micropython le but est de réproduire une mélodie qui sera composé par une séquence 
de differentes fréquences qui sont ensuite reproduites par le buzzer. 
La melodie choisi s'agit de "We wish you a merry christamas". 
Grâce a un potentiomètre le volume du son produit par le buzzer peut être varié. 
Pour contrôler le volume avec le potentiometre, les broches ont été configuré comme digital PWM, le PWM (Pulse Widht modulation) est une fonctionnalité 
qui permet de varier les cycles d'une periode permettant ainsi de varier l'intensité par des niveau de palliers. Le PWM permet de varier 
l'intensité du signal ayant ainsi un lien directe avec la variation du volume du buzzer.

Une LED est utilisé pour temoigner la variation de l'intensité des frequences utlises pendant la mélodie.

# Materiel utlisé pour ce rapport:

- 1 Buzzer

- 1 LED

- 1 Potentiomètre

- Des Fils de connexion


Liste des broches connectées:

LED connectée à la broche GP20

Bouton Poussoir connecté à la broche GP18

# Déroulemnt du code:
1 - Lors de la 1ère impulsion sur le bouton poussoir, la LED clignote avec une frequence de 5Hz.

2 - Lors de la 2ème impulsion sur le bouton poussoir, la LED clignote à une frequence de 10Hz.

3 - Lors de la 3ème impulsion sur le bouton poussoir, la LED clignote à une frequence de 16Hz.

4 - Lors de la 4ème impulsion sur le bouton poussoir, la LED s'éteint et redemarre alors le cycle.
