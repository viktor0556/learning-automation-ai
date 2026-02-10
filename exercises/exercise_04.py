# TODO:
# Írj egy programot, ami:

# Bekér addig számokat, amíg a felhasználó “stop”-ot nem ír.

# Közben gyűjti a számokat, és a végén kiírja:

# darabszám
# összeg
# átlag
# hány pozitív/negatív/0 volt.

# Korlát

# Kezeld le, ha valaki nem számot ír (ne omoljon össze, kérje be újra).

def reqNumbs():
  szám = 0
  allPos = 0
  allNeg = 0
  allNull = 0
  lista = []
  while True:
    x = input("Írj be egy számot, stop-al eredményt kapsz: ")
    try:
      shapedInput = int(x)
      lista.append(shapedInput)
      print("OK")
      szám += shapedInput
      print("Összeg: ", szám)
      
      positive = shapedInput > 0
      negative = shapedInput < 0

      if positive:
        allPos += 1
      elif negative:
        allNeg += 1
      else:
        allNull += 1
    except ValueError:
      print("NEM SZÁM")
      if x == "stop":  
        print(f"""Összeg: {szám}\nÖsszes pozitív: {allPos}
                \nÖsszes negatív: {allNeg}\nÖsszes nulla: {allNull}
                \nÖsszes szám: {lista}""")
        break
    
def gyak1(x):
  while x != "stop":
    x = input("Szöveg: ")
    print("Most ez az input: ", x)

def gyak2():
  userInput = input("Írj be egy számot, stop-al eredményt kapsz: ")
  try:
    if int(userInput):
      print("OK")
  except:
    print("NEM SZÁM")

def gyak3():
  userInput = int(input("Írj be egy számot, stop-al eredményt kapsz: "))
  lista = [1, 2, 3, 4]
  szám = 0  
  for i in lista:
    szám += i
  szám += userInput
  print(szám)

def gyak4(x):
  positive = x > 0
  negative = x < 0
  
  if positive:
    print("Pos")
  elif negative:
    print("Neg")
  else:
    print("Null")