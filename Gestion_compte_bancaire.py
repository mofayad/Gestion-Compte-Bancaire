# Dictionnaires pour la gestion des comptes
Client = {}
Compte = {}
ClientCompte = {}

def ajouterClient(numCl, MPC, numC, SoldeC):
    Client[numCl] = MPC
    Compte[numC] = SoldeC
    ClientCompte[numCl] = numC

def supprimerClient(numC):
    del ClientCompte[numC]
    del Client[next(key for key, value in ClientCompte.items() if value == numC)]
    del Compte[numC]

def modifierMPClient(numCl, newMP):
    Client[numCl] = newMP

def deposer(numCl, montant):
    numC = ClientCompte[numCl]
    Compte[numC] += montant

def retirer(numCl, montant):
    numC = ClientCompte[numCl]
    if Compte[numC] >= montant:
        Compte[numC] -= montant
    else:
        print("Solde insuffisant.")

genererNumCompte = lambda numCl: int(str(numCl) + str(random.randint(0, 100)))

import csv

def ecrireFichierCSV(filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Numéro Client', 'Code Secret']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for numCl, codeSecret in Client.items():
            writer.writerow({'Numéro Client': numCl, 'Code Secret': codeSecret})

def manipSTS():
    numComptesList = list(ClientCompte.values())
    numComptesTuple = tuple(ClientCompte.values())
    numComptesSet = set(ClientCompte.values())
    return numComptesList, numComptesTuple, numComptesSet

import random

def main():
    while True:
        print("1. Agent de la banque")
        print("2. Client de la banque")
        choice = int(input("Choisissez un utilisateur (1 ou 2): "))

        if choice == 1:
            print("1. Ajouter un compte")
            print("2. Supprimer un compte")
            agent_choice = int(input("Choisissez une action (1 ou 2): "))

            if agent_choice == 1:
                numCl = int(input("Numéro du client: "))
                MPC = input("Code secret: ")
                numC = genererNumCompte(numCl)
                SoldeC = float(input("Solde initial du compte: "))
                ajouterClient(numCl, MPC, numC, SoldeC)
                print("Compte ajouté avec succès.")
            elif agent_choice == 2:
                numC = int(input("Numéro du compte à supprimer: "))
                supprimerClient(numC)
                print("Compte supprimé avec succès.")

        elif choice == 2:
            print("1. Modifier son mot de passe")
            print("2. Afficher son solde")
            print("3. Déposer une somme d'argent")
            print("4. Retirer une somme d'argent")
            client_choice = int(input("Choisissez une action (1 à 4): "))
            numCl = int(input("Numéro du client: "))

            if client_choice == 1:
                newMP = input("Nouveau mot de passe: ")
                modifierMPClient(numCl, newMP)
                print("Mot de passe modifié avec succès.")
            elif client_choice == 2:
                print("Solde actuel:", Compte[ClientCompte[numCl]])
            elif client_choice == 3:
                montant = float(input("Montant à déposer: "))
                deposer(numCl, montant)
                print("Dépôt effectué avec succès.")
            elif client_choice == 4:
                montant = float(input("Montant à retirer: "))
                retirer(numCl, montant)
                print("Retrait effectué avec succès.")

        else:
            print("Choix invalide. Veuillez choisir 1 ou 2.")

if __name__ == "__main__":
    main()

