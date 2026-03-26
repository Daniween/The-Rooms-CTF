# Fiche Pratique : Investigation Git

## Le concept
Git est un système de contrôle de version. Il enregistre l'historique complet des modifications effectuées sur un projet.
Même si un fichier a été supprimé ou modifié aujourd'hui, les anciennes versions restent stockées dans le '.git' du projet (à condition que la modification ait été encodée, c'est-à-dire "commitée").

Cette persistance est la cause principale de ce qu'on appelle les "Git Leaks" : l'exposition involontaire de mots de passe, clés API ou identifiants.

## Commandes utiles

- `git status` : Affiche l'état du répertoire de travail (les fichiers modifiés, supprimés, etc. non encore commités).
- `git log` : Affiche la liste des anciens commits avec leur identifiant (hash), leur auteur et leur message.
- `git log -p` : Affiche la liste des commits ET détaille l'exactitude des fichiers modifiés, lignes ajoutées (+) et supprimées (-). C'est idéal pour lire un mot de passe qui aurait été supprimé par l'auteur !
- `git diff <commit1> <commit2>` : Compare deux points précis dans le temps.
- `git show <hash>` : Permet de voir l'intégralité d'un commit spécifique.

## Conseil d'audit
Ne présumez jamais qu'un dossier est vide ou que le code actuel est la seule chose importante. Le secret réside dans le passé.
