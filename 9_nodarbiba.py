# Uzdevums - Izveidojat funkciju, kas pārbauda vai dotā parole atbilst nosacījumiem
# Parolei jābūt vismaz 5 simboliem un jāsatur skaitli un vienu 
# no sekojošajiem simboliem - !@#$%^&*(). 
# Funkcija atgriež True ja atbilst nosacījumiem, False ja neatbilst.
# Pārbaudat vismaz 3 paroles.
def pārbaudīt_paroli(parole):
    if len(parole) < 6:
        return False
    simboli = "!@#$%^&*()"
    for simbols in parole:
        if simbols in simboli:
            return True
    return False
print(pārbaudīt_paroli("Lavizes2A!"))

# Uzdevums: Novelkat, saglabājat doto failu:
# https://s.ayy.lv/ff
# Sadalat doto kodu funkcijās

# Uzdevums (procentu darbs):
# Izveidojat divus mainīgos - svars un distance
# Uzrakstāt  divas funkcijas kas pielieto šos mainīgos - 
#            aprēķināt piegādi un izvadīt piegādes tipu
# Aprēķināt piegādi izvada piegādes cenu, kas tiek aprēķināti šādi - 
# Svars līdz 2kg - EUR3
# Svars no 2 līdz 5kg - EUR5
# Svars > 5kg - EUR8
# Tad pievieno EUR0.10 par katru kilometru
# Piegādes tips izvada 
# 'Vietējā' ja distance < 10km
# 'Reģionālā' ja distance ir 10-50km
# 'Gara distance' ja distance >50km
# Izsaucat šīs funkcijas ar testa datiem.