# Uzdevums: Izveidojat biļešu kalkulatoru
# Bērniem zem 12 gadiem cena ir €5
# Skolēniem (12-17 gadi) cena ir €8
# Pieaugušajiem (18-65) cena ir €15
# Senioriem (65+) cena ir €8
# Lietotājs ievada vecumu, programmai jāizvada biļetes cena
# vecums = int(input("Vecums"))
# cena = 0
# if vecums < 12:
#     cena = 5
# elif vecums >= 12 and vecums <= 17:
#     cena = 8
# elif vecums >= 18 and vecums <= 65:
#     cena = 15
# else:
#     cena = 8
# print(f"Cilvēkam cena ir €{cena}!")

# Uzdevums: Kalkulators
# Lietotājam ir jāievada divi skaitļi un darbības zīme
# (darb. zīmes - saskaitīšana, atņemšana, dalīšana vai reizināšana)
# Programmai ir jāizvada darbības rezultāts
# skaitlis1 = float(input("Pirmais skaitlis: ")) # float - daļskaitlis
# skaitlis2 = float(input("Otrais skaitlis: ")) # float - daļskaitlis
# darbība = input("Darbība: ")

# rezultāts = 0
# if darbība == "+":
#     rezultāts = skaitlis1 + skaitlis2
# elif darbība == "-":
#     rezultāts = skaitlis1 - skaitlis2
# elif darbība == "*":
#     rezultāts = skaitlis1 * skaitlis2
# elif darbība == "/":
#     rezultāts = skaitlis1 / skaitlis2
# else:
#     print("Nezināma darbība")
# print(f"Pārbaude - rezultāts ir {rezultāts}")
# Match
# rezultāts = 0
# match darbība:
#     case "+":
#         rezultāts = skaitlis1 + skaitlis2
#     case "-":
#         rezultāts = skaitlis1 - skaitlis2
#     case "*":
#         rezultāts = skaitlis1 * skaitlis2
#     case "/":
#         rezultāts = skaitlis1 / skaitlis2
#     case _:
#         print("Nezināma darbība")

# Cikli
# for - cikls, kuram zinam cik daudz reizes viņš izpildīsies
# while - cikls kuram jūs potenciāli nezinat izpildes reižu daudzumu

# for cikls
saraksts = [ 123, 234, 4123, 35342 ]
# Cikls - gan definīcija (for, while) gan izpildāmais kods
for vērtība in saraksts:
    # iterācija - viss kas tiek palaists ciklā katru reizi, kad viņš palaižās
    # piem. šajā ciklā, katrā iterācijā tiek palaista viena print komanda
    print(vērtība)
# cikls diapazonam (piem. no 0 līdz 9)
for skaitlis in range(0, 10, 2): # parametri - sākums, beigas, solis
    print(skaitlis)

# Uzdevums: Dots saraksts
saraksts = [ 123, 234, 4123, 35342 ]
# Lietotājs ievada skaitli, jums ir jāizvada šī skaitļa INDEKSS sarakstā (ja tas tur ir)
# Jeb vārdus "Nav sarakstā", ja ievadītais skaitlis sarakstā nav.
# Piemēram, ievadei '234' izvade būs 'Skaitļa indekss ir 1'. for ... in range(...)
skaitlis = int(input("Ievadāt skaitli: "))
atrasts = False
for idx in range(len(saraksts)):
    if saraksts[idx] == skaitlis:
        print(f"Skaitlis atrodās indeksā {idx}")
        atrasts = True
if not atrasts:
    print("Nav sarakstā")
# Ar while ciklu - manuāli jāizveido un jāseko līdzi idx pārbaudei
atrasts = False
idx = 0 
while idx < len(saraksts):
    if saraksts[idx] == skaitlis:
        print(f"Skaitlis atrodās indeksā {idx}")
        atrasts = True
    idx += 1 # pieskaita idx +1
if not atrasts:
    print("Nav sarakstā")

# Cikla kontroles atslēgvārdi
# break - pārtrauc cikla darbību 
# continue - pārtrauc iterāciju (turpinot nākošo)
a = 0
while a < 15:
    a += 1
    # Abi if ir pirms print - tiks veikta pārbaude pirms izvades
    if a == 5: # ja a ir 5, mēs beidzam iterāciju - 5 netiks izvadīts
        continue
    if a == 10: # ja ar ir 10, mēs beidzam ciklu - 10,11,12,13,14,15 netiks izvadīts, jo cikls jau beidzās
        break
    print(a)
print("Cikls beidzās")

# Uzdevums: Uzrakstat ciklus, kas ļauj ievadīt sarakstā 3 jebkādas vērtības.
# Realizējat 2 variantus - gan ar while, gan ar for ciklu
# for
saraksts = []
for iii in range(3):
    saraksts.append(input("Vērtība: "))
# while - pārveido for ciklu pa tiešo while ciklā
saraksts = []
skait = 0
while skait < 3:
    saraksts.append(input("Vērtība: "))
    skait += 1
# while otrā versija - izmanto faktu, ka saraksts palielinās katrā iterācijā (gudrāk)
saraksts = []
while len(saraksts) < 3:
    saraksts.append(input("Vērtība: "))
