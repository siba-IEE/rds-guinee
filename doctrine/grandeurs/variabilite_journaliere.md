# Fiche méthodologique : indice de variabilité journalière (`variabilite_journaliere`)

Conventions communes : voir la fiche [HEP](hep.md).

## 1. Identification

| Champ | Valeur |
|---|---|
| Nom | Indice de variabilité journalière (coefficient de variation) |
| Code | `variabilite_journaliere` |
| Unité | sans dimension |
| Famille | grandeur dérivée (stockée) |
| Périodicités | annuel uniquement (voir section 4) |

## 2. Définition

Coefficient de variation (CoV) du GHI journalier sur une année :

```
CoV(année) = écart-type(GHI_jour sur l'année) / moyenne(GHI_jour sur l'année)
```

Écart-type de population (divisé par N) et moyenne arithmétique. Indicateur
statistique standard, sans dimension.

## 3. Source amont

`ghi` journalier de NASA POWER (paramètre `ALLSKY_SFC_SW_DWN`).

## 4. Périodicité annuelle uniquement

Pas de calcul mensuel : un mois (28 à 31 jours) est statistiquement peu robuste
pour un coefficient de variation, qui demande typiquement au moins 30
observations. L'année (365 à 366 jours) satisfait cette condition.

## 5. Politique de complétude

Stricte (100 % des jours civils). Si une année manque un jour de GHI, elle est
écartée. Si la moyenne de GHI est nulle ou négative (cas pathologique non
observé), l'année est écartée (CoV non défini).

## 6. Interprétation

- CoV proche de 0.15 : climat très stable (équatorial humide, irradiation
  régulière).
- CoV proche de 0.25 : transition saisonnière marquée (côtier tropical).
- CoV de 0.40 et plus : forte variabilité (latitudes moyennes).

Utilité principale : le dimensionnement des systèmes avec stockage. Un CoV élevé
implique un stockage plus grand pour lisser la production.

## 7. Limites et portée

- **Co-localisation Kindia / Mamou** : les deux localités partagent le même pixel
  CERES SYN1deg, d'où un CoV identique (0.190 pour les deux). Voir
  [CAVEATS](../../CAVEATS.md).
- **Choix de l'estimateur** : l'écart-type de population (divisé par N) est
  retenu. L'estimateur d'échantillon (divisé par N-1) donnerait des valeurs très
  légèrement supérieures (environ 0.1 % sur 365 observations), différence non
  discriminante à cette échelle.

## 8. Plages de valeurs

Climatologie solaire intertropicale attendue : [0.10, 0.40] selon zone.

Observé 2021-2025 sur les six villes pilotes :

| Ville | Min | Max | Moyenne | Climat |
|---|---:|---:|---:|---|
| Conakry-Kaloum | 0.212 | 0.269 | 0.237 | côtier (maximum) |
| Kankan | 0.171 | 0.193 | 0.179 | soudanien |
| Kindia | 0.177 | 0.207 | 0.190 | pixel partagé avec Mamou |
| Labé | 0.180 | 0.220 | 0.194 | Fouta-Djalon |
| Mamou | 0.177 | 0.207 | 0.190 | pixel partagé avec Kindia |
| Nzérékoré | 0.156 | 0.192 | 0.177 | équatorial humide (minimum) |

Plage globale [0.156, 0.269]. Conakry-Kaloum présente le CoV le plus élevé
(saison sèche et humide marquées), Nzérékoré le plus bas (climat équatorial
humide plus stable).

## 9. Références

- Coefficient de variation : statistique classique.
- Variability Index : concept apparenté (PVsyst, Solargis) pour le
  dimensionnement PV.
- NASA POWER : https://power.larc.nasa.gov/docs/methodology/
- Limites : voir [CAVEATS](../../CAVEATS.md).
