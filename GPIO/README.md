Premier Labo avec micro python Contrôle d'une LED avec un bouton poussoir sur un microcontroleur MicroPython

# Description: 
Ce programme écrit en MicroPython permet de controler la frequence de clignotement d'une LED a l'aide d'un bouton poussoir. 
Il y a une sequence de quatres touches sur le bouton poussoir qui influencera l'état de la LED, la derniére touche (quatrième touche) fera recommencer le cycle a 0.

# Materiel utlisé pour ce rapport:

- 1 LED 

- 1 bouton poussoir 

- Des Fils de connexion 

- Liste des broches connectées: 

- LED connectée à la broche GP20 

- Bouton Poussoir connecté à la broche GP18

# Déroulemnt du code: 
1 - Lors de la 1ère impulsion sur le bouton poussoir, la LED clignote avec une frequence de 5Hz.

2 - Lors de la 2ème impulsion sur le bouton poussoir, la LED clignote à une frequence de 10Hz.

3 - Lors de la 3ème impulsion sur le bouton poussoir, la LED clignote à une frequence de 16Hz. 

4 - Lors de la 4ème impulsion sur le bouton poussoir, la LED s'éteint et redemarre alors le cycle.



