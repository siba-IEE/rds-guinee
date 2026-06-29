# Données

Données solaires et climatiques ouvertes pour les localités guinéennes, couche B
(satellite et réanalyse) sauf indication contraire. Niveaux de confiance et
limites : voir [CAVEATS](../CAVEATS.md) et la
[chaîne de confiance](../doctrine/chaine-de-confiance.md).

## Organisation

- `localites.csv` : référentiel des localités (code, nom, région administrative,
  coordonnées, altitude).
- `nasa-power/` : NASA POWER, mensuel 1991-2020 et journalier 2021-2025. La
  série journalière inclut la précipitation (mm/jour) ; la série mensuelle non.
- `cams/` : Copernicus CAMS. Irradiation directe normale (dni) mensuelle
  2004-2023, et particules en suspension (pm10, pm2_5) journalières 2021-2025.
- `era5-land/` : ERA5-Land (réanalyse Copernicus C3S). Rayonnement, température
  et vent, mensuel 2001-2020 et journalier 2021-2025.
- `sarah3/` : PVGIS-SARAH-3 (JRC, CM SAF / EUMETSAT). GHI mensuel 2021-2023.
- `terrain-kankan/` : station de mesure au sol de Kankan (ESMAP / WAPP),
  **couche A**. GHI et DNI, journalier et mensuel, fenêtre 2021-2023.

Chaque source porte son `ATTRIBUTION.txt`. Les couches B (satellite, réanalyse)
sont classées par source ; le terrain est classé par station, chaque station
étant une entité de mesure autonome.

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
| `pm10`, `pm2_5` | particules en suspension (diamètre < 10 µm, < 2,5 µm) | µg/m³ |
| `precipitation` | précipitation corrigée (NASA POWER PRECTOTCORR) | mm/jour |
| `jours` | nombre de jours mesurés dans le mois (terrain) | |

## À lire avant usage

- **Confiance B** : données satellitaires et de réanalyse, non validées au sol.
  Suffisant pour la pré-faisabilité et la comparaison de sites, pas pour un
  engagement bancable (voir [CAVEATS](../CAVEATS.md)).
- **Terrain Kankan (confiance A)** : seule source mesurée au sol. Une seule
  station, sur une fenêtre de deux ans (18 octobre 2021 au 17 octobre 2023), donc
  octobre 2021 et octobre 2023 sont des mois partiels (voir la colonne `jours`).
  Deux ans ne suffisent pas à établir une climatologie de long terme ; cette
  série sert de point d'ancrage pour juger les sources satellitaires sur place,
  pas de référence inter-annuelle.
- **SARAH-3** : couverture limitée à 2021-2023 dans ce dépôt. Rayonnement dérivé
  de Meteosat par un modèle de ciel clair, utile pour recouper NASA POWER et CAMS.
- **Cellules vides** : valeur absente à la source. Pour NASA POWER, `dni`, `kt`
  et `albedo` ne sont disponibles qu'à partir de 2001 dans la série mensuelle.
  Pour CAMS, la `dni` débute en février 2004 (début du service CAMS Radiation).
- **Co-localisation Kindia / Mamou** : ces deux localités partagent le même pixel
  satellitaire (1°, NASA POWER) et présentent donc des valeurs de rayonnement
  identiques. Les pixels CAMS et ERA5-Land sont plus fins.
- **DNI CAMS** : l'irradiation directe est plus sensible aux aérosols que le GHI.
  En Guinée, le panache de poussière de l'Harmattan (saison sèche) peut induire
  une surestimation de la `dni` CAMS. À recouper avec les `pm10` du même service.
- **Rayonnement ERA5-Land** : issu d'une réanalyse, il porte un biais connu sous
  ciel nuageux et reste une donnée de couche B. NASA POWER (CERES) et CAMS sont
  préférables pour le rayonnement ; ERA5-Land complète sur la température et le
  vent, et étend la profondeur historique.
- **Région administrative** : `localites.csv` indique la région administrative
  (factuelle), pas une région climatique (qui relève d'une analyse, voir la
  doctrine).
