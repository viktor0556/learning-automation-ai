# TODO: Írj egy programot, ami:

# Bekér egy egész számot N.

# Kiírja 1-től N-ig az összes számot úgy, hogy:
# ha osztható 3-mal: “Fizz”
# ha osztható 5-tel: “Buzz”
# ha mindkettővel: “FizzBuzz”
# különben a számot.

# Korlát
# A kiírás egy soronként történjen.
# Használj függvényt: label(x) (vagy hasonló),
# ami visszaadja a kiírandó értéket.

# Ellenőrzés
# N = 1, 15, 16 esetek.

# Fogalmak: 
- return: átadja egy másik függvénynek kapott számokat.

# Minták (Leírás emberi nyelven):
Csináltam két függvényt, az első ciklus függvényben a már kiszámolt megoldásokat írtam ki a terminálba, a label-ben pedig csináltam egy szabályt ami eldönteni mi melyik kategóriába tartozik bele és azt adtam tovább a ciklus függvénynek.

# Hibák (Mi volt a hibaüzenet? Mi volt a tippem, miért? Mit próbáltam?):
- Csak a return és a szám átadás volt a gondom. Nem tudtam miért áll meg a függvény for range-ben mikor returnot adok hozzá, rájöttem hogy nem szabad beletenni a return-t hanem másik függvényben kell használnom és ott kell átadnom a for ciklusnak így minden számot ellenőriz nem csak egyet. 

# Kimenet (Mi készült el):
- Beírok egy számot, egy számítás alapján pedig eldönteni hogy az 1-N-ig tartó számok melyik kategóriába esnek bele.