guia = input()
barrera_1 = input()
barrera_2 = input()
barrera_3 = input()
contador_true = 0 
contador_false = 0
len_guia = len(guia)

for letra in guia:
    if letra in barrera_1:
        contador_true += 1 
    else:
        contador_false += 1
if contador_true == len_guia:
    print(True)
else:
    print(False)

contador_true = 0
contador_false = 0

for letra in guia:
    if letra in barrera_2:
        contador_true += 1 
    else:
        contador_false += 1
if contador_true == len_guia:
    print(True)
else:
    print(False)

contador_true = 0
contador_false = 0

for letra in guia:
    if letra in barrera_3:
        contador_true += 1 
    else:
        contador_false += 1
if contador_true == len_guia:
    print(True)
else:
    print(False)
