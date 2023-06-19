import tkinter as tk 
from ManageDB import *
from tkinter import messagebox
class RaspInterface(object):
    def __init__(self,windows,uid):
        self.windows=windows
        self.uid=uid
        self.Sql=ConfigureBD("Rfiddb.bd")
        self.windows.resizable(0,0)
        self.windows.title("RaspInterface")
        self.windows.geometry(f"{300}x{170}+{int(self.windows.winfo_screenwidth()//2 - 800//2)}+{int(self.windows.winfo_screenheight()//2 - 500//2)}")
        self.add=tk.Button(self.windows,text="Ajouter",font="AgencyFB 10 bold",justify="center",bg="red",fg="white",width=8,height=2,bd=5,cursor="hand2",command=self.Add)
        self.add.place(x=10,y=70)
        self.frame=tk.Frame(self.windows,width=300, height=200,background="blue", border=2, relief="groove")
        self.frame.place(x=95,y=20)
        
        self.label1 = tk.Label(self.frame, text="Nom:")
        self.label1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.entry1 = tk.Entry(self.frame)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)

        self.label2 = tk.Label(self.frame, text="Matricule:")
        self.label2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.entry2 = tk.Entry(self.frame)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        self.label3 = tk.Label(self.frame, text="Prénom:")
        self.label3.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.entry3 = tk.Entry(self.frame)
        self.entry3.grid(row=2, column=1, padx=5, pady=5)

        self.label4 = tk.Label(self.frame, text="Uid:")
        self.label4.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.entry4 = tk.Entry(self.frame)
        self.entry4.grid(row=3, column=1, padx=5, pady=5)
        
        if self.Sql.get_rfid_badge(self.uid):
            self.entry1.insert(1,self.Sql.get_rfid_badge(self.uid)[1])
            self.entry2.insert(1,self.Sql.get_rfid_badge(self.uid)[0])
            self.entry3.insert(1,self.Sql.get_rfid_badge(self.uid)[2])
            self.entry4.insert(1,self.uid)
        else:
            self.entry1.insert(1,"")
            self.entry2.insert(1,"")
            self.entry3.insert(1,"")
            self.entry4.insert(1,self.uid)
            
    
    def Add(self):
        self.nom=self.entry1.get()
        self.prenom=self.entry2.get()
        self.matricule=self.entry3.get()
        if self.Sql.get_rfid_badge(self.uid)==False:
            self.Sql.add_rfid_badge(self.matricule,self.nom,self.prenom,self.uid)
            messagebox.showinfo("Info","Ajout Effectue avec Success")
        else :
            messagebox.showerror("Erreur","Deja Existant")
        
        


if __name__=="__main__":

        windows=tk.Tk()
        while True :
            uid="13"
            RaspInterface(windows,uid)
            windows.mainloop()
        
            