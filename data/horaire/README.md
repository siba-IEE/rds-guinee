# Données horaires

Les séries horaires ne sont pas stockées dans ce dépôt : leur volume (63,5
millions de pas validés pour la seule source NASA POWER) rendrait le clonage
pénible sans rien apporter à la lisibilité. Elles sont publiées en archive
jointe à chaque release et archivées sur Zenodo avec le reste de
l'instantané : https://doi.org/10.5281/zenodo.21051754 (le DOI concept pointe
la dernière version).

## Contenu de l'archive

Un fichier CSV par localité, classé par source :

    horaire/nasa-power/gin_beyla_2001_2025.csv
    horaire/nasa-power/gin_boffa_2001_2025.csv
    ...

34 localités (les chefs-lieux de préfecture et Kaloum), 9 paramètres, du
1er janvier 2001 au 31 décembre 2025. Les sommes de contrôle de l'archive et
de chaque fichier figurent dans MANIFEST.csv à la racine de la release.

## Conventions horaires

- La colonne temporelle est `instant_utc`, au format ISO 8601 avec décalage
  explicite (`2021-01-01T00:00:00+00:00`). L'horodatage marque le début du
  pas horaire. La Guinée étant à UTC+0, l'heure UTC est l'heure locale.
- Les colonnes sont `ghi`, `dni`, `dhi`, `kt`, `t2m`, `rh2m`, `vent_2m`,
  `vent_10m`, `precipitation`.
- Les unités horaires diffèrent des unités journalières : les irradiations
  `ghi`, `dni`, `dhi` sont en Wh/m² par pas horaire, la précipitation en
  mm/h. Température, humidité, vents et indice de clarté gardent leurs unités
  habituelles (°C, %, m/s, sans dimension).
- Seuls les pas validés par le contrôle de qualité (bornes physiques et tests
  de cohérence du réseau BSRN, appliqués pas par pas) sont publiés. Une ligne
  absente est un pas rejeté ou non défini, jamais une valeur nulle implicite.
- L'indice de clarté n'est défini que de jour ; la cellule est vide la nuit.
- Le rayonnement vaut réellement zéro la nuit : ce sont des valeurs, pas des
  manquants.

## Limites

Voir CAVEATS.md à la racine du dépôt, en particulier la co-localisation de
pixel (grille de rayonnement à 1°) et la qualité de l'horaire.
