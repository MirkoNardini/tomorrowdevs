while True:  
  lettere1 = ['a', 'c', 'e', 'g']
  lettere2 = ['b', 'd', 'f', 'h']
  numeri1 = [1, 3, 5, 7]
  numeri2 = [2, 4, 6, 8]
  lettere = input("Inserisci la lettera:\n")
  while True:  
    try:
      numberi = int(input("Inserire il numero:\n"))
      break
    except ValueError:
      print("Il numero deve essere un numero intero.\n")
  if lettere.lower() in lettere1 and numberi in numeri1:
    print("The square is black.\n")
  elif lettere.lower() in lettere2 and numberi in numeri1:
    print("Il quadrato è nero.\n")
  elif lettere.lower() in lettere2 and numberi in numeri2:
    print("Il quadrato è bianco.\n")
  elif lettere.lower() in lettere1 and numberi in numeri2:
    print("Il quadrato è nero.\n")
  else:
    print("La lettera deve essere una lettera.\n")

