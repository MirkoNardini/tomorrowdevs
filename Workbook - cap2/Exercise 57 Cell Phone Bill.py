min = float(input("Quanti minuti d'aria hai usato questo mese?:"))
mex = int(input("Quanti messaggi avete usato questo mese?:"))
base_tar = 15.00
emer_tar = 0.44
min_tar = 0
mex_tar = 0

if min > 50:
    min_tar = (min - 50)*0.25
if mex > 50:
    mex_tar = (mex - 50)*0.15

tot = (base_tar+emer_tar+min_tar+mex_tar)+((base_tar+emer_tar+min_tar+mex_tar)*5/100)
print(tot)

