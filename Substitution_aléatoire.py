from unicodedata import name
from random import shuffle

List_shuffled = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

Message = input("Entre votre message : ")
shuffle(List_shuffled)
print(List_shuffled)

Message = Message.lower()

List = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def chiffre_lettre(lettre, liste, list1) :
    for i in range(len(liste)):
        if lettre == ' ':
            return ' '
        elif liste[i] == lettre:
            return str(list1[i])
    return '?'
def dech_lettre(lettre, liste, liste1):
    for i in range(len(liste)):
        if lettre == ' ':
            return ' '
        elif liste1[i] == lettre:
            return str(liste[i])
    return '?'

Message_chff = str()
for lettre in Message:
    Message_chff += chiffre_lettre(lettre, List, List_shuffled)

Message_dech = str()
for lettre in Message_chff:
    Message_dech += dech_lettre(lettre, List, List_shuffled)


if __name__ == '__main__':
    print('Le Message chiffré : '+ Message_chff)
    print('Le Message déchifré : '+ Message_dech)