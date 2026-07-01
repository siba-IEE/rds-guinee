# Production de la donnée

Les données de ce référentiel ne sont pas assemblées à la main. Elles sont
produites par **Kuma Data Core**, l'infrastructure de Kuma, selon une chaîne
stable et tracée.

## La chaîne

1. **Ingestion.** Les sources sont récupérées depuis leurs fournisseurs
   documentés (NASA POWER, PVGIS-SARAH-3, Copernicus CAMS et ERA5-Land, mesures
   de terrain ESMAP/WAPP), sans retouche manuelle des valeurs.
2. **Qualification.** Chaque mesure reçoit un niveau de confiance (A, B ou C)
   dérivé par des règles fixes selon la nature de la mesure et la fiabilité de la
   source, pas déclaré au cas par cas. Voir la
   [chaîne de confiance](chaine-de-confiance.md).
3. **Versioning non destructif.** Aucune valeur n'est écrasée. Une valeur révisée
   ouvre une nouvelle version ; l'ancienne reste consultable. L'historique est
   intégral.
4. **Audit.** Chaque écriture est journalisée : qui, quand, quoi.
5. **Grandeurs dérivées.** Les grandeurs calculées (voir les
   [fiches de grandeurs](grandeurs/)) sont produites par des méthodes documentées
   à partir des sources, avec les mêmes règles de confiance et de traçabilité.

## Le moteur est propriétaire, la confiance est ouverte

Le moteur qui exécute cette chaîne (ingestion, calcul, versioning, audit,
service) est propriétaire : c'est le savoir-faire de Kuma. Mais rien de ce qui
fonde la confiance n'est caché :

- la **méthode** est documentée (cette doctrine) ;
- la **donnée** est ouverte (CC BY 4.0) et citable (DOI) ;
- des **exemples** reproduisent les résultats à partir de la donnée seule (voir
  `examples/`).

Un tiers peut donc refaire les chiffres sans le moteur. La confiance ne repose
pas sur la parole de Kuma, mais sur la reproductibilité.

## Ce que ce dépôt expose

La donnée, la doctrine et le schéma de référence. Il n'expose pas le moteur
d'ingestion, l'interface de service, ni les outils dérivés.
