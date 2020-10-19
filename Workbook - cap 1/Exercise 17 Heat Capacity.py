capacità_di_calore_acqua = 4.186
eletricita_spesa = 8.9
joul_KWH = 2.777e-7

volume = float(input("Quantità d'acqua in millilitri "))
tempo = float(input("Aumento della temperatura: "))

q = volume * tempo * capacità_di_calore_acqua
print("Questo avrà un dispendio di %d Joules di energia" % q)

kwh = q * joul_KWH
cost = kwh * eletricita_spesa

print("Tutta quell'energia costerà %.2f centesimi." % cost)
