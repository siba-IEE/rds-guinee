# Exemples d'utilisation

Scripts courts pour lire et exploiter les données du référentiel. Ce sont des
exemples de **consommation** de la donnée ouverte, pas le moteur du référentiel.

Aucune dépendance : Python 3 et sa bibliothèque standard suffisent. Lancer
depuis la racine du dépôt.

## Scripts

| Script | Ce qu'il montre |
|---|---|
| `resume_site.py` | Climatologie mensuelle du GHI d'une localité (NASA POWER, 1991-2020). |
| `comparer_sites.py` | Classement de localités par GHI annuel moyen (pré-faisabilité). |
| `terrain_vs_satellite.py` | Écart entre la mesure au sol (couche A) et le satellite (couche B) à Kankan. |

## Exemples

```
$ python examples/comparer_sites.py
GHI annuel moyen (kWh/m²/jour), NASA POWER 1991-2020

  1. gin_labe                5.60
  2. gin_kankan              5.59
  3. gin_kindia              5.43
  4. gin_mamou               5.43
  5. gin_conakry_kaloum      5.24
  6. gin_nzerekore           4.78
```

```
$ python examples/terrain_vs_satellite.py
GHI journalier moyen à Kankan, 730 jours communs (2021-10-18 à 2023-10-17)

  terrain (A, ESMAP/WAPP)   : 5.41 kWh/m²/jour
  satellite (B, NASA POWER) : 5.56 kWh/m²/jour
  écart satellite - terrain : +0.15 kWh/m²/jour (+2.8%)
```

`resume_site.py` et `comparer_sites.py` acceptent des codes de localité en
argument (voir `data/localites.csv`). Sans argument, ils prennent Kankan et les
six villes pilotes respectivement.

## Avec pandas

Les mêmes calculs tiennent en une ligne pour qui utilise pandas. Par exemple, la
climatologie mensuelle d'un site :

```python
import pandas as pd
df = pd.read_csv("data/nasa-power/mensuel_1991_2020.csv")
df[df.localite == "gin_kankan"].groupby("mois")["ghi"].mean()
```
