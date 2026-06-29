# Fiche méthodologique : indicateur de qualité des données (`indicateur_qualite_donnees`)

Conventions communes : voir la fiche [HEP](hep.md).

## 1. Identification

| Champ | Valeur |
|---|---|
| Nom | Score éditorial de qualité d'une série mesurée |
| Code | `indicateur_qualite_donnees` |
| Unité | échelle ordinale de 1 à 5 |
| Famille | grandeur dérivée (stockée) |
| Périodicité | statique (une valeur par série sur 2021-2025) |

## 2. Définition

### 2.1 Trois composantes pondérées

Le score continu est une combinaison linéaire de trois composantes normalisées
dans [0, 1] :

| Composante | Définition | Coefficient |
|---|---|---|
| C1, complétude | mesures courantes / jours attendus sur la plage | 0.5 |
| C2, niveau de confiance moyen | moyenne des niveaux des mesures (A = 1.0, B = 0.7, C = 0.4) | 0.3 |
| C3, fiabilité de la source | haute = 1.0, moyenne = 0.7, faible = 0.4 | 0.2 |

```
score_continu = 0.5 * C1 + 0.3 * C2 + 0.2 * C3
```

### 2.2 Projection sur l'échelle 1 à 5

| Score continu | Score discret |
|---|---|
| [0.0, 0.2) | 1 |
| [0.2, 0.4) | 2 |
| [0.4, 0.6) | 3 |
| [0.6, 0.8) | 4 |
| [0.8, 1.0] | 5 |

Intervalles fermés à gauche ; le dernier est fermé à droite pour absorber le cas
d'un score continu égal à 1.0 (série parfaitement complète, mesures toutes en
niveau A, source de fiabilité haute).

## 3. Source amont

L'indicateur ne consomme aucune donnée externe : il agrège des informations déjà
présentes dans le référentiel.

| Lecture | Origine |
|---|---|
| C1 (numérateur) | nombre de mesures courantes de la série |
| C1 (dénominateur) | nombre de jours civils de la plage (1826 sur 2021-2025) |
| C2 | moyenne des niveaux de confiance des mesures courantes |
| C3 | fiabilité de la source de la série |

## 4. Politique de complétude

Non applicable au sens habituel : l'indicateur est lui-même une mesure de la
complétude (composante C1). Aucune série n'est écartée pour incomplétude ; une
série partielle produit simplement un score plus bas.

## 5. Hypothèses

### 5.1 Pondération (0.5, 0.3, 0.2)

La complétude domine (0.5) car elle est la plus discriminante : un trou
systématique sur une saison entière biaise toutes les grandeurs dérivées. Le
niveau de confiance moyen (0.3) et la fiabilité de source (0.2) modulent le
score. La pondération est figée dans cette version.

### 5.2 Conséquence sur le périmètre actuel

Les séries brutes actuelles sont toutes satellitaires (source de fiabilité
haute, niveau de confiance B). Donc C2 = 0.7 et C3 = 1.0 sont constants, et le
score se réduit à :

```
score_continu = 0.5 * C1 + 0.41
```

Le score est alors entièrement porté par la complétude C1.

## 6. Limites et portée

- **Plage effective {3, 4, 5}** : tant que les séries brutes sont toutes
  satellitaires (C2 et C3 constants), les scores 1 et 2 ne sont pas atteignables.
  Une source de fiabilité moindre, ou une série fortement incomplète, étendrait
  la plage.
- **Non appliqué aux grandeurs calculées** : cette version note la qualité des
  séries mesurées, pas des grandeurs dérivées (HEP, fraction diffuse, etc.), dont
  la qualité se lit via celle de leurs entrées.
- **Rattachement** : la ligne porte le score de la série évaluée et référence
  directement cette série mesurée.
- **Pas de fenêtre glissante** : le score est statique sur 2021-2025.
- **Pas d'override** : aucun mécanisme éditorial ne permet de relever ou
  d'abaisser le score au-delà de la formule.

## 7. Plages de valeurs

Échelle complète : 1 à 5. Plage effective théorique sur le périmètre actuel :
{3, 4, 5} (le score minimal vaut 0.41, déjà dans le bin 3).

Observé 2021-2025 sur les séries brutes satellitaires :

- séries complètes (1826/1826 jours) : C1 = 1.0, score continu 0.91, discret 5 ;
- séries à une valeur manquante (1825/1826) : C1 proche de 0.999, score continu
  proche de 0.91, discret 5.

Plage observée : {5}. Toutes les séries brutes actuelles atteignent le maximum,
ce qui reflète leur qualité homogène et élevée. L'arrivée de sources moins
fiables ou de séries incomplètes étendrait la plage.

## 8. Validation locale

Pas de référent terrain : l'indicateur agrège des informations internes. Sa
validité dépend de la justesse de la pondération, révisable en version
ultérieure.

## 9. Versioning

| Version | Date | Modifications |
|---|---|---|
| v1 | 2026-05 | Définition initiale : trois composantes pondérées (0.5, 0.3, 0.2), projection sur l'échelle 1 à 5, périodicité statique. |

## 10. Auteurs

- v1, 2026-05 : Siba Kalivogui (Kuma Science).

## 11. Références

- Fiche [HEP](hep.md) pour les conventions communes.
- Limites : voir [CAVEATS](../../CAVEATS.md).
