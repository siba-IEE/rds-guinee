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

## Profondeur terrain

La couche de confiance A est limitée aux sites et périodes effectivement
mesurés. Ailleurs, le référentiel reste en B, ou en B calibré par analogie, avec
une incertitude croissant avec la distance climatique au point de mesure.
