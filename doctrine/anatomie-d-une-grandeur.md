# Anatomie d'une grandeur

Une grandeur est une quantité physique rattachée à une localité et à un temps :
irradiation, température, vent, ou une quantité dérivée comme le productible. Le
référentiel n'expose pas des chiffres nus, mais des grandeurs qualifiées.

## Ce qui caractérise une grandeur

- un **code** stable et une **unité** ;
- une **localité** et une **granularité temporelle** (horaire, journalière,
  mensuelle, climatologique) ;
- une **source** et une **méthode** ;
- un **niveau de confiance** et une **incertitude** ;
- un **statut éditorial** (brut, validé, publié) et une **période de validité**.

C'est le passeport décrit dans la [chaîne de confiance](chaine-de-confiance.md).

## Grandeurs brutes et grandeurs dérivées

- Les **grandeurs brutes** viennent directement d'une source, par exemple
  l'irradiation globale horizontale d'un produit satellitaire.
- Les **grandeurs dérivées** sont calculées à partir des brutes par une méthode
  documentée, par exemple l'irradiation dans le plan des modules, le
  productible, ou la fraction diffuse.

Une grandeur dérivée n'invente pas d'information : elle hérite des sources et des
limites des grandeurs qui la composent.

## Limites attachées

Toute grandeur porte ses limites connues. Une grandeur dérivée d'un modèle non
calibré localement, ou d'un quantile inter-annuel, le dit explicitement. Les
limites transversales sont rassemblées dans [CAVEATS](../CAVEATS.md).
