from math import pi

# liste des unités et des puissances correspondantes
expo1 = [10**-3, 10**-2, 10**-1, 10**0, 10**1, 10**2, 10**3, 10**-3, 10**0, 10**3, 10**6, 10**9]
unit1 = ["mL", "cL", "dL", "L", "daL", "hL", "kL", "cm3", "dm3", "m3", "dam3", "hm3", "km3"]

expo2 =[10**-3, 10**-2, 10**-1, 10**0, 10**1, 10**2, 10**3, 10**5, 10**6]
unit2 =["mg", "cg", "dg", "g", "dag", "hg", "kg", "q", "t"]

expo3 = [10**-9,10**-6,10**-3,10**-2,10**-1,10**0,10**1,10**2,10**3]
unit3 = ["nm","micrometre","mm","cm","dm","m","dam","hm","km",]

#-----------Formules des convertion------------

# --- Convertion des degrés en radians ---
def deg_en_rad(nbr):
    return nbr * pi / 180

# --- Convertion des radians en degrés ---
def rad_en_deg(nbr):
    return nbr * 180 / pi

# --- Convertion des joules en whatt-heures ---
def joule_en_watth(nbr):
    return nbr / 3600

# --- Convertion des watt-heures en joules ---
def watth_en_joule(nbr):
    return nbr * 3600


def demande_continuer():
    reponse = input("Effectuer une autre conversion ? (O/N) :\n ")
    if reponse == "N" or reponse == "n":
        return False
    elif reponse == "O" or reponse == "o":
        menu()


def volume():
    nbr = float(input("Quel nombre doit etre converti ? "))
    print("liste des unites : \n0 : mL\t1 : cL\t 2 : dL\n3 : L \t4 : daL\t5 : hL\n6 : kL\t7 : cm3\t8 : dm3\n9 : m3\t10 : dam3  11 : hm3\n12 : km3")
    unit_d1 = int(input("Unite du nombre de depart : "))
    unit_f1 = int(input("Unité dans lequel le nombre doit etre converti : "))
    convert1 = nbr * expo1[unit_d1] / expo1[unit_f1]
    print("Le resultat est : %.3e"%convert1, unit1[unit_f1])
    continuer = demande_continuer()

def angle():
    nbr = float(input("Quel nombre doit etre converti ? "))
    print("liste des convertions :\r 1 : radian => degre  2 : degre => radian ")
    angle_choix = int(input("Choix de la conversion : "))
    if angle_choix ==1:
        print("Mesure en degrés : " + str(rad_en_deg(nbr)))
        continuer = demande_continuer()
    elif angle_choix ==2:
        print("Mesure en radians : " + str(deg_en_rad(nbr)))
        continuer = demande_continuer()

def energie():
    nbr = float(input("Quel nombre doit etre converti ? "))
    print("liste des convertions :\r 1 : joule => watt heure  2 : watt heure => joules ")
    energie_choix = int(input("Choix de la conversion : "))
    if energie_choix == 1:
        print("Mesure en watt-heures : " + str(joule_en_watth(nbr)))
        continuer = demande_continuer()    
    elif energie_choix == 2:
        print("Mesure en joules : " + str(watth_en_joule(nbr)))
        continuer = demande_continuer()    
    
def masse():
    nbr = float(input("Quel nombre doit etre converti ?"))
    print("liste des unites : \n0 = mg\t1 = cg\t2 = dg\n3 = g     4 = dag   5 = hg\n6 = kg\t7 = q\t 8 = t")
    unit_d2 = int(input("Unite du nombre de depart : "))
    unit_f2 = int(input("Unité dans lequel le nombre doit etre converti : : "))
    convert2 = nbr * expo2[unit_d2] / expo2[unit_f2]
    print("Le resultat est :\n%.3e"%convert2, unit2[unit_f2])
    continuer = demande_continuer()

def longueur():
    nbr = float(input("Quel nombre doit etre converti ? "))
    print("liste des unites : \n0 = nm\t1 = micrometre\n2 = mm\t3 = cm\t4 = dm\n5 = m     6 = dam   7 = hm\n8 = km")
    unit_d3 = int(input("Unite du nombre de depart : "))
    unit_f3 = int(input("Unité dans lequel le nombre doit etre converti : "))
    convert3 = nbr * expo3[unit_d3] / expo3[unit_f3]
    print("Le resultat est :\n%.3e"%convert3, unit3[unit_f3])
    continuer = demande_continuer()

def menu():
    # Affiche le menu et renvoie le choix de l'utilisateur
    print("\n Grandeurs disponibles : ")
    print("1 : Volume")
    print("2 : Angle")
    print("3 : Energie")
    print("4 : Masse")
    print("5 : Longueur")
    choix = float(input("Choix de la grandeur : " ))

    if choix == 1:
        volume()
    elif choix == 2:
        angle()
    elif choix == 3:
        energie()
    elif choix == 4:
        masse()
    elif choix == 5:
        longueur()
    else:
        print("Option inconnue")
menu()

