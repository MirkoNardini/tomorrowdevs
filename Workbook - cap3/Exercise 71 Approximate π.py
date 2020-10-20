pi=3.0
op=1

for i in range(2,2*15+1,2):
    pi=pi+4/(i*(i+1)*(i+2))*op
    op*=-1

print("15 approssimazioni di π è:",pi)    
