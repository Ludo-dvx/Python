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
    
# --- Option de convertion ---

def menu():
    # Affiche le menu et renvoie le choix de l'utilisateur
    print("\nOptions disponibles : ")
    print("1 : Degrés en radians")
    print("2 : Radians en degrés")
    print("3 : Joules en watt-heures")
    print("4 : Watt-heures en joules")
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
        deg = float(input("Mesure en degré : "))
        # On affiche le résultat en convertissant en chaine de caractères
        print("Mesure en radian : " + str(deg_en_rad(deg)))
        # On demande si l'on souhaite faire d'autres convertions
        continuer = demande_continuer()
   
    elif choix == "2":
        rad = float(input("Mesure en radian : "))
        print("Mesure en degré : " + str(rad_en_deg(rad)))
        continuer = demande_continuer()
    
    elif choix == "3":
        joule = float(input("Mesure en joule : "))
        print("Mesure en watt-heure : " + str(joule_en_watth(joule)))
        continuer = demande_continuer()

    elif choix == "4":
        joule = float(input("Mesure en watt-heure : "))
        print("Mesure en joule : " + str(watth_en_joule(joule)))
        continuer = demande_continuer()
   
    elif choix == "q":
        # On veut quitter
        continuer = False

    else:
        print("Option inconnue")

