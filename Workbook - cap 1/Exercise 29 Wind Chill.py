
temperatura = float(input("Temperatura dell'aria: "))
velocità = float(input("Velocità del vento (chilometri all'orari): "))

WC_OFFSET = 13.12
WC_FACTOR1 = 0.6215
WC_FACTOR2 = -11.37
WC_FACTOR3 = 0.3965
WC_EXPONENT = 0.16

wci = WC_OFFSET + WC_FACTOR1 * temperatura + WC_FACTOR2 * velocità ** WC_EXPONENT + WC_FACTOR3 * temperatura * velocità ** WC_EXPONENT

print("L'indice di vento freddo è", round(wci))
