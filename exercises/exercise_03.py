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

userInput = int(input("Adj meg egy számot: "))

def cycle():
  for n in range(1, userInput + 1):
    print("Ciklusban: ", userInput)
    result = label(n)
    print(result)
    
def label(x):
  n = x
  fizz = n % 3 == 0 
  buzz = n % 5 == 0
  fizzBuzz = n % 3 == 0 and n % 5 == 0
  if fizzBuzz:
    return "FizzBuzz"
  elif fizz:
    return "Fizz"
  elif buzz:
    return "Buzz"
  else:
    return n
    
cycle()