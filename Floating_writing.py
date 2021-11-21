#La fonction suivante permet de convertir un nombre décimal en binaire
def DecToBin(nb):
    try :
        list=[]
        quotient,reste=nb,0
        if nb==0:
            list=[0]
        while quotient!=0:
            reste=quotient%2
            list.append(reste)
            quotient=quotient//2
        return list
    except :
        print("Erreur durant la conversion décimale->binaire \nLe type de l'argument doit être un nombre entier naturel.")

# La fonction suivante permet d'extraire et d'afficher les différents éléments d'écriture flottante en simple précision d'un nombre telle que python la donne
def EcritureFlottante(nb):
    import struct
    charnb=''.join('{:08b}'.format(b) for b in struct.pack('>f', float(nb)))
    print(charnb)
    signe=[int(charnb[0])]
    exposant=[]
    mantisse=[]
    for bit in charnb[1:9]:
        exposant.append(int(bit))
    for bit in charnb[9:32]:
        mantisse.append(int(bit))
    #On donne le bit du signe
    print("Bit du signe : " + str(signe))
    #On donne l'exposant du bit
    print("Exposant : " + str(exposant))
    #On donne la mantisse du bit
    print("Mantisse : " + str(mantisse))
    return[signe,exposant,mantisse]   

#L'argument doit être un nombre entier
print(DecToBin(7))
#Fonctionne avec des nombres entier mais aussi flottant
print(EcritureFlottante(-6.625))