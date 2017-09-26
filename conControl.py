from style import Ui_MainWindow
from list_fonctions import heure, recupChamps, messagebox, trveGrpe
from secTest import db

class control(Ui_MainWindow):
    def __init__(self,MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)
        self.h=heure(self.heures)
        self.conLogin.clicked.connect(self.conVerification)
        self.conCancel.clicked.connect(MainWindow.close)
        self.data = db()

    def conVerification(self):
        tab = recupChamps(self.conPassword,self.conPseudo)#recupere tout les champs de l'interface
        print(tab)
        etat = "mot_passe='" + str(tab[0]) + "' AND "
        etat += "nom_utilisateur = '" + str(tab[1]) + "'"#on cree une une variable condition qu'on va passer a la fontion rechercher
        try:
            res = self.data.selectAllWhere("gnmtb21", etat)#on appelle la fonction rechercher dans "gnmtb21" quand "etat"
        except ValueError as faute:
            messagebox("se connecter", faute)
        else:#si la fonction rechercher renvoie un resultat, c que l'user existe; donc on va sur la page correspondante
            print(res[0])
            #self.stackedWidget.setCurrentIndex(int(trveGrpe(self.con_3)));
            self.stackedWidget.setCurrentIndex(2)

### faire en sorte que les tables recuperes des infos des autre tables qui lui sont liee
