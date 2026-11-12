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

print("Pingvinu sugu modelis")
print(f"apmācībai: {len(x_tr)} testam: {len(x_te)}")
print(f"modelis: {precizitate:.2%} ({sum(prognozes == y_te)}/{len(y_te)})")
