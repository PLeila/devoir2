#1 Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
n=20
elem_pair=[]
for i in range(n + 1):
    if i%2==0:
        elem_pair.append(i)
print(elem_pair)

#2 
list_antye=[1,2,3,4,5,6,7,8,9]
list_chenn=[str(element)for element in list_antye]
print(list_chenn)

#3
list_chain_minuscule=["la lune","le soleil","la terre"]
list_chain_majuscule=[mot.upper() for mot in list_chain_minuscule ]
print(list_chain_majuscule)

#4
liste=[1,2,3,4,5,6,7,8,9,10]
nouvel=[]
for el in liste:
     if el%3==0:
      nouvel.append(el)
print(nouvel)

#5
ma_liste=[1,2,3,4,5,6,7,8,9,10]
#divise en groupe de 3
groupe_3=[ma_liste[i:i+3]for i in range(0,len(ma_liste),3)]
print(groupe_3)

#6
liste=[1,1,2,2,3,3,4,5,6,7,7,8,8,9]
liste_sans_doublons=list(set(liste))
print(liste_sans_doublons)

#7
list_1=[1,2,3,4,5,6,79,0,7]
list_2=[1,2,356,67,79,0,8,4]
list_mixte=[x for x in list_1 if x in list_2]
print(list_mixte)

#8
list_1=[1,2,3,5,6]
list_2=[3,4,5,6,7]

el_distinguable=list(set(list_1)^set(list_2))
print(el_distinguable)

#9
my_dictionnary={'a':1,'b':2,'c':4,'d':9}
cles= list(my_dictionnary.keys())
valeurs=list(my_dictionnary.values())
print("liste des cles",cles)
print("liste des valeurs",valeurs)

#10
liste1=[1,2,3,4,5,6]
liste2=[1,4,5,6,7,8]
liste3=[7,1,23,4,5,690]
ens_san_doublon=set(liste1+liste2+liste3)
list_sans_doublon=list(ens_san_doublon)
print(list_sans_doublon)