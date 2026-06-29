# Fiche méthodologique : fraction diffuse de l'irradiation (`fraction_diffuse`)

Conventions communes (versioning, complétude, métadonnées) : voir la fiche
[HEP](hep.md).

## 1. Identification

| Champ | Valeur |
|---|---|
| Nom | Fraction diffuse de l'irradiation |
| Code | `fraction_diffuse` |
| Unité | sans dimension |
| Famille | grandeur dérivée (stockée) |
| Périodicités | annuel, mensuel |

## 2. Définition

Rapport entre l'irradiation diffuse horizontale (DHI) et l'irradiation globale
horizontale (GHI) sur une période :

```
fraction_diffuse(année)       = somme DHI(t) / somme GHI(t),  t sur les jours de l'année
fraction_diffuse(année, mois) = somme DHI(t) / somme GHI(t),  t sur les jours du mois
```

## 3. Source amont

`dhi` et `ghi` journaliers de NASA POWER (paramètres `ALLSKY_SFC_SW_DIFF` et
`ALLSKY_SFC_SW_DWN`). DHI issu de CERES SYN1deg et FLASHFlux. Méthodologie :
https://power.larc.nasa.gov/docs/methodology/

## 4. Politique de complétude

Stricte (100 % des jours civils) sur l'intersection des dates présentes dans DHI
et GHI. Si la somme de GHI sur la période est nulle ou négative (cas
pathologique non observé), la période est écartée.

## 5. Hypothèses

Aucune hypothèse PV : ressource solaire pure, sans paramètre utilisateur. La
cohérence DHI ≤ GHI est garantie par construction, donc `fraction_diffuse`
appartient à [0, 1].

## 6. Limites et portée

- **Co-localisation Kindia / Mamou** : les deux localités tombent dans le même
  pixel CERES SYN1deg (1°, environ 110 km à 10° N), d'où des valeurs identiques.
  Voir [CAVEATS](../../CAVEATS.md).
- **Année 2024 écartée** : une valeur sentinelle observée sur DHI en 2024
  (interruption ponctuelle CERES) conduit à écarter l'année et le mois affectés
  pour les six villes.

## 7. Plages de valeurs

Régime tropical africain attendu : [0.3, 0.6] selon la couverture nuageuse.

Observé 2021-2025 sur les six villes pilotes :

| Ville | Min | Max | Moyenne | Note |
|---|---:|---:|---:|---|
| Conakry-Kaloum | 0.432 | 0.456 | 0.443 | côtier |
| Kankan | 0.439 | 0.458 | 0.448 | soudanien |
| Kindia | 0.443 | 0.457 | 0.452 | pixel partagé avec Mamou |
| Labé | 0.439 | 0.458 | 0.449 | Fouta-Djalon |
| Mamou | 0.443 | 0.457 | 0.452 | pixel partagé avec Kindia |
| Nzérékoré | 0.492 | 0.529 | 0.507 | sud forestier (maximum) |

Plage globale [0.432, 0.529]. Nzérékoré présente la fraction diffuse la plus
élevée (climat équatorial humide), Conakry et Kankan les plus basses (climats
plus secs).

## 8. Références

- NASA POWER : https://power.larc.nasa.gov/docs/methodology/
- CERES SYN1deg : https://ceres.larc.nasa.gov/data/
- Limites : voir [CAVEATS](../../CAVEATS.md).
