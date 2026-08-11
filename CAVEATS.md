# Limites documentées

Le référentiel dit ce qu'il ne sait pas. Les limites ci-dessous bornent l'usage
de certaines grandeurs et doivent accompagner toute réutilisation.

## Confiance et validation

L'essentiel du référentiel est en confiance B : satellite et réanalyse, non
validés au sol. Sauf mention explicite de confiance A, une valeur n'est pas une
mesure terrain. La divergence entre sources mesure un désaccord inter-source
relatif, pas une erreur absolue contre le sol.

## P50 et P90

Les quantiles d'irradiation exposés sont inter-annuels : ils ne propagent pas
l'incertitude de modèle. Ils ne constituent pas un P90 bancable au sens d'un
financement de projet, lequel exige une validation au sol et un budget
d'incertitude complet.

## Co-localisation de pixel

À la résolution de certaines grilles satellitaires (1°), des localités voisines
partagent la même cellule et reçoivent une valeur identique. C'est le cas de
Kindia et Mamou sur la grille NASA POWER. La valeur n'est alors pas
spatialement résolue entre ces sites.

## Salissure et correction thermique

Le taux de salissure exposé est un proxy dérivé de l'aérosol, pas une mesure
d'encrassement. La correction thermique repose sur un modèle standard, non
calibré localement. Ces grandeurs sont indicatives.

## Profondeur historique

La profondeur des séries suit la disponibilité réelle de chaque paramètre chez
le producteur. Chez NASA POWER : la météo (température, humidité, vent,
précipitation) remonte à 1981, le rayonnement global et diffus à 1984, et le
rayonnement direct, l'indice de clarté et l'albédo à 2001 seulement, date du
début des observations du capteur CERES. Avant ces dates, les cellules sont
vides. Les années les plus anciennes reposent sur des jeux satellitaires plus
anciens, moins bien contraints que la période récente, et l'homogénéité d'une
série longue repose sur l'harmonisation interne du producteur.

## Qualité de l'horaire

Les séries horaires publiées sont passées par un contrôle de qualité pas par
pas (bornes physiques et tests de cohérence du réseau BSRN). Seuls les pas
validés sont publiés : 9 201 pas rejetés sur 63,5 millions restent hors
publication, soit 0,014 pour cent. L'indice de clarté n'est défini que de
jour ; les pas nocturnes n'existent pas pour cette colonne. Les unités
horaires diffèrent des unités journalières : voir le dictionnaire des données.

## Fraîcheur par source

Chaque série s'arrête à la dernière date servie par sa source au moment de la
capture. Les particules fines (CAMS EAC4) s'arrêtent au 31 août 2025, la
réanalyse ayant plusieurs mois de latence. Le rayonnement horaire NASA POWER a
quelques semaines de retard sur le temps réel.

## Profondeur terrain

La couche de confiance A est limitée aux sites et périodes effectivement
mesurés. Ailleurs, le référentiel reste en B, ou en B calibré par analogie, avec
une incertitude croissant avec la distance climatique au point de mesure.
