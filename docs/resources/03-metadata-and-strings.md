# Fiche Pratique : Métadonnées et Texte Brut

## Métadonnées d'image
ExifTool est un outil classique permettant d'extraire (ou de modifier) les métadonnées (EXIF) encodées au sein des fichiers numériques tels que des images (`.jpg`, `.png`), ou des documents audios, vidéos, PDF.
Les appareils photos ou les logiciels d'édition "polluent" souvent vos images avec des métadonnées comme : 
- l'heure locale
- le modèle de l'appareil
- les coordonnées GPS...
- ou des commentaires textuels cachés par des logiciels (steghide) ou manuellement (hackers)

## Commandes 

- `exiftool <mon_fichier>` : Répertorie toutes les métadonnées associées au fichier.
- `strings <mon_fichier>` : Va balayer complètement tout un fichier en affichant toutes les séquences de caractères lisibles qui s'y trouvent. Parfait pour de l'analyse binaire rapide ou pour extraire de l'information (ex. des mots de passes) cachée n'importe où sans faire appel au concept de format.

## Conseil d'audit
Certaines informations ne sont pas visibles sur l'image elle-même, fouillez sous le "capot" !
