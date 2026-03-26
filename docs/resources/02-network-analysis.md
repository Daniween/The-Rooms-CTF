# Fiche Pratique : Analyse Réseau

## Le concept
L'analyse réseau consiste à intercepter, observer et analyser le trafic (les "paquets") transitant sur une carte réseau.
Lorsqu'une communication réseau n'est pas chiffrée (exemple : HTTP, Telnet, ou FTP classique), toutes les informations, y compris les mots de passe, circulent en texte clair ("cleartext"). 
Ces données peuvent être capturées et enregistrées dans un fichier `.pcap` (Packet Capture).

## TCPDump
`tcpdump` est l'un des outils de ligne de commande les plus courants pour sniffer ou relire ces paquets.

- `tcpdump -r fichier.pcap` : Lit le fichier pcap et affiche un résumé des paquets.
- `tcpdump -A -r fichier.pcap` : Lit le fichier pcap et affiche le contenu brut du paquet au format ASCII. Parfait pour lire un mot de passe non chiffré transité dans les airs.

Exemple : 
Si l'on cherche un mot de passe ou une connexion ftp, chercher le mot "PASS" ou "USER" dans les logs ASCII avec l'aide de grep :
`tcpdump -A -r ma_capture.pcap | grep -i pass`

## Conseil d'audit
Lisez les trames en clair, et fuyez les protocoles FTP ou HTTP si vous utilisez des identifiants sensibles !
