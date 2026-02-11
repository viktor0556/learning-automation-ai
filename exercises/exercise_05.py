# Python tutorial: “Reading and Writing Files” (I/O rész).

# Feladat 3.1 (exercises/day03_task01/)
# Készíts egy input.txt fájlt 20 sorral (kézzel).
# A program:

# Beolvassa a fájlt.

# Kiszűri azokat a sorokat, amelyek:

# üresek VAGY

# csak whitespace VAGY

# # jellel kezdődnek (komment).

# A maradék sorokat megtisztítja (pl. eleje-vége whitespace le).

# Kiírja egy output.txt fájlba.

# Ellenőrzés

# Nézd meg kézzel, hogy tényleg azt szűrte-e ki.

# Írd le a notes-ba: hány sor ment be, hány jött ki.

# Jegyzet: “automatizálás napló”

# Mit automatizáltál ezzel? (1 mondat)

# Milyen input változtatás törné el a programot? (1 mondat)

inputFile = open("./exercise_05.txt")
outputFile = open("./output.txt", "w")
notes = open("./notes.txt", "w")
linesBefore = 0
linesAfter = 0
for i in inputFile:
  linesBefore += 1
  clean = i.strip()   
  if clean == "" or clean.startswith("#"):
    continue
  else:
    linesAfter += 1
    outputFile.write(clean + "\n")

notes.write("Tisztítás Előtt: " + str(linesBefore))
notes.write("\nTisztítás Után: " + str(linesAfter))
print(linesBefore)
print(linesAfter)