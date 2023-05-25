from tinydb import TinyDB, Query
db = TinyDB('budget_db.json') 
depenses_table = db.table('depense')
revenus_table = db.table('revenus')

def enregistrement_depense():
    montant = int(input("montant de la depense : "))
    categorie = input("categorie de la depense:")
    depense = {"montant": montant, "categorie": categorie}
    depenses_table.insert(depense)
    print("la depense a été enregistré avec succés")
    
def enregistrement_revenu():
    montant = int(input("montant de la revenue: "))    
    categorie = input("categorie de la revenue: ")
    revenu = {"montant": montant, "categorie": categorie}
    revenus_table.insert(revenu)
    print("le revenu a été enregistré avec succés.")
    
def calculer_ecart():
    total_depenses = sum(depense["montant"] for depense in depenses_table.all() )    
    total_revenus = sum(revenu["montant"] for revenu in revenus_table.all() )
    ecart = total_revenus - total_depenses
    print("l'ecart entre les dépenses et les revenus sont : ", ecart)
    
def menu():
    while True :
        print("\n=== Gestion de budget ===")    
        print("1. Enregistrer une dépense")
        print("2. Enregistrer un revenu")
        print("3. Calculer l'ecart entre dépenses et revenus")
        print("4. Quitter")
        choix = input("Veuillez entrer votre choix : ")
        
        if choix == "1":
            enregistrement_depense()
        elif choix == "2":
            enregistrement_revenu()
        elif choix == "3":
            calculer_ecart()
        elif choix == "4":
            break            
        else:
            print("choix invalide. Veuillez réessayer")
            
menu()           
