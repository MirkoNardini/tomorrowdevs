frequenza = float(input("Inserire una frequenza di una certa radiazione: "))

if frequenza < 3e9:
    nome = "Radio Wavs"
elif frequenza >= 3e9 and frequenza < 3e12:
    nome = "Microwaves"
elif frequenza >= 3e12 and frequenza < 4.3e14:
    nome = "Infrared Light"
elif frequenza >= 4.3e14 and frequenza < 7.5e14:
    nome = "Visible Light"
elif frequenza >= 7.5e14 and frequenza < 3e17:
    nome = "Ultraviolet Light"
elif frequenza >= 3e17 and frequenza < 3e19:
    nome = "X-Rays"
elif frequenza >= 3e19:
    nome = "Gamma Rays"
