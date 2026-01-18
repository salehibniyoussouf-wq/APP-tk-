
import tkinter as tk



# fenetre principale
root = tk.Tk()
root.title("Gestionnaire de tâches")
root.geometry("500x500")
liste_taches = tk.Listbox(root)
liste_taches.pack()

taches = {}

# Entry
entrer_taches = tk.Entry(root)
entrer_taches.pack()


def marquer_taches(event):
    print("Un clic detecté")
    if not event.widget.curselection():
        return
    index = event.widget.curselection()[0]
    nom_tache = list(taches.keys())[index]
    taches[nom_tache] = not taches[nom_tache]
    mettre_a_jour_liste()
    print("index:", index)
    print("texte:", nom_tache)
    print("statut", taches[nom_tache])


liste_taches.bind("<<ListboxSelect>>", marquer_taches)

def mettre_a_jour_liste():
    liste_taches.delete(0, tk.END)
    for nom_tache in taches:
        fait = "✔"
        non_fait = "✘"
        if taches[nom_tache] == True:
            liste_taches.insert(tk.END, f"{nom_tache} {fait}")
        elif taches[nom_tache] == False:
            liste_taches.insert(tk.END, f"{nom_tache} {non_fait}")


def ajouter_taches():
    nom_tache = entrer_taches.get()
    if nom_tache != "" :
        taches[nom_tache] = False
        mettre_a_jour_liste()
        entrer_taches.delete(0, tk.END)


def supprimer_taches():
    if not liste_taches.curselection():
        print("Erreur de suppression")
        return
    selection = liste_taches.curselection()[0]
    nom_tache = list(taches.keys())[liste_taches.get(selection)]
    del taches[nom_tache]
    mettre_a_jour_liste()




# Bouton ajouter
tk.Button(root, text="Ajouter", command=ajouter_taches).pack()
tk.Button(root, text="Supprimer", command=supprimer_taches).pack()

root.mainloop()





