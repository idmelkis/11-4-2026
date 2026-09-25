# Uzdevums: Prasāt lietotājam lai ievada
# tā mīļāko dzīvnieku, ēdienu un valsti.
# Izvadat šo informāciju sekojošā formātā:

# Mīļākie:
# Dzīvnieks: {}
# Ēdiens: {}
# Valsts: {}
# dzivnieks = input("Mīļākais dzīvnieks: ")
# ediens = input("Mīļākais ēdiens: ")
# valsts = input("Mīļākā valsts: ")
# print("Mīļākais dzīvnieks: " + dzivnieks)
# print("Mīļākais dzīvnieks:", dzivnieks)
# print(f"Mīļākais dzīvnieks: {dzivnieks}\nMīļākais ēdiens: {ediens}\nMīļākā valsts: {valsts}")

# Uzdevums: Ir dots sekojošs saraksts:
soma = [ "Zobens", "Vairogs", "Ūdens" ]
# Uzrakstat programmu, kas ļauj lietotājam izņemt vienu no elementiem no somas
# Izvadāt izņemto elementu, un somas saturu pēc izņemšanas
# Piezīme - ir divi varianti - list.pop(idx), un list.remove(val) 
# - var izmantot jebkuru

# remove()
# soma = [ "Zobens", "Vairogs", "Ūdens" ]
# iznemt_elementu = input("Ko vēlaties izņemt? ")
# soma.remove(iznemt_elementu)
# print(f"Izņemtais elements: {iznemt_elementu}")
# print(f"Somas saturs pēc izņemšanas: {soma}")
# pop()
# soma = [ "Zobens", "Vairogs", "Ūdens" ]
# iznemt_kartu = int(input("Kādu elementu pēc kārtas vēlaties izņemt? ")) - 1
# print(f"Tiks izņemts elements {soma[iznemt_kartu]}")
# soma.pop(iznemt_kartu)
# print(f"Somas saturs pēc izņemšanas: {soma}")

# if - loģiskās pārbaudes
# if <pārbaude>:
#     darbība (ar atkāpi no kreisās puses)
if 10==10:
    # TAB poga - virs caps lock ieliek uzreiz atstarpes
    print("Vienmēr izpildās")
    if False:
        print("Vēl 4 atstarpes - otrais if bloks")
    print("Turpinās pirmais bloks")
print("Šeit turpinās kods, kas nav zem if")

skaitlis = 99
if skaitlis == 10:
    print("Pirmā darbība")
elif skaitlis == 11:
    print("Otrā darbība")
elif skaitlis == 12:
    print("Trešā darbība")
else:
    print("Neviena pārbaude neizpildās")

# match (citās valodās switch) - Strādā tikai no Python 3.10+
match skaitlis:
    case 10: # mazliet īsāk = nav jāraksta pārbaude atkārtoti
        print("Pirmā darbība")
    case 11:
        print("Otrā darbība")
    case 12:
        print("Trešā darbība")
    case _:
        print("Neviena cita pārbaude neizpildījās")

# Loģiskās pārbaudes
# Vienādojums - abās pusēs vērtība ir vienāda - == (piem. 10 == 10)
# Vienādojums ar objekta tipa pārbaudi - abās pusēs ir vienāds tips - is (piem. 10 is 10)
# Nevienādība - Abās pusēs vērtība NAV vienāda, != (piem. 11 != 10)
# Lielāks par - kreisā puse ir lielāka par labo pusi (skaitlis), > (piem. 10 > 9)
# Mazāks par - kreisā puse ir mazāka par labo pusi (skaitlis), < (piem. 9 < 10)
# Lielāks vai vienāds ar - kreisā puse ir lielāka vai vienāda ar labo pusi (piem. 10 >= 10)
# Mazāks vai vienāds ar - kreisā puse ir mazāka vai vienāda ar labo pusi (piem. 10 <= 10)
# Negatīvā pārbaude - not - apgriež pārbaudes rezultātu (piem. not 10 == 10 izvada False )
# piemērs
# logged_in = False
# if not logged_in:
#     print("Lietotājs nav autorizējies")

# Darbības:
# +, -, ., * 
# Modulus operators - % - izvada dalīšanas atlikumu
# Piemēram - 10 % 10 - nav atlikums == 0
# 10 % 9 - atlikums ir 1 == 1
# Parasti izmanto lai pārbaudītu vai skaitlis dalās ar citu skaitli (atlikums ir 0)
#print(10 % 10)
#print(10 % 9)

# Uzdevums: Lietotājs ievada skaitli, programmai jānosaka vai ievadītais skaitlis ir pāra skaitlis
# (dalās ar 2 bez atlikuma)
ievade = int(input("Skaitlis: "))
if ievade % 2 == 0:
    print("Ievadīts pāra skaitlis")
else:
    print("Ievadīts nepāra skaitlis")

# Pārbaužu apvienošana
# and - apvieno dažādas pārbaudes - abās pusēs pārbaudēm ir jāizpildās
# or - apvieno pārbaudes, bet jāizpildās tikai vienai no pārbaudēm
skaitlis = 15
if skaitlis > 10 and skaitlis < 20:
    print('skaitlis ir diapazonā starp 10 un 20')
if skaitlis < 20 or skaitlis > 50:
    print('skaitlis ir vai nu mazāks par 20, vai lielāks par 50')

# if (ievade > 10 or ievade < 5) and (ievade < 15 and ievade > 10):
#     pass

# Uzdevums: Izveidojat biļešu kalkulatoru
# Bērniem zem 12 gadiem cena ir €5
# Skolēniem (12-17 gadi) cena ir €8
# Pieaugušajiem (18-65) cena ir €15
# Senioriem (65+) cena ir €8
# Lietotājs ievada vecumu, programmai jāizvada biļetes cena
