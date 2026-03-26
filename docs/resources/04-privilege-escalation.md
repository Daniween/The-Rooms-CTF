# Fiche Pratique : Élévation de privilèges & SUID

## Le concept de base : SUID Bit
Sous Linux (et les systèmes UNIX en général), un binaire (une application exécutable) qui possède l'attribut spécial "SUID" (Set User ID) sera toujours exécuté avec les privilèges exclusifs de son propriétaire (généralement `root`), peu importe l'utilisateur qui tapera la commande !

Cela crée une brèche de sécurité critique : si un attaquant peut manipuler ou utiliser de manière détournée ce fichier (GTFOBins), il obtient indirectement un pouvoir `root`.

## Comment le trouver ?
Un fichier doté de l'attribut SUID possède un "s" dans ses droits :
`rws r-x r-x` au lieu de `rwx r-x r-x`.

Pour chercher tous les fichiers de votre session actuelle ayant ce privilège attribué, on fait appel à la commande FIND avec l'argument '-perm'
`find / -type f -user root -perm -4000`
