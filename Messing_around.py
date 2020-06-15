#   48
#   (48/2) + 1 = 5 ^ 2
#   48 + 1 = 7 ^ 2
#   next smallest number with same conditions?

# počáteční číslo
n = 1

# modul s komplexnějšími matematickými funkcemi
import math

# opakuje to co je sepsáno uvnitř 
while True:
    
    #mocnina čísla
    other_n = n * n - 1

    #přidá 2 k n
    n += 2
    
    # zkontroluje zda je toto možná odpověď
    if int(math.sqrt(((other_n)/2)+1)) == float(math.sqrt(((other_n)/2)+1)):
        
        # pokud ano, tak napíše číslo do konzole
        print(other_n)