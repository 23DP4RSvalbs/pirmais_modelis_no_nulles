# Rezultāti

## 1. Dati

Paņēmu Palmer Penguins datu kopu, tur ir 344 pingvīni no 3 sugām (Adelie, Chinstrap un Gentoo), pavisam 8 kolonnas, dati ir no Palmeras arhipelāga Antarktīdā, 2007.–2009. gads, gribeju pārbaudīt vai pēc četriem ķermeņa mērījumiem var uzminēt sugu.

## 2. Datu tīrīšana

Sākumā bija 344 rindas. Divām rindām trūka visu četru mērījumu tās izņemu, Vēl 11 rindās nebija dzimuma , bet šī kolonna man nav vajadzīga tāpēc šī iemesla dēļ neko nedzēsu (2 no tām jau bija bez mērījumiem). Pārbaudīju arī vai nav nulles, negatīvi mērījumi, trūkstošas sugas vai vienādi ieraksti, tādu papildus nebija

Beigās palika 342 rindas, izmetu tikai 2. Failu `penguins.csv` nemainīju, tajā atstāju sugu, 4 mērījumus un sākotnējās rindas numuru

## 3. Modelis un precizitāte

Izvēlējos `DecisionTreeClassifier`, jo lēmumu koku ir diezgan viegli saprast, uzliku `max_depth=3` un `min_samples_leaf=3` lai neveidotos pārāk sarežģīts koks, sadalīju datus 75% treniņam un 25% testam, ar `random_state=42` un `stratify=y`, sanāca 256 treniņa un 86 testa rindas, testa dati netika izmantoti apmācībai.

**Modelis pareizi noteica 85 no 86 jeb 98,84%.** Salīdzinājumam vienmēr minot biežāko treniņa sugu Adelie sanāca 38 no 86 jeb 44,19%, tātad modelis bija labāks par 54,65 procenta punktiem un tiešām izmantoja sakarības datos, nevis tikai minēja biežāko atbildi. Manuprāt tas nenozīmē, ka modelis vienmēr būs tik precīzs, Testā ir tikai 86 pingvīni un visi dati ir no viena reģiona, tāpēc citos datos rezultāts varētu atšķirties.

## 4. Svarīgākie mērījumi

Lēmumu kokam visvairāk palīdzēja pleznas garums (`flipper_length_mm`) 55,5% un knābja garums (`bill_length_mm`) 34,6%. Tam ir jēga jo dažādām sugām izmēri atšķiras, tie ir svarīguma rādītāji tikai šim kokam, nevis visiem pingvīniem kopumā

## 5. Viena nepareiza prognoze

Kļūda bija sākotnējā CSV **300. rindā**, patiesībā tas ir **Chinstrap**, bet modelis atbildēja **Adelie**. šis pingvīns bija no Dream salas, knābis 43,2 mm garš un 16,6 mm dziļš, plezna 187 mm un svars 2900 g. Salu es modelī neizmantoju.

Man šķiet koks kļūdījās, jo šī pingvīna izmēri ir līdzīgi Adelie. Viena no robežām kokā ir 43,35 mm knābja garumam, bet šim ir 43,2 mm, tikai nedaudz mazāk, tā kā koks izmanto stingras robežas, ne visi dzīvnieki sadalās perfekti.

## 6. Kur šo neizmantotu

Es šo modeli neizmantotu automātiskai sugu uzskaitei īstā dabas pētījumā bez biologa pārbaudes, tas pazīst tikai trīs sugas un tikai konkrētu datu kopu, ja iedotu citu sugu tas tāpat mēģinātu izvēlēties vienu no šīm trim. šim mācību darbam der, bet kā drošs noteicējs nē.

## Pašvērtējums

Sanāca iztīrīt datus, uztaisīt modeli un salīdzināt ar vienkāršu bāzes variantu, visinteresantāk bija atrast to vienu kļūdu un saprast kāpēc tā radās. Ja turpinātu, gribētu izmēģināt vairākus datu sadalījumus un redzēt vai precizitāte paliek līdzīga.
