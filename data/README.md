# Données

Données solaires et climatiques ouvertes pour les localités guinéennes, couche B
(satellite et réanalyse) sauf indication contraire. Niveaux de confiance et
limites : voir [CAVEATS](../CAVEATS.md) et la
[chaîne de confiance](../doctrine/chaine-de-confiance.md).

## Organisation

- `localites.csv` : référentiel des localités (code, nom, région administrative,
  coordonnées, altitude).
- `nasa-power/` : NASA POWER, mensuel 1991-2020 et journalier 2021-2025.
- À venir : SARAH-3, CAMS, ERA5-Land, terrain Kankan.

Chaque source porte son `ATTRIBUTION.txt`.

## Dictionnaire de données

| Colonne | Description | Unité |
|---|---|---|
| `localite` | code de la localité (voir `localites.csv`) | |
| `annee`, `mois` | période des séries mensuelles | |
| `date` | jour des séries journalières (AAAA-MM-JJ) | |
| `ghi` | irradiation globale horizontale | kWh/m²/jour |
| `dni` | irradiation directe normale | kWh/m²/jour |
| `dhi` | irradiation diffuse horizontale | kWh/m²/jour |
| `kt` | indice de clarté | sans dimension |
| `albedo` | albédo de surface | sans dimension |
| `t2m` | température de l'air à 2 m | °C |
| `rh2m` | humidité relative à 2 m | % |
| `vent_2m`, `vent_10m` | vitesse du vent à 2 m et 10 m | m/s |

## À lire avant usage

- **Confiance B** : données satellitaires et de réanalyse, non validées au sol.
  Suffisant pour la pré-faisabilité et la comparaison de sites, pas pour un
  engagement bancable (voir [CAVEATS](../CAVEATS.md)).
- **Cellules vides** : valeur absente à la source. Pour NASA POWER, `dni`, `kt`
  et `albedo` ne sont disponibles qu'à partir de 2001 dans la série mensuelle.
- **Co-localisation Kindia / Mamou** : ces deux localités partagent le même pixel
  satellitaire (1°) et présentent donc des valeurs de rayonnement identiques.
- **Région administrative** : `localites.csv` indique la région administrative
  (factuelle), pas une région climatique (qui relève d'une analyse, voir la
  doctrine).
