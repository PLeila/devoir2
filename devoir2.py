#1
phrase=("DIEU EST TOUT POUR MOI")
print (phrase.lower())
#2
cutcaracters=("hello we are here to practice python")
print(cutcaracters.split())
#3
firstletter=("happy birthday leila")
print(firstletter.title())

#4  
ma_chaine=("il est important de travailler" )
A=ma_chaine.split()
b= ''.join([i[0] for i in A])
print(b)
 

#5
fraz=("ranplase tout karacte a par @")
b=(fraz.replace('a','@'))
print(b)

#6 Mete yon chenn karaktè devan dèyè, answit mete l an majiskil.
chaine=("nouvle yon lot ayiti.")
inv=chaine[:: -1]
print(inv.upper())

#7 Afiche endeks premye karaktè "a" ki nan yon chenn
chaine= ("happy new year")
var=chaine.index('a')
print(var)

#8Afiche total tout endeks karaktè "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil)
chaine="Ayiti kapab"
long=len(chaine)
ind=0
j=0
for ch in range(long):
    if chaine[j]=="A"or chaine[j]=="a":
       ind += j
    j +=1
print(ind)
        
#9 Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a miniskil) en python
lis=("Ayiti kapab avanse")
karakte='a'
indices_a = [i for i, caractere in enumerate(lis) if caractere ==karakte]
print(indices_a)

#10 Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen (Pa kontwole espas yo)
chenn=(" lavi pap diw")
newchenn=chenn.replace(" ","")
chenn_colle=newchenn + ""
print(chenn_colle)





