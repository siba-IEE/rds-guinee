# Fiche méthodologique : indice de confort thermique (`humidex`)

Conventions communes : voir la fiche [HEP](hep.md).

## 1. Identification

| Champ | Valeur |
|---|---|
| Nom | Indice de confort thermique Humidex |
| Code | `humidex` |
| Unité | °C apparents |
| Famille | grandeur dérivée (stockée) |
| Périodicités | annuel, mensuel (moyenne arithmétique) |

## 2. Définition

Formule de Masterton et Richardson (1979), constantes Magnus standard (17.67 et
243.5) :

```
e = (RH / 100) * 6.112 * exp((17.67 * T) / (T + 243.5))
H = T + (5/9) * (e - 10)
```

Avec :
- `T` : température journalière moyenne en °C ;
- `RH` : humidité relative journalière moyenne en % ;
- `e` : pression de vapeur en hPa ;
- `H` : humidex en °C apparents.

Référence numérique : T = 30 °C, RH = 70 % donne H ≈ 40.95 °C apparents.

## 3. Agrégation

Humidex calculé jour par jour, puis moyenne arithmétique sur la période agrégée
(annuelle ou mensuelle). Un compteur du nombre de jours par an avec H ≥ 40 °C
(seuil d'inconfort modéré, Environnement Canada) est également calculé ; il n'est
pas stocké dans cette version.

## 4. Source amont

`t2m` et `rh2m` journaliers de NASA POWER (paramètres `T2M` et `RH2M`, source
MERRA-2 GMAO).

## 5. Limites et portée

- **Altitude (Fouta-Djalon)** : humidex consomme T2M directement. La
  sous-estimation du différentiel d'altitude par la réanalyse MERRA-2 (voir
  [CAVEATS](../../CAVEATS.md)) affecte Labé (1025 m) et Mamou (782 m), dont les
  valeurs sont biaisées vers le haut par rapport au terrain. La direction
  physique reste préservée : Labé demeure le minimum observé.
- **Pixels météo** : humidex ne consomme pas le GHI ; la co-localisation CERES
  Kindia / Mamou ne s'applique pas. Sur la grille météo MERRA-2, les valeurs
  observées diffèrent (Kindia 34.7, Mamou 30.9), donc des pixels distincts.

## 6. Plages de valeurs

Guinée tropicale attendue : [27, 40] °C apparents selon zone et altitude.

Observé 2021-2025 sur les six villes pilotes :

| Ville | Min | Max | Moyenne | Note |
|---|---:|---:|---:|---|
| Conakry-Kaloum | 37.29 | 38.55 | 37.93 | côtier humide (maximum) |
| Kankan | 32.49 | 33.53 | 33.10 | soudanien sec |
| Kindia | 33.98 | 35.03 | 34.68 | |
| Labé | 29.00 | 29.96 | 29.60 | Fouta-Djalon (minimum) |
| Mamou | 30.26 | 31.14 | 30.89 | |
| Nzérékoré | 31.30 | 32.44 | 32.02 | équatorial humide |

Plage globale [29.0, 38.6]. Conakry-Kaloum domine (côtier humide chaud), Labé au
minimum (altitude, voir limite ci-dessus).

## 7. Références

- Masterton J.M. et Richardson F.A. (1979). *Humidex: A method of quantifying
  human discomfort due to excessive heat and humidity.* Environment Canada,
  Atmospheric Environment Service, CLI 1-79.
- Environnement Canada : grille d'inconfort humidex (40 modéré, 45 élevé, 54+
  danger).
- NASA POWER (MERRA-2) : https://power.larc.nasa.gov/docs/methodology/
- Limites : voir [CAVEATS](../../CAVEATS.md).
