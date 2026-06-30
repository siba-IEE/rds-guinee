"""Comparer le gisement solaire de plusieurs localités (pré-faisabilité).

Classe les localités par GHI annuel moyen (NASA POWER, 1991-2020). Sert à
hiérarchiser des sites candidats avant une étude de faisabilité.

    python examples/comparer_sites.py [code_localite ...]
    python examples/comparer_sites.py gin_kankan gin_labe
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean

DONNEES = Path(__file__).resolve().parent.parent / "data" / "nasa-power" / "mensuel_1991_2020.csv"
PILOTES = [
    "gin_conakry_kaloum",
    "gin_kindia",
    "gin_mamou",
    "gin_labe",
    "gin_kankan",
    "gin_nzerekore",
]


def ghi_annuel_moyen(localites: set[str]) -> dict[str, float]:
    valeurs: dict[str, list[float]] = defaultdict(list)
    with DONNEES.open(encoding="utf-8") as fichier:
        for ligne in csv.DictReader(fichier):
            if ligne["localite"] in localites and ligne["ghi"]:
                valeurs[ligne["localite"]].append(float(ligne["ghi"]))
    return {localite: mean(serie) for localite, serie in valeurs.items()}


def main() -> None:
    parseur = argparse.ArgumentParser(description="Classement de localités par GHI annuel moyen.")
    parseur.add_argument(
        "localites",
        nargs="*",
        default=PILOTES,
        help="codes de localités (défaut : les six villes pilotes)",
    )
    localites = parseur.parse_args().localites

    moyennes = ghi_annuel_moyen(set(localites))
    if not moyennes:
        raise SystemExit("Aucune donnée pour ces localités (voir data/localites.csv).")

    print("GHI annuel moyen (kWh/m²/jour), NASA POWER 1991-2020\n")
    classement = sorted(moyennes.items(), key=lambda paire: paire[1], reverse=True)
    for rang, (localite, valeur) in enumerate(classement, 1):
        print(f"  {rang}. {localite:<22} {valeur:5.2f}")


if __name__ == "__main__":
    main()
