# TODO: Írj egy programot, ami:
# Bekér egy szöveget.
# Kiírja: hány karakter, hány szó (szó = whitespace-szel elválasztott token).
# Kiírja a leghosszabb szót (ha több azonos, elég az első).
 
def reqSentence():
  userInput = str(input("Adj meg egy szót vagy mondatot: "))
  wordLength = len(userInput.strip())
  shapedInput = userInput.strip()
  
  hunLetters = ["A","Á","B","C","Cs","D","Dz","Dzs","E","É","F",
                "a","á","b","c","cs","d","dz","dzs","e","é","f",
                "G","Gy","H","I","Í","J","K","L","Ly","M","N",
                "g","gy","h","i","í","j","k","l","ly","m","n",
                "Ny","O","Ó","Ö","Ő","P","Q","R","S","Sz","T",
                "ny","o","ó","ö","ő","p","q","r","s","sz","t",
                "Ty","U","Ú","Ü","Ű","V","W","X","Y","Z","Zs",
                "ty","u","ú","ü","ű","v","w","x","y","z","zs"
                ]
  if wordLength >= 1:
    word = 1
    space = 0
    
    # Karakter és szó számolás
    for i in shapedInput:
      if i == " ":
        space += 1
        print("Hozzáadva egy space: ", space)
        if space == 1 and space < 2:
          word += 1
          print("Hozzáadva word: ", word)
        elif space >= 2 or space == 2:
          wordLength -= 1
          space -= 1
          print(f"Eltávolítva egy space: {space} és karakter: {wordLength}", )

        if i in hunLetters:
          space = 0
          print("Space lenullázva")

    print("Összes szó", word)
    print("Összes karakter: ", wordLength)
  elif wordLength <= 0:
    print("Nincs megadva szó")
    
  # hosszúság számolás 
  # Kiírja a leghosszabb szót (ha több azonos, elég az első).
  splitedWords = shapedInput.split()
  itemsArray = []
  
  for i in splitedWords:
    itemsArray.append(len(i))
    biggestItemsArrayIdx = itemsArray.index(max(itemsArray))
    print(biggestItemsArrayIdx)
    print("Legnagyobb számu szó: ", splitedWords[biggestItemsArrayIdx], itemsArray[biggestItemsArrayIdx])
  
reqSentence()