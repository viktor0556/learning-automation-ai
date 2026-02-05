#TODO: Írj egy programot, ami:
# - Bekér 3 számot a felhasználótol (külön sorban).
# - Kiírja: minimum, maximum, átlag (két tizedesre kerekítve)

def reqNumbs():
  userInput1 = int(input("Írd be az első számot: "))
  userInput2 = int(input("Írd be a második számot: "))
  userInput3 = int(input("Írd be a harmadik számot: "))
  if (userInput1 is None 
      and userInput1 is not int):
    print("Helytelen szám", userInput1)
  elif(userInput2 is None 
      and userInput2 is not int):
    print("Helytelen szám", userInput2) 
  elif(userInput3 is None
      and userInput3 is not int):
    print("Helytelen szám", userInput3)
    
  else:
    numbContainers = [userInput1, userInput2, userInput3]
    
    avgNumbs = userInput1 + userInput2 + userInput3 / 3
    
    print(f"Általad megadott számok: {userInput1}, {userInput2}, {userInput3}")
    print(f"Legkisebb szám: {min(numbContainers)}\nLegnagyobb szám: {max(numbContainers)}\nÁtlag számolás: {round(avgNumbs)}")
    
reqNumbs()