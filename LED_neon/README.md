# Détection de battement sonore avec la led WS2812 sur un Raspberry Pi Pico

# Objectif

Ce projet a pour but de détecter des variations sonores grâce à un microphone branché sur une entrée analogique du Raspberry Pi Pico, puis d’allumer une LED RGB WS2812 en changeant sa couleur aléatoirement à chaque détection des pics sonores reçus par le microphone.

# Matériel utilisé

Raspberry Pi Pico

1x LED RGB WS2812 

1x Microphone analogique

Fils de connexion 

# Description

Le système fonctionne dans une boucle infinie.

1- Lecture en temps réel du microphone via une entrée ADC.

2- Quand un pic sonore dépasse un seuil défini, cela est considéré comme un pic sonore.

3- A chaque pic sonore détecté, la LED WS2812 change de couleur de manière aléatoire.

4- Différentes couleurs RGB sont disponibles et sélectionnées aléatoirement.

5- Le code tourne en continu en vérifiant toutes les 50ms.

# Fonctionnement général du code

Initialisation de la LED WS2812 sur le GPIO18.

Initialisation du microphone en entrée analogique sur GP0.

Définition d’un seuil sonore : si le signal dépasse cette valeur, un pic sonore est détecté.

Lors d’un pic sonore: Il y a le choix d’une couleur RGB aléatoire.

Ensuite il y a une mise à jour de la LED WS2812.

# Librairies nécessaires

ws2812.py 

machine / ADC 

utime

# Fichier principal

Detection_de_battement_sonore.py (main)


