import random
import string


#1
def mot_inves(mot):
    return mot[::-1]
mot_correct=("institution")
mot_inverse=mot_inves(mot_correct)
print(mot_inverse)

#2

def genere_kod_aleyatwa(n):
    lettre=string.ascii_letters
    code=''.join(random.choice(lettre) for _ in range(n))
    return code
kod_aleyatwa=genere_kod_aleyatwa(8)
print(kod_aleyatwa)

#3
def generer_code_aleatoire(n):
    if n > 52:
        raise ValueError("N pa ka plis pase 52 paske nou gen sèlman 52 lèt alfabetik.")
    alphabet = list(string.ascii_letters) 
    if n > len(alphabet):
        raise ValueError("N pa ka plis pase " + str(len(alphabet)) + " paske nou gen sèlman 52 lèt alfabetik.")

    code = random.sample(alphabet, n)
    code = ''.join(code)
    return code
kod_aleyatwa = generer_code_aleatoire(10)
print(kod_aleyatwa)

#4
def  generer_code_aleatoire(n):
    caracteres = string.ascii_letters + string.digits  
    if n > len(caracteres):
        raise ValueError("N pa ka plis pase " + str(len(caracteres)) + " paske nou gen sèlman lèt ak chif yo.")

    code = ''.join(random.sample(caracteres, n))
    return code
# kreye yon kòd de 8 karaktè alfanimerik san repetisyon
kod_aleyatwa = generer_code_aleatoire(8)
print(kod_aleyatwa)


#6
def separe_let_ak_vigil(mot, vigil):
    mot_separe = ""
    for lettre in mot:
        mot_separe += lettre + vigil
    return mot_separe
mot_original = "hello"
vigil = "-"
mot_separe = separe_let_ak_vigil(mot_original, vigil)
print(mot_separe)

#7
def kripte_avek_endeks(mot):
    alfabè = "abcdefghijklmnopqrstuvwxyz"  # Alfabè a
    mot_kripte = ""

    for lettre in mot:
        lettre = lettre.lower()  # Konvèti lèt yo nan minis kòm ekzanp
        if lettre in alfabè:
            endeks = alfabè.index(lettre)
            mot_kripte += str(endeks) + "-"
        else:
            mot_kripte += lettre + "-"

    return mot_kripte.rstrip('-')  # Retire dènye tirè nan dènye po a
mot_original = "ALO"
mot_kripte = kripte_avek_endeks(mot_original)
print(mot_kripte)

#8
def dekripte_mo(mo_kripte):
    alfabe = "abcdefghijklmnopqrstuvwxyz"  # Alfabe a
    mo_dekripte = ""  # stoke mo a dekripte a

    endeks_let = mo_kripte.split("-")  # Separe mo a nan endeks yo

    for endeks in endeks_let:
        if endeks.isdigit():
            endeks = int(endeks)
            if 0 <= endeks < len(alfabe):
                mo_dekripte += alfabe[endeks]
            else:
                mo_dekripte += "?"  # Endeks la pa nan ranje korek
        else:
            mo_dekripte += ""  # Endeks la pa yon chif valide

    return mo_dekripte

mo_kripte = "0-11-14"
mo_dekripte = dekripte_mo(mo_kripte)
print(mo_dekripte)  
    
#9
def retounen_inisyal(mo):
    mo_san_espas = mo.replace("-", " ")  # Elimine tire yo ak remplace yo avèk espas
    mo_san_espas = mo_san_espas.split()  # Separe mo yo dapre espas yo

    inisyal = ""
    for mo in mo_san_espas:
         if len(mo) > 0 and not mo[0].isnumeric():
            inisyal += mo[0].upper()

    return inisyal
mo = "Jean-Ronald, payen"
inisyal = retounen_inisyal(mo)
print(inisyal)  # Afiche

    



