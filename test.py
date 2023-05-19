import tkinter as tk
import autre



def buton_click():
    if champ_saisie.get()=="12345":    
     print('le bouton a ete clique')
def buton() :
            autre
            
                

fenetre = tk.Tk()
bouton =  tk.Button(fenetre ,  text='cliquez ici', command=buton_click)
bouto =  tk.Button(fenetre ,  text='go', command=buton)
champ_saisie = tk.Entry(fenetre)

fenetre.geometry(f"{500}x{300}")

champ_saisie.pack()
bouton.pack()
bouto.pack()
fenetre.mainloop()