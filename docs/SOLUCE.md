# Hackathon 2026 - CyberQuest - SOLUTION

[![Version](https://img.shields.io/badge/Version-2026-blue)]()

## Solution détaillée

### Niveau 1: Git Leak

- Explorer le dossier `project`
- Utiliser la commande `git log -p` ou git history pour visualiser les anciens commits.
- L'un des commits contient la suppression d'un fichier `.env` avec le mot de passe : `GitL0v3r`.

**Décompression de l'archive:**
```bash
  unzip -P GitL0v3r secret.zip

# Archive:  secret.zip
# extracting: flag.txt
# inflating: key_part.txt
# extracting: next_level.txt
```

#### Infos à récupérer pour le niveau suivant:

- Flag : FLAG{g1t_c0mm1t_l34k_f0und}
- contenu du fichier next_level.txt : 
  - Host : 172.30.0.12 
  - User : bob 
  - Pass : Pc4PwIr3sh4rK


### Niveau 2: Analyse réseau PCAP

- Ouvrir ou analyser le fichier `network_capture.pcap` situé dans le dossier de l'utilisateur.
- Utiliser tcpdump pour afficher le contenu en clair, par exemple :
  `tcpdump -A -r network_capture.pcap | grep PASS`
- Trouver le mot de passe FTP en clair transféré sur le réseau : `CleartextIsBad`.

**Décompression de l'archive:**
```bash
  unzip -P CleartextIsBad secret.zip

# Archive:  secret.zip
# extracting: flag.txt
# inflating: key_part.txt
# extracting: next_level.txt
```

#### Infos à récupérer pour le niveau suivant:

- Flag : FLAG{pc4p_n3tw0rk_c4ptur3}
- contenu du fichier next_level.txt :
    - Host : 172.30.0.13
    - User : charlie
    - Pass : Tu443LSs8

### Niveau 3: Service Caché / Local Port

- Analyser les ports ouverts localement avec `ss -tulpn` ou `netstat -an`.
- Découvrir que le port 8080 écoute sur `127.0.0.1`.
- Les administrateurs ayant supprimé `curl` et `wget`, il faut utiliser un tunnel SSH pour rediriger le port vers votre machine (ou le Hub).
  Se reconnecter avec l'option `-L` :
  `ssh -4 -L 8080:127.0.0.1:8080 charlie@172.30.0.13`
  Depuis un autre terminal (ou après avoir mis la session en arrière-plan), faire la requête HTTP locale :
  `curl http://127.0.0.1:8080/`
- Le mot de passe rendu par la page est `LocalHostBypass`.

**Décompression de l'archive:**
```bash
  unzip -P LocalHostBypass secret.zip

# Archive:  secret.zip
# extracting: flag.txt
# inflating: key_part.txt
# extracting: next_level.txt
```

#### Infos à récupérer pour le niveau suivant:

- Flag : FLAG{l0c4lf0rw4rd_m4st3r}
- contenu du fichier next_level.txt :
    - Host : 172.30.0.14
    - User : dave
    - Pass : 3xIft00lS

### Niveau 4: Métadonnées (ExifTool / Stegano)

- Examiner l'image `company_logo.jpg`.
- Utiliser un outil comme exiftool ou la commande strings:
  `exiftool company_logo.jpg` ou `strings company_logo.jpg | grep ZIP_PASS`
- Repérer le champ `Comment` (ou autre metadata) contenant le mot de passe : `HiddenInImage`.

**Décompression de l'archive:**
```bash
  unzip -P HiddenInImage secret.zip

# Archive:  secret.zip
# extracting: flag.txt
# inflating: key_part.txt
# extracting: next_level.txt
```

#### Infos à récupérer pour le niveau suivant:

- Flag : FLAG{m3t4d4t4_4ct1ng_up}
- contenu du fichier next_level.txt :
    - Host : 172.30.0.15
    - User : eve
    - Pass : 3L3v4T3m3

### Niveau 5: Privilèges SUID (Privesc)

- Rechercher les binaires possédant le bit SUID qui pourraient être exploités pour lire un fichier protégé.
  `find / -user root -perm -4000 2>/dev/null`
- Découvrir que la commande `find` possède le bit SUID (`/usr/local/bin/find`).
- Utiliser cette commande pour forcer la lecture du fichier de mot de passe du root (`/root/flag_dir/password.txt`) :
  `find . -exec cat /root/flag_dir/password.txt \; -quit`
- Le mot de passe obtenu est `SuidRootMaster`.

**Décompression de l'archive:**
```bash
  unzip -P SuidRootMaster secret.zip

# Archive:  secret.zip
# extracting: flag.txt
# inflating: key_part.txt
# extracting: next_level.txt
```

#### Infos à récupérer pour le niveau suivant:

- Flag : FLAG{su1d_r00t_3sc4l4t10n_d0n3}
- contenu du fichier next_level.txt :
    - Host : 172.30.0.16
    - User : frank
    - Pass : FindM3IfYouC4n

### Niveau 6: Rétro-ingénierie (Analyse de binaire)

- Un binaire compilé en C nommé `auth_service` est présent dans le répertoire.
- Il s'agit d'un exécutable vérifiant un mot de passe passé en argument.
- Utilisez la commande `ltrace` pour observer les appels aux fonctions de bibliothèques dynamiques:
  `ltrace ./auth_service motdepasse_quelconque`
- Observez l'appel à la fonction `strcmp` (comparaison de chaînes) qui révèle le texte attendu : `R3v3rs3_M4st3r`.
- Alternative: la commande `strings auth_service` liste toutes les chaînes de texte, dont le mot de passe s'y trouve.

**Décompression de l'archive:**
```bash
  unzip -P R3v3rs3_M4st3r secret.zip

# Archive:  secret.zip
# extracting: flag.txt
# inflating: key_part.txt
# extracting: next_level.txt
```

#### Fin de partie !

- Le Flag Ultime : FLAG{r3v3rs3_3ng1n33r_g0d}
- Vous avez infiltré EvilCorp et terminé ce CTF.