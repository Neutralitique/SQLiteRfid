import sqlite3

class ConfigureBD(object):
    def __init__(self,bd):
        
        self.bd=bd
        self.conn=sqlite3.connect(self.bd)
        self.cursor=self.conn.cursor()
        self.create_table()
        
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS rfid_badges
                             (Matricule TEXT NOT NULL,
                             Nom TEXT NOT NULL,
                             Prenom TEXT NOT NULL,
                             Uid TEXT NOT NULL)''')
        self.conn.commit()

    def add_rfid_badge(self, matricule,nom,prenom,uid):
        
        self.cursor.execute("INSERT INTO rfid_badges (Matricule,Nom,Prenom,Uid) VALUES (?,?,?,?)", (matricule,nom,prenom,uid,))
        self.conn.commit()
        
    def del_rfid_badge(self,uid):
        self.cursor.execute(f"DELETE * FROM rfid_badges WHERE Uid={uid}")
        self.conn.commit()
        
    def get_rfid_badge(self,uid):    
        self.cursor.execute(f"SELECT * FROM rfid_badges WHERE Uid={uid}")
        uid = self.cursor.fetchone()
        if uid:
            return uid
        else:
            return None

if __name__=="__main__":
    root=ConfigureBD("Rfiddb.bd")
    #root.add_rfid_badge("21INP00539","Amani","Maximin","12345678")
    print(root.get_rfid_badge("12345678"))
    

