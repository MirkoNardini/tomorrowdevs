
lunghezza_d = int(input("Inserisci una lunghezza d'onda: "))

if lunghezza_d >= 380 and lunghezza_d <450:
    colore = "Viola"
elif lunghezza_d >=450 and lunghezza_d <495:
    colore = "Blu"
elif lunghezza_d >=495 and lunghezza_d <570:
    colore = "Grigio"
elif lunghezza_d >=570 and lunghezza_d <590:
    colore = "Giallo"
elif lunghezza_d >=590 and lunghezza_d <620:
    colore = "Arancione"
elif lunghezza_d >=620 and lunghezza_d <=750:
    colore = "Rosso"
else:
    colore = ""

if colore == "":
    print("Quella lunghezza d'onda è al di fuori dello spettro visibile.")
else:
    print("Il colore di quella lunghezza d'onda è: %s" %color)
