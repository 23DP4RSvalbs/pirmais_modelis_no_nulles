from pathlib import Path
import pandas as pd

mape  = Path(__file__).resolve().parent
avots =  mape / "dati" / "penguins.csv"
merijumi = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]

dati = pd.read_csv(avots)
sakuma  = len(dati)
# originala csv rindas numurs, lai vares atrast kludu (+2 jo pirma rinda ir nosaukumi)
dati["avota_rinda"] = dati.index + 2

# dzimumam trukst 11 vertibas, bet to neizmantoju, tapec tikai saskaitu
nav_dzimuma = int(dati["sex"].isna().sum())
# trukstosas vertibas ir rakstitas ka NA, tapec merijumus parveidoju par skaitliem
for kolonna in merijumi:
    dati[kolonna] = pd.to_numeric(dati[kolonna], errors="coerce")

# suga ir tas ko prognozeju, tapec rinda bez sugas neder (sajos datos tadu nebija)
nav_sugas  =  dati["species"].isna()
bez_sugas = int(nav_sugas.sum())
dati = dati.loc[~nav_sugas].copy()

# divam rindam visi 4 merijumi ir NA, tadas modelim neder
nav_merijumu = dati[merijumi].isna().any(axis=1)
bez_merijumiem = int(nav_merijumu.sum())
dati = dati.loc[~nav_merijumu].copy()

# knabja garums vai svars nevar but 0 vai negativs, parbaudiju vai tadu nav (nebija)
slikti_merijumi = (dati[merijumi] <= 0).any(axis=1)
slikti = int(slikti_merijumi.sum())
dati = dati.loc[~slikti_merijumi].copy()

# parbaudu vai kads pingvins nav ierakstits divreiz, lai tas nebutu gan trenina, gan testa datos (nebija)
dublikati =   dati.duplicated(subset=["species", "island", *merijumi, "sex", "year"])
dublikatu_skaits = int(dublikati.sum())

dati = dati.loc[~dublikati].copy()

# tirs.csv liku tikai sugu un 4 merijumus, jo tikai tos lietoju modelim
tirie =  dati[["avota_rinda", "species", *merijumi]].copy( )
tirie.to_csv(mape / "tirs.csv", index=False)

print("Datu tīrīšana")
print(f"sākumā: {sakuma} beigas: {len(tirie)}")
print(f"bez sugas: {bez_sugas} bez merijumiem: {bez_merijumiem}")
print(f"nederigi merijumi: {slikti} dublikati: {dublikatu_skaits}")
print(f"kopa izmestas: {sakuma - len(tirie)}")
print(f"bez dzimuma bija {nav_dzimuma} rindas tas nedzesu jo dzimumu neizmantoju")
print("saglabats tirs.csv")
