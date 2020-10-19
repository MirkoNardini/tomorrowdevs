valutazione = float(input("Inserisci la valutazione: "))

FATTORE_DI_SOLLEVAMENTO = 2400.00
INACCETTABILE = 0
ACCETTABILE = 0.4
MERITORIO = 0.6

if valutazione == INACCETTABILE:
    performance = "inaccettabile"
elif valutazione >= MERITORIO:
    performance = "meritorio"
elif valutazione == ACCETTABILE:
    performance = "accettabile"
else:
    performance = ""

if performance == "":
    print("Non era una valutazione valida.")
else:
    print("In base a tale valutazione, la vostra performance è %s." % \
    performance)
    print("Riceverai un aumento di $%.2f." % \
    (valutazione * FATTORE_DI_SOLLEVAMENTO))
