#1
dictionnaire={'a':1,'b':2,'c':3,'d':4}
vale=list(dictionnaire.values())
kle=list(dictionnaire.keys())
print("vale yo:",vale)
print("kle ki koresponn:",kle)

#2
valeur=input(print("taper yon vale: "))
if "{" in valeur and "}"in valeur:
    print(" gen akolad avan e apre")
else:
    print(" pa gen akolad avn e apre")

#3 
dictione={'a':1,'b':2,'c':3}
for cle in dictione.keys():
    print(cle)
    
#4 
dictione={'a':1,'b':2,'c':3}
for valeur in dictione.values():
    print(valeur)
     
#5
dictionnaire={'a':1,'b':2,'c':3}
nouvo_dik={}
for kle, eleman in dictionnaire.items():
    nouvo_dik[kle]= eleman
    
print(nouvo_dik)


#6
diks={'a':"bonjour", 'b': "annee", 'c': 21, 'd': "hello", 'e':16}

for kle, val in diks.items():
    if isinstance(val, str):
        diks[kle]= "_" + val + "_"

print(diks)

#7
diks={'a':"bonjour", 'b': "annee", 'c': 21, 'd': "hello", 'e':16}
diksyone={}
for cle, valeur in diks.items():
    if isinstance(valeur, (int, float)):
        diksyone[cle] = valeur
print(diksyone) 

#8
dict={'a':1,'b':2,'c':4,'d':5}
lis_tipl=[(cle,valeur)for cle, valeur in dict.items()]
print(lis_tipl)

#9
liste_de_tuple = [('a', 1), ('b', 2), ('c', 3)]
dictionnaire = {}
for cle,value in liste_de_tuple:
    dictionnaire[cle]=value
print(dictionnaire)

#10
def fusionner_dictionnaires(dict1, dict2):
    fusion = {}

    # Fusionner les clés du premier dictionnaire
    for cle, valeur in dict1.items():
        if cle in dict2:
            if isinstance(valeur, int) and isinstance(dict2[cle], int):
                fusion[cle] = valeur + dict2[cle]
            elif isinstance(valeur, (str, list, set)) and isinstance(dict2[cle], (str, list, set)):
                fusion[cle] = valeur + dict2[cle]
        