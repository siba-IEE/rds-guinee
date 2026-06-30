# Feuille de route

Le RDS Guinée est un bien commun à vocation territoriale : couvrir la ressource
solaire de tout le pays, de façon ouverte, qualifiée et documentée. Le
référentiel grandit par la qualification de la donnée, pas par son volume, et
selon le besoin public.

## Trois couches

Le référentiel se construit en couches superposées, pas en une seule passe.

1. **Couverture territoriale** (satellite et réanalyse). Une valeur de ressource
   pour chaque localité du pays, à la résolution honnête de la source. La
   densification fine s'appuie sur PVGIS-SARAH-3 (environ 5 km) et ERA5-Land
   (environ 9 km), qui distinguent réellement des sites voisins. NASA POWER
   apporte la profondeur historique longue, à sa résolution plus grossière
   (environ 110 km, où des localités proches partagent une même valeur).
2. **Vérité locale** (mesure au sol). Là où une station de mesure existe, elle
   ancre le satellite et élève la confiance de la zone. Le référentiel ne compte
   aujourd'hui qu'un seul point au sol (Kankan). C'est sa frontière la plus
   précieuse à étendre.
3. **Produits par site**. Là où l'historique le permet : statistiques de
   dépassement (P50, P90), année météorologique type (TMY, propre à chaque
   site), grandeurs métier dérivées.

## Pourquoi

Un développeur de centrale ou de mini-réseau, un chercheur, un planificateur qui
travaille sur un site guinéen n'a pas aujourd'hui de ressource solaire ouverte,
documentée et ancrée localement. Le RDS la fournit, en disant ce qu'il sait et
ce qu'il ne sait pas. Sa couverture vise le territoire entier, pas un
échantillon de villes.

## Comment contribuer, et pourquoi telle contribution

Le référentiel progresse par contributions ciblées, chacune comblant un manque
déclaré. Les profils attendus ne sont pas seulement des développeurs.

- **Porteur de mesure au sol** (métrologie, institution, projet instrumenté). Le
  référentiel n'a qu'un point au sol. Une série mesurée (pyranomètre, station)
  dans une localité non couverte crée un nouveau point de confiance haute et
  permet de juger le satellite dans une nouvelle zone climatique.
- **Spécialiste du calage** (géostatistique, télédétection). La correction du
  satellite par la mesure au sol, et son transfert raisonné aux sites voisins,
  est posée mais pas outillée. Un calage validé (par exemple par validation
  croisée sur les stations régionales d'Afrique de l'Ouest) transforme un point
  au sol en valeur de zone, avec un résidu documenté.
- **Chercheur, analyste de données**. Plusieurs produits manquent ou demandent
  validation : l'année type (TMY) par site, la confirmation des biais satellite
  en saison sèche, l'extension des grandeurs dérivées. Sujets publiables et
  utiles au pays.
- **Bureau d'études, développeur**. En signalant un site d'intérêt ou en versant
  sa propre mesure, il oriente la densification vers les zones où le besoin est
  réel.

## Ce dont le référentiel a besoin

Par ordre de priorité :

1. **Des points de mesure au sol hors Kankan**, en particulier sur la côte, dans
   le Sud forestier et sur le Fouta-Djalon. C'est le besoin le plus structurant.
2. **Une année météorologique type (TMY) par site**, construite sur un
   historique horaire et calée au sol là où c'est possible.
3. **Une méthode de calage et de transfert spatial** validée, pour passer d'un
   point au sol à une valeur de zone honnête.
4. **La confirmation des biais satellite**, notamment sur l'irradiation directe
   en saison sèche (panache de poussière de l'Harmattan).
5. **La densification territoriale fine** des localités encore absentes, à
   partir des sources à fine résolution.
6. **Les demandes de sites** des utilisateurs, pour prioriser cette
   densification.

Ces besoins sont suivis comme des tickets ouverts (issues), étiquetés par type
de contribution.

## Ce qui n'est pas (encore) au programme

- **La résolution n'est pas inventée.** Deux localités dans une même maille
  satellitaire partagent la même valeur tant qu'aucune mesure au sol ne les
  distingue. Le référentiel le signale plutôt que de simuler une précision qu'il
  n'a pas.
- **Les calculs paramétrables** (productible en plan incliné, ratio de
  performance, correction thermique, degrés-jours) dépendent d'hypothèses
  propres à chaque projet (orientation, matériel). Ils relèvent d'un calcul, pas
  d'une donnée figée : le référentiel en fournit des exemples reproductibles
  (voir `examples/`) plutôt qu'un moteur.
- **Les autres dimensions de l'énergie** (infrastructure de réseau, équipements,
  économie, usages) sont un horizon, pas le périmètre actuel. Le référentiel
  couvre d'abord la ressource solaire, sur tout le territoire.
