# E-klases pastā - parole, lietotājvārds un links uz Bebr[a]s konkursu
# Ielogojoties prasīs vārdu uzvārdu - ievadāt un saglabājat
# Augšā labajā stūrī ir poga Konkursi - tur varēsiet sākt.

# Uzdevums: Pārveidojat kodu - izveidojat funkciju no dotā koda gabala
# Funkcijai jāatgriež rezultāts ar return
# Izsauciet to trīs reizes ar dažādiem skaitļiem un darbības zīmēm
def kalkulators(skaitlis1, skaitlis2, darbība):
    rezultāts = 0
    if darbība == "+":
        rezultāts = skaitlis1 + skaitlis2
    elif darbība == "-":
        rezultāts = skaitlis1 - skaitlis2
    elif darbība == "*":
        rezultāts = skaitlis1 * skaitlis2
    elif darbība == "/":
        rezultāts = skaitlis1 / skaitlis2
    else:
        print("Nezināma darbība")
        return None
    return rezultāts
#rezultāts = funkcija(skaitlis1, skaitlis2, darbzīme)
print(kalkulators(10, 10, "+"))
print(kalkulators(10, 5, "/"))
print(kalkulators(2, 2, "*"))

# Uzdevums - Izveidojat funkciju, kas pārbauda vai dotā parole atbilst nosacījumiem
# Parolei jābūt vismaz 5 simboliem un jāsatur skaitli un vienu 
# no sekojošajiem simboliem - !@#$%^&*(). 
# Funkcija atgriež True ja atbilst nosacījumiem, False ja neatbilst.
# Pārbaudat vismaz 3 paroles.
def pārbaudīt_paroli(parole):
    ...