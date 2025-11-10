# Horloge analogique avec Raspberry Pi Pico et servo

# Objectif

Ce projet a pour but de créer une horloge analogique à l’aide d’un servo moteur, pilotée par un Raspberry Pi Pico.
L’horloge récupère l’heure UTC via Internet par le protocole NTP et applique un fuseau horaire configurable.
Un bouton permet de changer le fuseau horaire ou de basculer entre le mode 12h et 24h.
Le servo positionne l’aiguille en fonction de l’heure locale calculée.

# Description

- Le système fonctionne en boucle continue :

- Connexion au Wi-Fi pour récupérer l’heure via NTP.

- Lecture du bouton pour détecter :

- Double clic pour basculer entre mode 12h et 24h.

- Simple clic pour changer du fuseau horaire.

- Lecture de l’heure UTC et application du fuseau horaire.

- Calcul de l’angle correspondant à l’heure pour positionner le servo.

- Mise à jour du servo toutes les 10 secondes.

# Matériel utilisé pour ce projet

- Raspberry Pi Pico

- Servo moteur = GPIO16 

- Bouton poussoir = GPIO18

- Fils de connexion

# Détails matériels

- Servo moteur

Le servo moteur reçoit un signal PWM pour positionner l’aiguille de l’horloge.
Le signal PWM est configuré pour 50 Hz, avec une durée d’impulsion variant de 500 µs à 2500 µs pour 0° à 180°.

- Bouton poussoir

Le bouton permet de changer le fuseau horaire, basculer le mode 12h/24h de gérer la gestion des rebonds et des intervalles de clic pour détecter correctement les actions simples et doubles clics.

# Déroulement du code

- Initialisation :

1 - Connexion Wi-Fi 

2 - Synchronisation avec serveur NTP pour obtenir l’heure UTC

3 - Initialisation du servo et configuration du bouton

4 - Boucle principale :

5 - Détection des appuis sur le bouton :

6 - Double clic → changement mode 12h/24h

7 - Simple clic → changement du fuseau horaire

8 - Lecture de l’heure UTC et application du fuseau horaire actif

9 - Calcul de l’angle pour le servo en fonction du mode 12h ou 24h

10 - Positionnement du servo

11 - Attente de 50 ms pour la mise à jour de l’heure

# Fichiers nécessaires

main.py (main)

network, ntptime, machine, time

# Remarques

Le projet nécessite une connexion Wi-Fi pour synchroniser l’heure via NTP. Si le Wi-Fi est indisponible, le programme peut être adapté pour continuer avec une heure locale par défaut, mais la synchronisation sera impossible.

La logique de détection des clics et du calcul d’angle permet une gestion continue même après un changement de fuseau horaire ou de mode horaire.

# Images du projet qui représentent le terminal et l'horloge simultanement

![Image](https://github.com/user-attachments/assets/bc606646-4777-46bc-9465-6f3fc6583a89)

<img width="1848" height="1026" alt="Image" src="https://github.com/user-attachments/assets/ac9a0753-319c-4062-973c-c7ed1560ab6c" />



