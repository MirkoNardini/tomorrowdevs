
posta = {"Newfoundland": "A", "Nova Scotia": "B", "Prince Edward Island": "C", "New Brunswick": "E",
             "Quebec": ["G", "H", "I"], "Ontario": ["K", "L", "M", "N", "P"], "Manitoba": "R", "Saskatchewan": "S",
             "Alberta": "T", "British Columbia": "V", "Nunavut": "X", "or Northwest Territories": "X", "Yukon": "Y"}

codice_posta = input("Inserisci il codice postale: ").upper()
risultato = ""
if codice_posta[1] == 0:
    risultato += "un rurale "
else:
    risultato += "un rubano "
for key, value in posta.items():
    if codice_posta[0] in value:
        risultato += "indirizzo " + key


print("Il codice postale {} è per {} ".format(codice_posta, risultato))
