import sys
from datetime import datetime

def ajouter_heure_au_fichier(chemin_fichier):
    try:
        with open(chemin_fichier, 'a') as fichier:
            heure_actuelle = datetime.now().strftime("%H:%M:%S")
            fichier.write('\n' + heure_actuelle)
        print("L'heure a été ajoutée au fichier avec succès.")
    except FileNotFoundError:
        print("Erreur : Le fichier spécifié n'existe pas.")
    except PermissionError:
        print("Erreur : Permission refusée pour accéder au fichier.")
    except Exception as e:
        print("Une erreur s'est produite :", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilisation : python script.py <chemin_vers_fichier>")
    else:
        chemin_fichier = sys.argv[1]
        ajouter_heure_au_fichier(chemin_fichier)
