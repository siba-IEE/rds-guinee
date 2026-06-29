# Chaîne de confiance

Chaque donnée du référentiel porte un niveau de confiance. Ce niveau n'est pas
déclaré au cas par cas : il est dérivé de la nature de la mesure et de la
fiabilité de la source. C'est ce qui sépare un référentiel d'un simple entrepôt
de fichiers.

## Trois niveaux

- **A** : mesure directe au sol, issue d'une source de haute fiabilité (station
  radiométrique calibrée). Niveau bancable, rare et ciblé.
- **B** : modèle satellitaire ou réanalyse (NASA POWER, SARAH-3, CAMS, ERA5),
  non validé au sol. Suffisant pour la pré-faisabilité et la comparaison de
  sites.
- **C** : estimation fondée sur la littérature scientifique.

L'essentiel du référentiel est aujourd'hui en B. Le niveau A est limité aux
sites et aux périodes effectivement mesurés.

## Le passeport

Aucune donnée n'entre sans passeport. Cinq champs accompagnent chaque mesure :

- la **source** (origine, référence citable) ;
- la **méthode** de production ou de collecte ;
- le **niveau de confiance** (A, B ou C) ;
- la **période de validité** ;
- l'**incertitude** connue.

Le passeport est le rail qui garde le qualifié qualifié : il rend chaque valeur
traçable et réutilisable en connaissance de cause.

## Comment une donnée monte de B vers A

Le terrain ne remplace pas le satellite, il le calibre. Une station fournit une
vérité de point ; le champ satellite fournit la couverture spatiale et
temporelle. La donnée en confiance A est le champ satellite corrigé par la
mesure au sol, au pixel de la station et sur la période mesurée.

La montée est traçable : la version B reste consultable, la version calibrée
s'ajoute sans rien écraser. Hors du pixel mesuré, la correction se transfère par
analogie climatique, avec une incertitude qui croît avec la distance au point de
mesure. Ce régime intermédiaire est étiqueté comme tel, jamais présenté comme
une mesure.

## Ce que la confiance n'est pas

- Le niveau A n'est pas disponible partout : il exige une mesure au sol.
- Un niveau B n'est pas une erreur : c'est une estimation honnête, bornée par
  ses limites (voir [CAVEATS](../CAVEATS.md)).
- La confiance qualifie la fiabilité d'une mesure, pas la qualité d'un site pour
  le solaire.
