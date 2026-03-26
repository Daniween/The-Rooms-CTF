# Fiche Pratique : Services Cachés et SSH Port Forwarding

## Le concept de base
Dans certaines cibles ou serveurs, des services sont volontairement isolés ou coupés du réseau externe (`10.x`, `172.x` etc.). Ces services ne tournent alors que sur la boucle locale (l'adresse de boucle `127.0.0.1` ou `localhost`). Une personne à l'extérieur ne pourra pas l'atteindre directement.  

Si ce service caché est un site web/API (port 80 ou 8080), il n'est donc pas accessible classiquement depuis le navigateur de sa propre machine et le trafic web s'arrêtera aux portes du pare-feu.

## Identifier et résoudre
La première action consiste à utiliser `netstat -an` ou la commande allégée `ss -tulpn` pour lister toutes ces écoutes discrètes non montrées à l'utilisateur :
- `ss -tulpn` : Affiche de manière explicite tous les processus d'interface et d'écoute réseau.

Une fois repéré (exemple: `127.0.0.1:port_cible`), on peut faire deux choses :
### 1. Utiliser un client en interne (CLI)
L'outil en ligne de commande `curl` peut simuler un accès web, afficher la requête HTTP GET textée depuis l'intérieur même du terminal :
`curl http://127.0.0.1:port_cible`

### 2. Le port forwarding (Tunnel SSH)
C'est souvent l'opération désirée pour faciliter le pilotage : depuis le Terminal Côté Client (votre PC) on encapsule le port localement grâce à une connexion chiffrée de SSH.
`ssh -L port_local:127.0.0.1:port_cible utilisateur@IP_ADDRESS`

Alors sur sa propre machine, l'audit local est faisable en tapant l'URL : http://127.0.0.1:port_local sur son navigateur.
