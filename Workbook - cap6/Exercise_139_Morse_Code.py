#inserisco un codice morse in un dizionario

morse = {
  "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
  "E": ".", "F": "..-.", "G": "--.", "H": "...",
  "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
  "M": "--", "N": "-.", "O": "---", "P": ".--.",
  "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
  "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
  "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
  "3": "...--", "4": "....-", "5": ".....", "6": "-....",
  "7": "--...", "8": "---..", "9": "----."
}

enter = list(input("Inserisci una frase e il programma la trasformerà in codice Morse: ").upper())
risultato = ""

for i in enter:
    for key, value in morse.items():
        if i in key:
                 risultato += " " + value

print('(',risultato,')')
