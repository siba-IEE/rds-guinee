# Contribuer au RDS Guinée

Le référentiel accueille des contributions : données, corrections, méthodologie.
La règle est unique et non négociable : rien n'entre sans passeport.

## Le passeport

Toute donnée proposée précise :

- la **source** (origine, référence citable) ;
- la **méthode** de production ou de collecte ;
- le **niveau de confiance** visé (A, B ou C) et sa justification ;
- la **période de validité** ;
- l'**incertitude** connue et ses limites.

Une contribution sans passeport ne peut pas être qualifiée, donc pas intégrée.

## Cheminement d'une contribution

Une contribution entre au statut `brut`. Elle est revue, passe à `validé`, puis
à `publié`. Le niveau de confiance est dérivé de la nature de la mesure, pas
déclaré librement (voir GOVERNANCE.md). La donnée d'un contributeur tiers entre
par défaut en confiance B et au statut `brut` ; elle monte par validation.

## Comment proposer

- Donnée ou correction : ouvrir une issue (des formulaires guident la saisie du
  passeport), puis une pull request.
- Méthodologie : proposer une pull request sur les documents de doctrine, avec
  les références.

## Qualité

Le code et les scripts éventuels suivent le style du dépôt : concis,
idiomatique, commentés seulement là où le pourquoi n'est pas évident.

## Licence des contributions

En contribuant, vous acceptez que votre apport soit publié sous CC BY 4.0, avec
attribution.
