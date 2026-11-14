# Pirmais modelis no nulles

Šeit pamēģināju uztaisīt modeli, kas pēc pingvīna izmēriem pasaka tā sugu. Izmantoju Palmer Penguins datus ar 3 sugām. Sākumā iztīru CSV failu un tad apmācu vienkāršu lēmumu koku, beigās salidzinu ar variantu kur vienmēr min biežāko sugu.

## Kā palaist

Vajag Python 3.10+ un instalētas bibliotēkas, projekta folderi palaist šīs komandas pēc kārtas:

```bash
python -m pip install -r requirements.txt
python 01_tirisana.py
python 02_modelis.py
```

Ja Windows `python` nestrādā, var pamēģināt `py`.

`01_tirisana.py` lasa `dati/penguins.csv` un izveido `tirs.csv`, bet `02_modelis.py` izmanto jau to tīro failu. Oriģinālos datus nepārrakstu.

Modelim ir tikai 4 mērījumi: knābja garums un dziļums, pleznas garums un svars. Dzimumu, salu un gadu neņēmu, jo gribēju redzēt vai pietiek ar šiem izmēriem. `avota_rinda` ir tikai lai vēlāk varētu atrast kļūdu sākotnējā CSV.

Rezultātu un kļūdas piemēru aprakstīju [rezultati.md], datu saite un licence ir [dati/AVOTS.txt], izmantoju `pandas` un `scikit-learn`
