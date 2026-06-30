"""Confronter la mesure au sol (couche A) au satellite (couche B) à Kankan.

Compare le GHI journalier mesuré (campagne ESMAP/WAPP) au GHI NASA POWER sur
les jours communs et calcule l'écart moyen. C'est le geste central du
référentiel : juger une source satellitaire à l'aune du terrain.

    python examples/terrain_vs_satellite.py
"""

from __future__ import annotations

import csv
from pathlib import Path
from statistics import mean

DATA = Path(__file__).resolve().parent.parent / "data"
TERRAIN = DATA / "terrain-kankan" / "journalier_2021_2023.csv"
SATELLITE = DATA / "nasa-power" / "journalier_2021_2025.csv"
SITE = "gin_kankan"


def ghi_journalier(chemin: Path, localite: str) -> dict[str, float]:
    serie: dict[str, float] = {}
    with chemin.open(encoding="utf-8") as fichier:
        for ligne in csv.DictReader(fichier):
            if ligne["localite"] == localite and ligne["ghi"]:
                serie[ligne["date"]] = float(ligne["ghi"])
    return serie


def main() -> None:
    sol = ghi_journalier(TERRAIN, SITE)
    satellite = ghi_journalier(SATELLITE, SITE)
    jours = sorted(sol.keys() & satellite.keys())
    if not jours:
        raise SystemExit("Aucun jour commun entre terrain et satellite.")

    moy_sol = mean(sol[jour] for jour in jours)
    moy_sat = mean(satellite[jour] for jour in jours)
    biais = moy_sat - moy_sol

    print(f"GHI journalier moyen à Kankan, {len(jours)} jours communs ({jours[0]} à {jours[-1]})\n")
    print(f"  terrain (A, ESMAP/WAPP)   : {moy_sol:.2f} kWh/m²/jour")
    print(f"  satellite (B, NASA POWER) : {moy_sat:.2f} kWh/m²/jour")
    print(f"  écart satellite - terrain : {biais:+.2f} kWh/m²/jour ({biais / moy_sol:+.1%})")


if __name__ == "__main__":
    main()
