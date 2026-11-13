from pathlib import Path
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

mape =  Path(__file__).resolve().parent
merijumi  = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
dati = pd.read_csv(mape / "tirs.csv")

x = dati[merijumi]
y = dati["species"]

# 25% atstaju testam lai parbauditu uz neredzetiem datiem
x_tr, x_te, y_tr, y_te = train_test_split(
    x, y, test_size=0.25, random_state=42, stratify=y
)

modelis = DecisionTreeClassifier(max_depth=3, min_samples_leaf=3, random_state=42)
modelis.fit(x_tr, y_tr)
prognozes = modelis.predict(x_te)
precizitate = accuracy_score(y_te, prognozes)

# salidzinajumam vienmer mineju  biezako sugu no trenina datiem
biezaka = y_tr.value_counts().idxmax()
bazes_prognozes = [biezaka] * len(y_te)
bazes_precizitate = accuracy_score(y_te, bazes_prognozes)

print("Pingvinu sugu modelis")
print(f"apmācībai: {len(x_tr)} testam: {len(x_te)}")
print(f"modelis: {precizitate:.2%} ({sum(prognozes == y_te)}/{len(y_te)})")
print(f"vienmer {biezaka}: {bazes_precizitate:.2%} ({sum(y_te == biezaka)}/{len(y_te)})")

svarigums = sorted(zip(merijumi, modelis.feature_importances_), key=lambda a: a[1], reverse=True)
print("Svarigākie merijumi:")
for kolonna, vertiba in svarigums[:2]:
    print(f"{kolonna}: {vertiba:.1%}")
