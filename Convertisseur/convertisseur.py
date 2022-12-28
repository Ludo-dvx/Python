from math import pi

#-----------Formules des convertion------------

# --- Convertion des degrés en radians ---
def deg_en_rad(deg):
    return deg * pi / 180

# --- Convertion des radians en degrés ---
def rad_en_deg(rad):
    return rad * 180 / pi

# --- Convertion des joules en whatt-heures ---
def joule_en_watth(joule):
    return joule / 3600

# --- Convertion des watt-heures en joules ---
def watth_en_joule(watth):
    return watth * 3600

# --- Convertion des litres en metres cubes ---
def litre_en_m3(litre):
    return litre / 1000

# --- Convertion des metres cubes en litres ---
def m3_en_litres(m3):
    return m3 * 1000
    
# --- Option de convertion ---

def menu():
    # Affiche le menu et renvoie le choix de l'utilisateur
    print("\nOptions disponibles : ")
    print("1 : Degrés en radians")
    print("2 : Radians en degrés")
    print("3 : Joules en watt-heures")
    print("4 : Watt-heures en joules")
    print("5 : Litres en metre cube")
    print("6 : Metres cubes en litres")
    print("q : Quitter\n")

    return input("Choix de convertion : ")

def demande_continuer():
    # On demande si l'utilisateur veut quitter avant de réafficher le menu
    reponse = input("Effectuer une autre conversion ? (O/N) :\n ")
    if reponse == "N" or reponse == "n":
        return False
    elif reponse == "O" or reponse == "o":
        return True
continuer = True

while continuer:
    # On affiche le menu et on récupère le choix de l'utilisateur
    choix = menu()

    if choix == "1":
        # On récupère et converti l'angle donné par l'utilisateur
        deg = float(input("Mesure en degrés : "))
        # On affiche le résultat en convertissant en chaine de caractères
        print("Mesure en radians : " + str(deg_en_rad(deg)))
        # On demande si l'on souhaite faire d'autres convertions
        continuer = demande_continuer()
   
    elif choix == "2":
        rad = float(input("Mesure en radians : "))
        print("Mesure en degrés : " + str(rad_en_deg(rad)))
        continuer = demande_continuer()
    
    elif choix == "3":
        joule = float(input("Mesure en joules : "))
        print("Mesure en watt-heures : " + str(joule_en_watth(joule)))
        continuer = demande_continuer()

    elif choix == "4":
        watth = float(input("Mesure en watt heures : "))
        print("Mesure en joules : " + str(watth_en_joule(watth)))
        continuer = demande_continuer()
    
    elif choix == "5":
        litre = float(input("Mesure en litres : "))
        print("Mesure en metres cubes : " + str(litre_en_m3(litre)))
        continuer = demande_continuer()
    
    elif choix == "6":
        m3 = float(input("Mesure en metres cubes : "))
        print("Mesure en litres : " + str(m3_en_litres(m3)))
        continuer = demande_continuer()
   
    elif choix == "q":
        # On veut quitter
        continuer = False

    else:
        print("Option inconnue")

