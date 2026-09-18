print("Izvade")
#ievade = input()
#print(ievade)

# Datu tipi
# teksts - string
# veseli skaitļi - integer
# daļskaitļi - float/double
# loģiskie predikāti - boolean (True/False - Patiess/Nepatiess)
# saraksts - list
print(10+10+1.0)

#mainīgais = str(10)+"10" # Pārveido skaitli 10 par tekstu "10" == 1010
mainīgais = 10+int("10") # pārveido tekstu "10" par skaitli 10 == 20
mainīgais = 10*"asdfg" # == asdfgasdfgasdfgasdfgasdfgasdfgasdfgasdfgasdfgasdfg
print(mainīgais)

# Ja veicat ievadi (input()) - un ja ir prasīts skaitlis - OBLIGĀTI PADOMĀJAT VAI VAJAG PĀRVEIDOT PAR SKAITLI
# Ar int() (veseli skaitļi) vai float() (daļskaitļi) funkcijām!

# Uzdevums: Prasat no lietotāja viņa vecumu, un izvadat sekojošu tekstu - 
# "Jūs esat x gadus vecs!"
#x = int(input("Vecums: "))
#print("Jūs esat " + str(x) + " gadus vecs!")
#formatēts = f"Jūs esat {x} gadus vecs { 2 + 2 + x }"
#print(formatēts)

# Loģiskie predikāti - parasti vienādības pārbaudes rezultāts
rezultāts = 10 == 11
print(rezultāts)
rezultāts = True

# saraksti - list
saraksts = [ 10, 20, 20, 30, 40, "asdd", True, [ 123, 123, 321 ], 5 * 5 ]
sensora_dati = [ 0.5, 1.0, 0.7, 0.8 ]
saraksti = [ [123, 234, 345], [ 456, 456, 455 ] ]

print(saraksts)
saraksts.insert(0, "Saraksta sākumā") # pievieno saraksta sākumā (0 indeksācija)
saraksts.insert(-1, "Saraksta priekšpēdējais elements") # izņēmuma situācija - -1 citās situācijās ir pēdējais indekss
saraksts.append("Saraksta pēdējais elements!") # pievieno saraksta beigās
print(saraksts)
saraksts.remove(20) # izņem vērtību 20 no saraksta (bet izņem tika VIENU šādu vērtību)
saraksts.pop(0) # izņem pirmo elementu
saraksts.pop(-1) # izņem pēdējo elementu
saraksts.pop(-2) # izņem priekšpēdējo elementu
print(saraksts)
saraksta_garums = len(saraksts)
print(saraksta_garums)
print(saraksts[1:4]) # iegūst elementus ar indeksiem no 1 līdz 3 - neiekļauj ceturto
print(saraksts[1:-1]) # iegūst visus elementus izņemot pirmo un pēdējo

cits_saraksta_tips = ( 10,20,30 ) # Tuple - Kortežs - Neizmaināms saraksts
# Piemērs - peles koordinātes - (x,y) - nevar pievienot jaunu koordināti - pele kustās tikai 2D telpā

teksts = "Kaut kāds teksts"
print(len(teksts))
print(teksts[0:4])