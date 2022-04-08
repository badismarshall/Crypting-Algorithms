List = list (['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])

Message = input("Entre votre message : ")
a = int(input("Donner la valeur de a : ")) # le a doit etre premier avec 26
b = int(input("Donner la valeur de b : "))

def chiffre_lettre(lettre, liste) :
    for i in range(len(liste)):
        if lettre == ' ':
            return ' '
        elif liste[i] == lettre:
            k = a * i + b
            if k > 26 :
                k = k % 26
            return str(liste[k])
    return '?'

def dech_lettre(lettre, liste):
    for i in range(len(liste)):
        if lettre == " ":
            return " "
        elif lettre == liste[i]:
            y = i
            a_prime = pow(a, -1, 26)
            x = ((y- b) * a_prime ) % 26
            return liste[x]
    return '?'
Message_chff = str()

for lettre in Message:
    Message_chff += chiffre_lettre(lettre, List)

Message_dech = str()

for lettre in Message_chff:
    Message_dech += dech_lettre(lettre, List)

if __name__ == '__main__':
    print('Le Message chiffré : '+ Message_chff)
    print('Le Message déchifré : '+ Message_dech)