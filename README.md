# RDS Guinée

Référentiel de Données Solaires de la Guinée : des données solaires ouvertes,
qualifiées et documentées, pour le dimensionnement, la recherche et la
planification énergétique.

Licence CC BY 4.0. Publié en versions archivées sous DOI :
[10.5281/zenodo.21051754](https://doi.org/10.5281/zenodo.21051754)
(dernière version : 2.0.1, août 2026).

## Le référentiel en chiffres

| | |
|---|---|
| Mesures publiées | plus de 68 millions |
| Localités | 34 (les chefs-lieux de préfecture et Kaloum) |
| Profondeur historique | 1981 à 2025 selon le paramètre |
| Granularités | mensuel et journalier dans le dépôt, horaire en archive de release |
| Sources | NASA POWER, SARAH-3, CAMS Radiation, CAMS EAC4, ERA5-Land, station au sol |
| Confiance A (mesure au sol) | 1 station, Kankan, campagne ESMAP/WAPP |

Inventaire détaillé, périodes et sommes de contrôle : [MANIFEST.csv](MANIFEST.csv).
Journal des versions : [CHANGELOG.md](CHANGELOG.md).

## Ce que c'est

Un référentiel, pas un entrepôt : l'autorité vient de la qualification de chaque
donnée, pas du volume. Chaque mesure porte un passeport : source, méthode,
niveau de confiance, période de validité, incertitude. Le référentiel dit ce
qu'il sait et ce qu'il ne sait pas.

La Guinée est le pays pilote. La donnée y est ouverte (CC BY 4.0).

## Accéder aux données

- [`data/`](data/) : les séries mensuelles et journalières, en CSV lisibles,
  classées par source ; le dictionnaire des colonnes et des unités est dans
  [`data/README.md`](data/README.md).
- Les séries horaires (63 millions de pas validés) sont publiées en archive
  jointe à chaque release et archivées sur Zenodo : voir
  [`data/horaire/README.md`](data/horaire/README.md).
- [`examples/`](examples/) : des scripts d'utilisation sans aucune dépendance.

## Méthode et confiance

- **B** : données satellitaires et de réanalyse (NASA POWER, SARAH-3, CAMS,
  ERA5), non validées au sol. Suffisant pour la pré-faisabilité et la
  comparaison de sites. C'est l'essentiel du référentiel aujourd'hui.
- **A** : données mesurées au sol et validées. Le référentiel en contient un
  premier point à Kankan (campagne ESMAP/WAPP). Le passage à A ailleurs se fait
  par calage terrain, traçablement.
- **C** : estimations fondées sur la littérature.

Le référentiel assume le B et monte vers le A là où la mesure existe. La
méthode complète est publique : [doctrine/](doctrine/).

Les données sont produites par **Kuma Data Core**, l'infrastructure de Kuma :
ingestion de sources documentées, qualification en confiance (A, B, C),
versioning non destructif, audit. Le moteur est propriétaire ; la méthode et la
donnée, elles, sont ouvertes et reproductibles (voir
[Production de la donnée](doctrine/production-de-la-donnee.md)). Ce dépôt
n'expose pas le moteur d'ingestion, l'interface de service ni les outils dérivés.

## État et feuille de route

Trois versions publiées depuis juin 2026 ; la profondeur historique complète
des sources satellitaires est versée. Viennent ensuite les grandeurs dérivées
(quantiles P50 et P90, climatologies), l'extension de la couche terrain et les
années nouvelles au fil des sources. Détail : [FEUILLE-DE-ROUTE.md](FEUILLE-DE-ROUTE.md).

## Le mot « National »

« National » désigne la couverture du territoire, pas un statut officiel conféré
par l'État. Tant que l'État guinéen n'a pas adopté le référentiel, il est
proposé comme bien commun, pas revendiqué comme référentiel officiel. L'autorité
se gagne par la rigueur et l'usage.

## Citer

> Kalivogui, S. (2026). Référentiel de Données Solaires de la Guinée (RDS Guinée). Kuma Science. https://doi.org/10.5281/zenodo.21051754

Ce DOI pointe toujours vers la dernière version. Chaque version a aussi son
propre DOI : la 1.0.0 correspond à 10.5281/zenodo.21051755, la 2.0.0 à
10.5281/zenodo.21883903, et la 2.0.1 (archive des séries horaires incluse) à
10.5281/zenodo.21895763. Voir aussi [CITATION.cff](CITATION.cff).

## S'impliquer

Une donnée n'entre qu'avec son passeport (source, méthode, confiance, validité).
Le référentiel cherche des chercheurs pour challenger la méthode, des
développeurs pour l'outiller, et des institutions qui veulent des données
solaires dont chaque chiffre s'audite. Voir CONTRIBUTING.md et GOVERNANCE.md,
ou écrire à contact@kumascience.com.

## Sources, limites, licence

- Sources et attributions : SOURCES.md
- Limites documentées : CAVEATS.md
- Licence : CC BY 4.0 (LICENSE). Les sources tierces conservent leur propre
  attribution.
