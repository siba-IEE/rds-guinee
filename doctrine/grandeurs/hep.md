# Fiche méthodologique : heures équivalentes pleines (`hep`)

Toute révision de la formule, de la politique de complétude ou des hypothèses
ouvre une nouvelle version et une entrée dans l'historique.

## 1. Identification

| Champ | Valeur |
|---|---|
| Nom | Heures équivalentes pleines |
| Code | `hep` |
| Unité | h_eq (heure équivalente pleine) |
| Famille | grandeur dérivée (stockée) |
| Périodicités | annuel, mensuel |

## 2. Définition

HEP est l'énergie produite par un système photovoltaïque par kilowatt-crête
nominal, exprimée en heures équivalentes pleines. Kuma la publie comme
**ressource solaire**, pas comme productible PV réel.

### 2.1 Définition opérationnelle

Convention : 1 kWh/m²/j équivaut à 1 h_eq/j à 1 kW/m² (conditions standard,
1000 W/m²). Sous cette convention, la valeur journalière de HEP est numériquement
égale à l'irradiation globale horizontale en kWh/m²/j :

```
HEP_jour(t) = GHI_jour(t)
```

L'agrégation temporelle est une somme :

```
HEP_mensuel(année, mois) = somme des HEP_jour(t) sur les jours du mois
HEP_annuel(année)        = somme des HEP_jour(t) sur les jours de l'année
```

## 3. Source amont

| Élément | Valeur |
|---|---|
| Grandeur amont | `ghi` (irradiation globale horizontale journalière) |
| Source | NASA POWER (paramètre `ALLSKY_SFC_SW_DWN`) |
| Méthode satellitaire | CERES SYN1deg et FLASHFlux |
| Résolution native | 1° (environ 110 km à 10° N) |
| Plage couverte | 2021-01-01 au 2025-12-31 |

Attribution NASA POWER : « These data were obtained from the NASA Langley
Research Center (LaRC) POWER Project funded through the NASA Earth Science /
Applied Science Program. »

## 4. Politique de complétude

Règle stricte : 100 % des jours civils.

- **HEP annuel** : inséré si et seulement si la série GHI amont contient
  exactement le nombre de jours civils de l'année (365, ou 366 en année
  bissextile).
- **HEP mensuel** : inséré si et seulement si la série contient exactement le
  nombre de jours du mois.

Si la condition n'est pas remplie, aucune ligne n'est créée : pas d'imputation,
pas de valeur dégradée. Kuma engage son autorité sur la correction du calcul et
ne publie pas ce qui n'est pas complet.

## 5. Hypothèses

- **Conversion STC** : 1 kWh/m²/j équivaut à 1 h_eq/j à 1 kW/m². Équivalence
  exacte sous l'hypothèse d'une production proportionnelle à l'irradiance.
- **Plan horizontal** : HEP intègre l'irradiation globale horizontale. La
  transposition dans le plan incliné des modules relève d'un calcul paramétrable
  distinct.
- **Pas de correction thermique ni de ratio de performance** : HEP ne décote pas
  l'énergie disponible. Ces corrections relèvent de grandeurs dérivées dédiées.

## 6. Limites et portée

- **HEP est une ressource, pas un productible réel.** C'est une borne haute
  théorique : un système réel produit moins (ratio de performance inférieur à 1,
  pertes thermiques, orientation). Kuma porte cette distinction explicitement.
- **Co-localisation Kindia / Mamou** : Kindia (10.06° N, -12.86° E) et Mamou
  (10.37° N, -12.10° E) tombent dans le même pixel CERES SYN1deg (1°), d'où des
  valeurs GHI, donc HEP, identiques. Les quatre autres villes sont dans des
  pixels distincts. Voir [CAVEATS](../../CAVEATS.md).
- **Indépendance vis-à-vis de la température** : HEP n'utilise que le GHI, donc
  la sous-estimation de l'altitude du Fouta-Djalon par la réanalyse météo ne
  l'affecte pas (contrairement aux grandeurs thermiques).
- **Périmètre** : HEP est calculée pour les six villes pilotes (Conakry-Kaloum,
  Kindia, Mamou, Labé, Kankan, Nzérékoré).

## 7. Validation locale

Pas de confrontation à des mesures terrain à ce stade. Quand une source sol se
libérera, une campagne de validation pourra être conduite et documentée, sans
modifier la formule.

## 8. Plages de valeurs

Guinée tropicale (6° N à 12° N) attendue : [1700, 2100] h_eq/an.

Observé 2021-2025 sur les six villes pilotes :

| Ville | Min | Max | Pixel CERES |
|---|---:|---:|---|
| Conakry-Kaloum | 1884 | 1954 | côtier distinct |
| Kindia | 1891 | 2005 | pixel partagé avec Mamou |
| Mamou | 1891 | 2005 | pixel partagé avec Kindia |
| Labé | 1971 | 2056 | Fouta-Djalon distinct |
| Kankan | 1985 | 2060 | intérieur soudanien distinct |
| Nzérékoré | 1727 | 1786 | sud forestier distinct |

Plage globale [1727, 2060] h_eq/an. Nzérékoré au minimum (climat plus nuageux),
Kankan au maximum (ciel plus clair). L'identité « somme des mois = annuel » est
vérifiée.

## 9. Versioning

| Version | Date | Modifications |
|---|---|---|
| v1 | 2026-05 | Définition initiale : agrégation cumulative du GHI, complétude 100 % des jours civils, plan horizontal STC. |

## 10. Auteurs

- v1, 2026-05 : Siba Kalivogui (Kuma Science).

## 11. Références

- NASA POWER : https://power.larc.nasa.gov/docs/methodology/
- CERES SYN1deg : https://ceres.larc.nasa.gov/data/
- Limites : voir [CAVEATS](../../CAVEATS.md).
