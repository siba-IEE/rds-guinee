# RDS Guinée

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21051754.svg)](https://doi.org/10.5281/zenodo.21051754)

Référentiel de Données Solaires de la Guinée. Données solaires ouvertes,
qualifiées et documentées, pour le dimensionnement, la recherche et la
planification énergétique.

## Ce que c'est

Un référentiel, pas un entrepôt : l'autorité vient de la qualification de chaque
donnée, pas du volume. Chaque mesure porte un passeport : source, méthode,
niveau de confiance, période de validité, incertitude. Le référentiel dit ce
qu'il sait et ce qu'il ne sait pas.

La Guinée est le pays pilote. La donnée y est ouverte (CC BY 4.0).

## Niveaux de confiance

- **B** : données satellitaires et de réanalyse (NASA POWER, SARAH-3, CAMS,
  ERA5), non validées au sol. Suffisant pour la pré-faisabilité et la
  comparaison de sites. C'est l'essentiel du référentiel aujourd'hui.
- **A** : données mesurées au sol et validées. Le référentiel en contient un
  premier point à Kankan (campagne ESMAP/WAPP). Le passage à A ailleurs se fait
  par calage terrain, traçablement.
- **C** : estimations fondées sur la littérature.

Le référentiel assume le B et monte vers le A là où la mesure existe.

## Périmètre

Ce dépôt contient :

- la **doctrine** : conventions, méthodologie de calage, contrôle qualité,
  fiches de grandeurs ;
- les **données** ouvertes des localités solaires guinéennes, par source, avec
  leur attribution ;
- le **schéma** de référence ;
- des **exemples** d'utilisation sans dépendance (`examples/`).

Il ne contient pas le moteur d'ingestion ni les outils dérivés.

## Le mot « National »

« National » désigne la couverture du territoire, pas un statut officiel conféré
par l'État. Tant que l'État guinéen n'a pas adopté le référentiel, il est
proposé comme bien commun, pas revendiqué comme référentiel officiel. L'autorité
se gagne par la rigueur et l'usage.

## Utiliser et citer

Les données sont publiées en instantanés versionnés, chacun archivé sur Zenodo
avec un identifiant persistant (DOI).

Citation :

> Kalivogui, S. (2026). Référentiel de Données Solaires de la Guinée (RDS Guinée). Kuma Science. https://doi.org/10.5281/zenodo.21051754

Ce DOI pointe toujours vers la dernière version. Chaque version a aussi son
propre DOI : la 1.0.0 correspond à 10.5281/zenodo.21051755.

## Contribuer

Une donnée n'entre qu'avec son passeport (source, méthode, confiance, validité).
Voir CONTRIBUTING.md et GOVERNANCE.md.

## Sources, limites, licence

- Sources et attributions : SOURCES.md
- Limites documentées : CAVEATS.md
- Licence : CC BY 4.0 (LICENSE). Les sources tierces conservent leur propre
  attribution.

## Contact

contact@kumascience.com
