import string
import random

translations = {
    'fr' : {
        'bienvenue': 'Bienvenue sur un générateur de mot de passe aléatoire.',
        'option_disponible': 'Voici les diverses options disponibles : \n 1 - Limite du programme \n 2 - Génerateur de mot de passe \n 3 - A propos  ',
        'option_choix' : 'Choisir une option',
        'limite_programme': "Le programme est capable de gênerer un mot de passe contenant de 1 à 100 caractères.\n Lorsque une option est invalide, le programme s'arretera avec l'erreur ' Erreur : Option Invalide'",
        'generateur_motpasse' :'Génerateur de mot de passe \n ',
        'choix_lettre' : 'Souhaitez vous que votre mot de passe utilise des lettres? (Y / N)',
        'utilisation_lettre' : 'Votre mot de passe utilisera des lettres',
        'no_utilisation_lettre' : "Votre mot de passe n'utiliseras pas de lettre",
        'option_invalide' : "Erreur : Option Invalide",
        'choix_nombre' : 'Souhaitez vous utiliser des chiffres ? (Y / N)',
        'utilisation_nombre' : 'Votre mot de passe utilisera des chiffres',
        'no_utilisation_nombre' : "Votre mot de passe n'utiliseras pas de chiffre",
        'choix_ponctuation' : 'Souhaitez vous utiliser des symboles de ponctuations ? (Y / N)',
        'utilisation_ponctuation' : 'Votre mot de passe utilisera des symboles de ponctuations',
        'no_utilisation_ponctuation' : "Votre mot de passe n'utiliseras pas des symboles de ponctuations",
        'nbr_caractere' : 'Veuillez choisir le nombre de caractères souhaités:',
        'a_propos' : "Ce programme permet de gênerer un mot de passe en utilisant les chiffres,lettres et ponctuations (au choix) afin que celui-ci soit sécurisé. \nLe programme est developpé en python3 et utilise la librairie 'random'"
    },
    'en':{
        'bienvenue' : 'Welcome to a random generator password',
        'option_disponible' : ' Available option : \n 1 - Limit of program \n 2 - Generator of password \n 3 - Timely  ',
        'option_choix' : 'Choose a option',
        'limite_programme': "This programs is able generate password contain 1 to 100 characters. \n If one option is invailable, programs stop with error : 'Error : Invalid Option' ",
        'generateur_motpasse' :'Generator of password\n ',
        'choix_lettre' : 'Would you like use letters in your password? (Y / N)',
        'utilisation_lettre' : 'Password use letters',
        'no_utilisation_lettre' : "Password not use letters",
        'option_invalide' : " Error : Invalid Option",
        'choix_nombre' : 'Would you like use number in your password?(Y / N)',
        'utilisation_nombre' : 'Password use number',
        'no_utilisation_nombre' : "Password not use number",
        'choix_ponctuation' : 'Would you like use punctuation in your password? (Y / N)',
        'utilisation_ponctuation' : 'Password use punctuation',
        'no_utilisation_ponctuation' : "Password not use punctuation",
        'nbr_caractere' : 'Choose number of characters for your password: ',
        'a_propos' : "This programs generate password used number,letter and punctuation.\n This programs developped in Python3 and used 'random' library"
    
    }
}
def generator(lenght_char):

    password = ''.join(random.choice(character) for _ in range(lenght_char))
    return password
langue = input("Choose your language (fr/en)")
print (translations[langue]['bienvenue'])
print (translations[langue]['option_disponible'])
while True:
    choose =input(translations[langue]['option_choix'])
    if choose == "1":
        print(translations[langue]['limite_programme'])
        


    elif choose == "2":
        print(translations[langue]['generateur_motpasse'])
        ascii_letters_choose = input(translations[langue]['choix_lettre'])
        # Choix des lettres 
        if ascii_letters_choose == "Y":
            character = string.ascii_letters
            print (translations[langue]['utilisation_lettre'])
        elif ascii_letters_choose == "N":
            print (translations[langue]['no_utilisation_lettre'])
            character= ""
        else:
            print(translations[langue]['option_invalide'])
            break
            
#Choix des chiffres 
        digits_choose = input(translations[langue]['choix_nombre'])
        if digits_choose == "Y":
            character = character + string.digits
            print (translations[langue]['utilisation_nombre'])
        elif digits_choose == "N":
            character = character
            print (translations[langue]['no_utilisation_nombre'])
        else:
            print(translations[langue]['option_invalide'])
            break
#Choix des ponctuations 
        punctuation_choose = input(translations[langue]['choix_ponctuation'])
        if punctuation_choose == "Y":
            character = character + string.punctuation
            print (translations[langue]['utilisation_ponctuation'])
        elif punctuation_choose == "N":
            character = character
            print (translations[langue]['no_utilisation_ponctuation'])
        else:
            print(translations[langue]['option_invalide'])
            break
# Choix du nombre de caracteres
        nbr_character= input(translations[langue]['nbr_caractere'])
        int_nbr_character= int(nbr_character)
        if 2 <= int_nbr_character <= 100:
            password = generator(int_nbr_character)
            print ("PASSWORD:  ", password)
            break
        else:
            print(translations[langue]['option_invalide'])

    elif choose == "3":
            print(translations[langue]['a_propos'])
        
    else:
        print(translations[langue]['option_invalide'])