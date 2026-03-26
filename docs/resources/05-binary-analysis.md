# Fiche Pratique : Reverse Engineering de bas niveau (Ltrace)

## Le concept ou Outil
Lorsqu'un créateur compile son programme depuis du code en langages tels que C ou C++, le fichier exécutable résultant masque entièrement le code source. "Reverse", ou la "rétro-ingénierie", c'est la tâche souvent complexe visant à le décompiler (Ghidra, IDA), pour l'ausculter pour deviner son fonctionnement.

La commande "ltrace", pour *library call tracer*, est un bon outil de premier plan. Lorsqu'un fichier ELF (.exe) interagit avec le système ou lance une vérification de la demande d'entrée ("mot de passe" par exemple), son déroulement doit passer à un moment ou un autre par des requêtes de librairies (`strcmp()`, `printf()`, etc.) afin de vérifier une condition.
Ltrace se charge de l'espionner en vous rendant dans la console chaque appel intercepté !

## Commandes utiles
- `ltrace ./mon_programme` : Exécute le programme et liste chaque appel à la bibliothèque de Linux.

## Conseil d'audit
Ne faites jamais confiance au comportement binaire par défaut, traquez chacun de ses faits et gestes.
