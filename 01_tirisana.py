from pathlib import Path
import pandas as pd

mape  = Path(__file__).resolve().parent
avots =  mape / "dati" / "penguins.csv"
merijumi = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]

dati = pd.read_csv(avots)
sakuma  = len(dati)
dati["avota_rinda"] = dati.index + 2  # csv pirmaja rinda ir kolonnu nosaukumi

nav_dzimuma = int(dati["sex"].isna().sum())
for kolonna in merijumi:
    dati[kolonna] = pd.to_numeric(dati[kolonna], errors="coerce")

# iznemu rindas kuras modelim neder
nav_sugas  =  dati["species"].isna()
bez_sugas = int(nav_sugas.sum())
dati = dati.loc[~nav_sugas].copy()

nav_merijumu = dati[merijumi].isna().any(axis=1)
bez_merijumiem = int(nav_merijumu.sum())
dati = dati.loc[~nav_merijumu].copy()

tirie =  dati[["avota_rinda", "species", *merijumi]].copy( )
tirie.to_csv(mape / "tirs.csv", index=False)

print("Datu tīrīšana")
print(f"sākumā: {sakuma} beigas: {len(tirie)}")
print(f"bez sugas: {bez_sugas} bez merijumiem: {bez_merijumiem}")
print(f"kopa izmestas: {sakuma - len(tirie)}")
print(f"bez dzimuma bija {nav_dzimuma} rindas tas nedzesu jo dzimumu neizmantoju")
print("saglabats tirs.csv")
