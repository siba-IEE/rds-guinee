# Journal des versions

## 2.0.0 (2026-08-11)

Versement de la profondeur historique NASA POWER, aux 34 localités.

- `nasa-power/mensuel_1981_2025.csv` : séries mensuelles pleine profondeur,
  18 360 lignes, précipitation incluse. Remplace `mensuel_1991_2020.csv` ;
  la fenêtre 1991-2020 reste calculable par simple filtre d'années, comme le
  font les exemples.
- `nasa-power/journalier_1981_1990.csv` à `journalier_2021_2025.csv` : séries
  journalières pleine profondeur, un fichier par décennie, 558 824 lignes au
  total.
- Séries horaires 2001-2025 : 34 fichiers, 7 450 896 pas horaires validés,
  publiés en archive jointe à la release et archivés sur Zenodo. Conventions
  et accès : `data/horaire/README.md`.
- `MANIFEST.csv` : inventaire des fichiers de données avec périodes, comptages
  et sommes de contrôle.
- CAVEATS enrichi : profondeur historique et planchers par paramètre, qualité
  de l'horaire, fraîcheur par source.
- Dictionnaire des données : unités par granularité, colonne `instant_utc`.
- Exemples recalés sur la série longue, fenêtre climatologique 1991-2020
  conservée à l'identique.
- `era5-land/`, `cams/`, `sarah3/`, `terrain-kankan/` : données inchangées.
  Les fichiers sont désormais reproduits à l'identique par un exporteur
  versionné du moteur.

## 1.0.0 (2026-06-30)

Première publication : doctrine, données mensuelles et journalières des 34
localités (NASA POWER, CAMS, ERA5-Land, SARAH-3), premier point de mesure au
sol à Kankan (couche A), exemples sans dépendance.
DOI de version : 10.5281/zenodo.21051755.
