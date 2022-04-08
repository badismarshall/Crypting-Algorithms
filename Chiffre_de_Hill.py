import numpy as np
List = list (['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])

# TaillBloc = int(input('Donner la taille des Blocs : '))
print('la taill de message doit > 2 ')

while (True):
    Message = input("Entre votre message : ")
    if (len(Message) >= 2):
        break

Message = Message.replace(' ', '')
Message = Message.lower()
if(len(Message) % 2 != 0):  # la taille de Message est impaire
    Message += 'x'          # ajoute x a la fin
    
# a = int(input('Donner la valeur de a : '))
# b = int(input('Donner la valeur de b : '))
# c = int(input('Doneer la valeur de c : '))
# d = int(input('Donner la valeur de d : '))

a = 9
b = 4
c = 5
d = 7

Matrix = np.matrix([[a, b],[c, d]])


def chiffre_lettre(lettre, lettre2, liste) :
    for i in range(len(liste)):
        if liste[i] == lettre:
            for j in range(len(liste)):
                if lettre2 == liste[j]:
                    Ck = a * i + b * j
                    Ck_1 = c * i + d * j
                    if Ck > 26:
                        Ck = Ck % 26
                    if Ck_1 > 26:
                        Ck_1 = Ck_1 % 26
                    return liste[Ck] + liste[Ck_1]
    return '?'

Inv =  pow(a * d - b * c, -1, 26) * np.matrix([[d, -b],[-c, a]])
Inv = Inv % 26
def dech_lettre(lettre, lettre2, liste):
    if np.linalg.det(Matrix) == 0:
        print("La matrice n'est pas inverssible")
    else:
        for i in range(len(liste)):
            if lettre == liste[i]:
                C1 = i
            if lettre2 == liste[i]:
                C2 = i
        C = np.matrix([[C1],[C2]])
        P = (Inv * C) % 26
        return str(liste[P[0,0]]+liste[P[1,0]])

Message_chff = str()

for i in range(0, len(Message), 2): # avec un pas de 2
    Message_chff += chiffre_lettre(Message[i], Message[i+1],List)
    
Message_dech = str()

for i in range(0, len(Message_chff), 2): # avec un pas de 2
    Message_dech += dech_lettre(Message_chff[i], Message_chff[i+1],List)
    
if __name__ == '__main__':
    print('Le Message chiffré : '+ Message_chff)
    print('Le Message déchifré : '+ Message_dech)