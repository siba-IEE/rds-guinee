# Gouvernance

## Principe

L'autorité du référentiel vient de la qualification, pas du volume. Le rôle de
la gouvernance est de garder le qualifié qualifié.

## Statut éditorial

Chaque donnée suit un cycle : `brut` (entrée), `validé` (revue passée), `publié`
(exposé dans le référentiel). Le versioning est non destructif : une valeur
révisée ouvre une nouvelle version, l'ancienne reste consultable.

## Niveaux de confiance

Le niveau A/B/C est dérivé de la nature de la mesure et de la fiabilité de la
source, selon des règles fixes, pas déclaré au cas par cas :

- **A** : mesure directe au sol, source de haute fiabilité.
- **B** : modèle satellitaire ou réanalyse.
- **C** : estimation fondée sur la littérature.

Le niveau A est réservé à la mesure terrain validée. Aucune donnée n'est promue
en A sans validation au sol.

## Validation et intégration

Kuma Science opère le référentiel et assure la validation éditoriale. Les
contributions tierces entrent en `brut` et sont validées selon les mêmes règles
que la donnée interne. L'ouverture du processus est volontaire : le
multi-contributeur est la forme attendue.

## Attribution

Tout apport conserve son attribution. Les sources tierces gardent la leur, comme
détaillé dans SOURCES.md.
