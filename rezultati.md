# Rezultāti

## 1. Dati

Paņēmu Palmer Penguins datu kopu, tur ir 344 pingvīni no 3 sugām (Adelie, Chinstrap un Gentoo), pavisam 8 kolonnas, dati ir no Palmeras arhipelāga Antarktīdā, 2007.–2009. gads, gribeju pārbaudīt vai pēc četriem ķermeņa mērījumiem var uzminēt sugu.

## 2. Datu tīrīšana

Sākumā bija 344 rindas. Divām rindām trūka visu četru mērījumu tās izņemu, Vēl 11 rindās nebija dzimuma , bet šī kolonna man nav vajadzīga tāpēc šī iemesla dēļ neko nedzēsu (2 no tām jau bija bez mērījumiem). Pārbaudīju arī vai nav nulles, negatīvi mērījumi, trūkstošas sugas vai vienādi ieraksti, tādu papildus nebija

Beigās palika 342 rindas, izmetu tikai 2. Failu `penguins.csv` nemainīju, tajā atstāju sugu, 4 mērījumus un sākotnējās rindas numuru
