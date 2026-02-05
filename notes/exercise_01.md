Írj egy programot, ami:
# - Bekér 3 számot a felhasználótol (külön sorban).
# - Kiírja: minimum, maximum, átlag (két tizedesre kerekítve)

# Fogalmak: 
- min(): Legkisebb
- max(): Legnagyobb
- round(_, 2): Mennyi számra kerekítse

# Minták (Leírás emberi nyelven):
- Először memóriába mentettem a 3 külön változót, a 3 beírt változót mentettem egy tömbbe és a tömbből min-el kikerestem a legkisebb számot, max-al kikerestem a legnagyobb számot és egy saját változóval kiszámoltam az átlagot és kerekítettem kettőre.

# Hibák (Mi volt a hibaüzenet? Mi volt a tippem, miért? Mit próbáltam?):
- Annál akadtam el nem tudom hogy lehetne megoldani hogy több szám közül pl 1,2,3 között válasszon. 10 perc elteltével rájöttem hogy tömbbe kell rakni őket.
- Hibák: - Próbáltam hogy hibás írások esetén pl nem szám vagy ha semmit nem írunk be akkor printelje ki hogy helytelen szám, de nem az én kódom futott le hanem a python hibakódja.

# Kimenet (Mi készült el):
- Elkészítettem hogy kiírja a bekért számok legkisebb legnagyobb számát és az átlagát két tizedesjegyig
- Példa megoldás:
Írd be az első számot: 5
Írd be a második számot: 5
Írd be a harmadik számot: 11
Általad megadott számok: 5, 5, 11
Legkisebb szám: 5
Legnagyobb szám: 11
Átlag számolás: 13.666666666666666