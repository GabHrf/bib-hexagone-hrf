import socketserver
import json
import sys

class Livre:
    def __init__(self, nom, tag, image):
        self.__nom = nom
        self.__tag = tag
        self.__image = image

    def __str__(self):
        return f"Livre: {self.__nom}\nTag: {self.__tag}\nImage: {self.__image}\n"
    
    @property
    def nom(self):
        return self.__nom
    @property
    def tag(self):
        return self.__tag
    @property
    def image(self):
        return self.__image
    

class LivreEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Livre):
            return {
                "nom": obj.nom,
                "tag": obj.tag,
                "image": obj.image
            }
        return super().default(obj)
    
        
class Bibliotheque:
    def __init__(self):
        self.__livres = []
    
    def ajouter_livre(self, livre):
        self.__livres.append(livre)
    
    def supprimer_livre(self, nom):
        for livre in self.__livres:
            if livre.__nom == nom:
                self.__livres.remove(livre)
    
    def lister_livres(self):
        if not self.__livres:
            print("Aucun livre dans la bibliothèque.")
        else:
            for livre in self.__livres:
                print(livre)
    
    def detail_livre(self, nom):
        for livre in self.__livres:
            if livre.__nom == nom:
                print(livre)
    
    def sauvegarder(self):
        with open("bibliotheque.json", "w") as f:
            json.dump([livre.__dict__ for livre in self.__livres], f)

def menu():
    print("1. Ajouter un livre")
    print("2. Supprimer un livre")
    print("3. Lister les livres")
    print("4. Détail d'un livre")
    print("5. Sauvegarder")
    print("6. Charger")
    print("7. Quitter")
    choix = input("Votre choix : ")
    return choix

def main():
    bibliotheque = Bibliotheque()
    bibliotheque.charger()
    
    while True:
        choix = menu()
        
        if choix == "1":
            nom = input("Nom : ")
            tag = input("Tag : ")
            image = input("Image : ")
            livre = Livre(nom, tag, image)
            bibliotheque.ajouter_livre(livre)
        elif choix == "2":
            nom = input("Nom : ")
            bibliotheque.supprimer_livre(nom)
        elif choix == "3":
            bibliotheque.lister_livres()
        elif choix == "4":
            nom = input("Nom : ")
            bibliotheque.detail_livre(nom)
        elif choix == "5":
            bibliotheque.sauvegarder()
        elif choix == "6":
            bibliotheque.charger()
        elif choix == "7":
            sys.exit(0)
        else:
            print("Choix invalide")

class Server(socketserver.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("Received from {}:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), Server) as server:
        server.serve_forever()

if __name__ == "__main__":
    main()