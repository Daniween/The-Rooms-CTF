# Fiche Pratique : Injection SQL avec SQLMap

## Le concept

Une **injection SQL** se produit lorsqu'une application web intègre directement une entrée utilisateur dans une requête SQL sans la valider ni l'échapper. L'attaquant peut alors manipuler la requête pour lire des données arbitraires, modifier la base de données, ou contourner l'authentification.

Exemple de code vulnérable (Python/Flask) :
```python
# VULNERABLE — entrée utilisateur directement dans la requête
query = f"SELECT * FROM employees WHERE id = {user_input}"
```

Exemple de code sécurisé (requête paramétrée) :
```python
# SÉCURISÉ — paramètre lié séparément
cursor.execute("SELECT * FROM employees WHERE id = ?", (user_input,))
```

## SQLMap

**SQLMap** est un outil open-source qui automatise la détection et l'exploitation des injections SQL. Il supporte tous les grands systèmes de gestion de bases de données (MySQL, PostgreSQL, SQLite, MSSQL, Oracle, etc.).

### Commandes essentielles

```bash
# Tester une URL pour détecter une injection SQL
sqlmap -u "http://cible/search?id=1"

# Lister les bases de données disponibles
sqlmap -u "http://cible/search?id=1" --dbs

# Lister les tables d'une base de données
sqlmap -u "http://cible/search?id=1" -D nom_bdd --tables

# Lister les colonnes d'une table
sqlmap -u "http://cible/search?id=1" -D nom_bdd -T nom_table --columns

# Extraire le contenu d'une table
sqlmap -u "http://cible/search?id=1" -D nom_bdd -T nom_table --dump

# Mode non-interactif (répond automatiquement aux questions)
sqlmap -u "http://cible/search?id=1" --tables --batch
```

### Options utiles

| Option | Description |
|--------|-------------|
| `--batch` | Mode automatique, n'interrompt pas pour confirmation |
| `--dbs` | Enumère les bases de données |
| `--tables` | Liste les tables |
| `--dump` | Extrait les données |
| `--level=5` | Augmente l'intensité des tests |
| `--risk=3` | Augmente les types d'injections testées |
| `--dbms=sqlite` | Spécifie le SGBD cible |

## Conseil d'audit

Cherchez toujours les paramètres GET/POST qui semblent correspondre à un identifiant ou à un filtre de recherche (`id=`, `user=`, `category=`). Ce sont les candidats les plus fréquents aux injections SQL.
