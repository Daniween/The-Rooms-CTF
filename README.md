# Hackathon 2026 - CyberQuest: Infiltration d'EvilCorp
[![Version](https://img.shields.io/badge/Version-2026-blue)]()

![wallpaper](docs/images/wallpaper-1.jpg)

## Description
Bienvenue dans "CyberQuest", un CTF entièrement repensé pour tester et améliorer vos compétences système et réseau de manière concrète. 
Dans ce scénario de simulation d'intrusion (Red Team), vous avez été engagé pour infiltrer les serveurs de la multinationale "EvilCorp". Chaque niveau nécessite l'application de diverses techniques et compétences en cybersécurité pour déverouiller une archive protégée (`secret.zip`) et accéder au niveau suivant.

## Objectifs Pédagogiques

- Maîtriser l'investigation dans l'historique d'un dépôt Git (Git Leaks).
- Développer des compétences en analyse réseau (PCAP, TCPDump).
- Comprendre et exploiter le port-forwarding SSH ou l'accès aux interfaces locales.
- Extraire des métadonnées dissimulées (Steganographie basique / Exiftool).
- Exploiter les vulnérabilités de configuration système Linux (Élévation de privilèges via SUID).

## Description des niveaux

| Niveau | Objectif Cible | Compétences développées |
|--------|----------------|-------------------------|
| **Niveau 1** | Explorer un dépôt Git pour retrouver un vieux commit contenant des identifiants (Git Leak) | Investigation repository Git |
| **Niveau 2** | Analyser une capture de trames réseau (`.pcap`) pour récupérer un mot de passe en clair | Analyse Réseau, TCPDump, Scapy |
| **Niveau 3** | Découvrir et interagir avec un service caché n'écoutant que sur l'interface locale (`127.0.0.1`) | Reconnaissance réseau interne, SSH Tunneling |
| **Niveau 4** | Analyser les métadonnées d'une image pour y déceler des informations dissimulées | Analyse de métadonnées, Exiftool |
| **Niveau 5** | Élévation de privilèges (Privesc) en exploitant un exécutable possédant le bit SUID | Système Linux, Privesc, GTFOBins |
| **Niveau 6** | Rétro-ingénierie d'un binaire C protégé (Analyse dynamique et appels systèmes) | Reverse Engineering, ltrace, strings |

## Démarrage et accès au Hub

### Prérequis
Assurez-vous que Docker et Docker Compose sont bien installés sur votre système hôte.

### Démarrage des containers

Depuis la racine du projet, lancez la commande suivante pour construire et démarrer les serveurs en arrière-plan :

```bash
docker compose build
docker compose up -d
```

### Accès au Hub (Point d'Entrée)

Voici les identifiants pour entrer dans l'infrastructure de départ "EvilCorp Hub" :

```bash
ssh -p 2222 infiltrator@<ip_address>
 
# Mot de passe : welcome
```

*(<ip_address> correspond à l'adresse de votre machine hôte (ex: `127.0.0.1` ou l'IP de votre VM/Serveur))*

Si vous avez besoin de regarder la topologie du lab plus tard dans docker, le réseau se trouve sur la plage `172.30.0.0/24`.

Bon apprentissage et que le meilleur gagne !