#1
def mot_inves(mot):
    return mot[::-1]
mot_correct=("institution")
mot_inverse=mot_inves(mot_correct)
print(mot_inverse)

#2
import random
import string
def genere_kod_aleyatwa(n):
    lettre=string.ascii_lowercase
    code=''