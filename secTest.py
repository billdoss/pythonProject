import pymysql
import os

class db:
    def __init__(self):
        self.conn = pymysql.connect(host="localhost",user="root",passwd="",db="gnm")
        self.cursor = self.conn.cursor()
        print("OK")

    
    #pour renvoyer tout les elements de la table nomTable
    def selectAll(self,nomTable):
        #connexionDatabase
        SQL = "SELECT * FROM " + nomTable
        print(SQL)
        self.cursor.execute(SQL)
        self.conn.commit()#lancer la requete
        tab = []
        for row in self.cursor.fetchall():
            #print(row[0],"  ",row[1],"  ",row[2],"  ",row[3])
            tab.append(row)
        if tab == []:
            raise ValueError("table pas dans la base")
        else :
            return tab


    #pour renvoyer tout en fonction de la condition where :'etat'
    def selectAllWhere(self,nomTable,etat):
        #connexionDatabase
        SQL = "SELECT * FROM " + nomTable + " WHERE " + etat
        print(SQL)
        self.cursor.execute(SQL)
        self.conn.commit()#lancer la requete
        tab = []
        for row in self.cursor.fetchall():
            #print(row[0],"  ",row[1],"  ",row[2],"  ",row[3])
            tab.append(row)
        if tab == []:
            raise ValueError("elt pas dans la table")
        else:
            return tab


            # pour afficher tout en fonction de la condition where:etat

    def selectAllWhereTo(self, nomTable, colTable, etat):
        # connexionDatabase
        i=0
        sql = "SELECT * FROM " + nomTable + " WHERE "
        while(i< len(colTable)):
            sql += str(colTable[i]) + "='" + str(etat) + "'"
            i +=1
            if (i < len(colTable)):
                sql += " OR "
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()  # lancer la requete
        tab = []
        for row in self.cursor.fetchall():
            # print(row[0],"  ",row[1],"  ",row[2],"  ",row[3])
            tab.append(row)
        if tab == []:
            raise ValueError("elt pas dans la table")
        else:
            return tab




    def queryInsert(self,nomTable, contenuTableau):
        #connexionDatabase
        if "" in contenuTableau :
            raise ValueError("inserer un element valide dans la table")
        i = 0
        SQL = "INSERT INTO " + nomTable + " VALUES(";

        while (i <= len(contenuTableau) - 1):
            SQL += "'" + contenuTableau[i] + "'"
            if (i < len(contenuTableau) - 1):
                SQL += ","
            i = i + 1
        SQL += ")";
        self.cursor.execute(SQL)
        self.conn.commit()  # lancer la requete




    #inserer dans la table des valeurs en ft de leurs label contenu
    #dans nomcolone(surcharge)
    #les colones doivent avoir une valeur par defaut ou accepter le null

    def queryInsertTwo(self,nomTable, nomColonne, contenuTableau):

        #connexionDatabase();
        i=0;
        SQL = "INSERT INTO " + nomTable + "(";
        while (i <= len(nomColonne) - 1):
            SQL += nomColonne[i];
            if (i < len(nomColonne) - 1):
                SQL += ","
            i=i+1            
        SQL += ") VALUES(";
        i = 0;
        while ( i <= len(contenuTableau) - 1):
            SQL += "'" + contenuTableau[i] + "'";
            if (i < len(contenuTableau) - 1):
                SQL += ",";
            i=i+1
            
        SQL += ")";
        self.cursor.execute(SQL)
        self.conn.commit()#lancer la requete


    #modif des colones listés avec une cond where
    def queryUpdate(self, nomTable, nomColonne, contenuTableau, etat):
        #connexionDatabase();
        i =0
        SQL = "UPDATE " + nomTable + " SET "
        i = 0;  
        while (i <= len(nomColonne) - 1):
            SQL += nomColonne[i] + "='" + contenuTableau[i] + "'";
            if (i < len(nomColonne) - 1):
                SQL += ","
            i=i+1       
        SQL += " WHERE " + etat
        self.cursor.execute(SQL)
        self.conn.commit()#lancer la requete



    # modif des colones listés avec une cond where
    def queryUpdateTo(self, nomTable, nomColonne, contenuTableau, etat):
        # connexionDatabase();
        i = 0
        SQL = "UPDATE " + nomTable + " SET "

        while (i <= len(nomColonne) - 1):
            SQL += nomColonne[i] + "='" + contenuTableau[i] + "'";
            if (i < len(nomColonne) - 1):
                SQL += ","
            i = i + 1
        SQL += " WHERE "
        i = 0
        while (i < len(nomColonne)):
            SQL += str(nomColonne[i]) + "='" + str(etat) + "'"
            i += 1
            if (i < len(nomColonne)):
                SQL += " OR "
        print(SQL)
        self.cursor.execute(SQL)
        self.conn.commit()  # lancer la requete




    #suppression des elements de la table
    def queryDelete(self, nomtable):
        #connexionDatabase
        SQL = "DELETE FROM " + nomtable
        self.cursor.execute(SQL)
        self.conn.commit()



    #surcharge de la fonction precedente avec une cond where
    def queryDeleteTwo(self, nomTable, etat):
        #connexionDatabase
        SQL = "DELETE FROM " + nomTable + " WHERE " + etat;
        self.cursor.execute(SQL)
        self.conn.commit()



    # surcharge de la fonction precedente avec une cond where
    def queryDeleteTo(self, nomTable, colTable, etat):
        # connexionDatabase
        i = 0
        sql = "DELETE FROM " + nomTable + " WHERE "
        while (i < len(colTable)):
            sql += str(colTable[i]) + "='" + str(etat) + "'"
            i += 1
            if (i < len(colTable)):
                sql += " OR "
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()

#data = db()
#t = data.selectAllWhere("gnmtb21","mot_passe='gn123' AND nom_utilisateur = 'adiko'")
#print(t[0][0])
