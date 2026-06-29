# Fiche méthodologique : productible spécifique théorique (`productible_specifique_theorique`)

Conventions communes : voir la fiche [HEP](hep.md).

## 1. Identification

| Champ | Valeur |
|---|---|
| Nom | Productible spécifique théorique |
| Code | `productible_specifique_theorique` |
| Unité | kWh/kWc |
| Famille | grandeur dérivée (stockée) |
| Périodicités | annuel, mensuel (héritées de `hep`) |

## 2. Définition

```
productible_specifique_theorique(période) = hep(période) * pr_theorique
```

Avec `pr_theorique = 0.8` par défaut, valeur conservatrice cohérente avec
IEC 61724-1 et les pratiques des bureaux d'études.

## 3. Choix du ratio de performance théorique

`0.8` est une valeur conservatrice, cohérente avec :

- IEC 61724-1:2021 (*Photovoltaic system performance, Part 1*) ;
- NREL PVWatts (ratio de performance par défaut autour de 0.84) ;
- les pratiques des bureaux d'études (0.75 à 0.85 pour des installations fixes
  inclinées).

Elle permet la comparaison avec les outils tiers (PVGIS, NREL). Le ratio de
performance réel d'un projet relève d'un calcul paramétrable, hors du périmètre
de cette grandeur.

## 4. Source amont

`hep` (grandeur dérivée calculée par le référentiel). C'est une grandeur calculée
à partir d'une autre grandeur calculée.

## 5. Politique de complétude

Héritée de `hep` : si `hep` est absent pour une localité et une période,
`productible_specifique_theorique` l'est aussi par construction.

## 6. Hypothèses

- Convention STC héritée de HEP : 1 kWh/m²/j équivaut à 1 heure équivalente à
  1 kW/m².
- `pr_theorique = 0.8` capture les pertes système agrégées (onduleur, câblage,
  écarts entre modules, salissure et ombrage typiques).
- Plan horizontal (pas de transposition dans le plan des modules à ce stade).
- Pas de correction thermique.

## 7. Limites et portée

- **Ratio de performance fixe** : `0.8` n'est pas paramétrable ici. Un système
  réel peut présenter un ratio entre 0.65 et 0.92 selon la technologie, le
  climat et la conception.
- **Co-localisation Kindia / Mamou** : la grandeur dérive de HEP, donc les
  valeurs sont identiques pour ces deux localités (pixel CERES partagé). Voir
  [CAVEATS](../../CAVEATS.md).

## 8. Plages de valeurs

Guinée tropicale, ratio 0.8 attendu : [1360, 1680] kWh/kWc/an.

Observé 2021-2025 sur les six villes pilotes :

| Ville | Min | Max | Moyenne |
|---|---:|---:|---:|
| Conakry-Kaloum | 1507 | 1563 | 1535 |
| Kankan | 1588 | 1648 | 1623 |
| Kindia | 1513 | 1604 | 1566 |
| Labé | 1577 | 1645 | 1615 |
| Mamou | 1513 | 1604 | 1566 |
| Nzérékoré | 1381 | 1429 | 1402 |

Plage globale [1381, 1648] kWh/kWc/an, cohérente avec HEP multiplié par 0.8.

## 9. Références

- IEC 61724-1:2021 (*Photovoltaic system performance, Part 1: Monitoring*).
- NREL PVWatts (ratio de performance par défaut).
- Limites : voir [CAVEATS](../../CAVEATS.md).
