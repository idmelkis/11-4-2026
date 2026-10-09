# Uzdevums: Uzrakstāt ciklu, kas izvada skaitļus no 0 līdz 10
# Izlaižot skaitļus 4 un 6. Realizēt gan for,
#  gan while ciklu variantus.
# for
for iii in range(0, 11):
    if iii == 4 or iii == 6:
        continue
    print(iii)
# while
iii = -1
while iii < 11:
    iii += 1
    if iii == 4 or iii == 6:
        continue
    print(iii)

# Uzdevums: Ir dots saraksts
saraksts = [ 123, 432, 6324, 7544 ]
# Neizmantojot funkciju sum(), uzrakstāt ciklu, kas saskaita
# visas vērtības šajā sarakstā un izvada rezultātu
rezultāts = 0
for vērtība in saraksts:
    rezultāts += vērtība
print(rezultāts)

# Uzdevums: Aprēķini faktoriāli lietotāja ievadītam skaitlim
# Faktorālis - skaitlis kas veidojas reizinot visus skaitļus
# no 1 līdz n (ievadītais skaitlis). Piem, 3! == 1 * 2 * 3 = 6
# N.B. - 0! == 1
ievade = int(input("Ievade: "))
if ievade == 0:
    print("1")
else:
    rezultāts = 1
    for iii in range(2, ievade + 1):
        rezultāts *= iii
    print(rezultāts)

# Uzdevums: Dots mainīgais ar paroli:
parole = "RAVGParole!"
# uzrakstāt ciklu, kas prasa lietotājam paroli
# līdz tā tiek ievadīta pareizi. Ja parole ir nepareiza
# izvadāt "Nepareiza parole."

# 1. var
# ievade = input("Parole: ")
# while ievade != parole:
#     print("Nepareiza parole")
#     ievade = input("Parole: ")
# print("Pareiza parole")    
# 2. var
while True:
    ievade = input("Parole: ")
    if ievade == parole:
        break
    print("Nepareiza parole")
print("Pareiza parole")

# procentu darbiņš:
# Bankas konta simulators - lietotājam ir dotas sekojošas funkcijas
# Iemaksāt naudu, izņemt naudu, parādīt atlikumu un iziet.
# Nevar izņemt vairāk naudu kā ir kontā.
# Programma turpina darbu, līdz lietotājs izvēlas funkciju "Iziet".