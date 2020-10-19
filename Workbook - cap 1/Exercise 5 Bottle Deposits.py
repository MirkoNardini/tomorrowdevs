deposito_piccolo = 0.10
deposito_grande  = 0.25

piccolo = int(input("quanti contenitori da un litro? "))
grande = int(input("quanti contenitori di più di un litro? "))

rimborso = piccolo * deposito_piccolo + grande * deposito_grande

print("il tuo romborso sarà $%.2f." % rimborso)
