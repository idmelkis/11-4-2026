# f(a) = a*a
# f(1) = 1 * 1
# f(2) = 2 * 2

def nosaukums(parametrs1, parametrs2):
    print("Funkcijas kods")
    print("Funkcijas kods 2")
    return parametrs1 * parametrs2
rezultāts = nosaukums(1, 2)

# Pielietojums
# 1. Lai padarītu programmu lasāmāku
# Piemērs - Uzdevums no KD - Sarakstā ievada 5 vērtības, izvada šo skaitļu reizinājumu kvadrātā
def ievadīt_skaitļus(skaitļu_daudzums):
    saraksts = []
    for iii in range(skaitļu_daudzums):
        saraksts.append(input(f"Skaitlis nr. {iii}"))
    return saraksts
def izvadīt_skaitļus(saraksts):
    for skaitlis in saraksts:
        print(skaitlis * skaitlis)
saraksts = ievadīt_skaitļus(5)
izvadīt_skaitļus(saraksts)
# 2. Lai samazinātu koda duplikāciju (piem. ja kods atkārtojas 3+ reizes)
# 3. Abstraktēšana - Ņemam praktiskus procesus, piem. naudas izņemšana no bankas konta, un apraksta funkcijas formā.

# Terminoloģija
# Procedūra - Funkcija, kas neko neatgriež - funckijai nav return

# Uzrakstat funkciju (procedūru), kas pārbauda vai dotais skaitlis (parametrs) ir lielāks par 0,
# mazāks, vai vienāds ar 0 - attiecīgi izvada "Lielāks", "Mazāks" vai "Vienāds ar 0"
def lielaks_mazaks(skaitlis):
    if skaitlis > 0:
        print("Lielāks")
    elif skaitlis < 0:
        print("Mazāks")
    else:
        print("Vienāds ar 0")
lielaks_mazaks(-1)
lielaks_mazaks(0)
lielaks_mazaks(1)
lielaks_mazaks(9999)

# Uzdevums: Uzrakstat funckiju kas pieņem skaitli kā parametru un
# atgriež False ja skaitlis ir nepāra, True ja tas ir pāra. (ja skaitlis % 2 == 0, tad ir pāra)
# Pārbaudat vismaz 3 vērtības.
def pāra_nepāra(skaitlis):
    if skaitlis % 2 == 0:
        return True
    else:
        return False
    #return skaitlis % 2 == 0
print(pāra_nepāra(2))
print(pāra_nepāra(8))
print(pāra_nepāra(15))

# Parametriem var būt standarta vērtības - izsaucot vairs nav katru reizi jānorāda šī vērtība
def funkcija_piemērs(parametrs="vērtība"):
    print(parametrs)
funkcija_piemērs()

# Šo var izmantot lai uzliktu neobligātos parametrus. Ja gribam šos parametrus izmantot
# Mēs izsaucot funkciju varam norādīt parametra nosaukumu.
def funkcija_piemērs(parametrs1 = "viena vērtība", parametrs2 = "otra vērtība"):
    print(parametrs1, parametrs2)
funkcija_piemērs(parametrs2="Cita vērtība")

# Praktisks piemērs - funkcijai print ir parametrs kas norāda kāds simbols būs pēc teksta -
# parasti tas ir jaunas rindas simbols \n. Nomainot to, varam izmantot vairākus print lai izvadītu
# tekstu vienā rindā.
print("Gribu lai", end=" ") #\n
print("Šis ir vienā rindā")

# Vairāki parametri (nezināms skaits - praktiski neierobežots) ar vienu definīciju
def piemērs(*parametrs):
    print(parametrs) # parametrs ir Tuple (saraksts)
piemērs("Pirmais", "Otrais", "Trešais")
# Praktiski to dara arī print -
print("Viens", "Divi", "Trīs", "Četri")

# Uzdevums: Uzrakstīt funkciju, kas pieņem nezināmu daudzumu skaitļus
# un izvada lielāko skaitli. Neizmantot funkciju max()!
def lielākais(*skaitļi):
    rezultāts = skaitļi[0]
    for skaitlis in skaitļi:
        if skaitlis > rezultāts:
            rezultāts = skaitlis
    return rezultāts
print(lielākais(10,20,-1,99,9))
