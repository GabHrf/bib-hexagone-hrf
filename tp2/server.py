import socketserver
import json
import sys

class Book:
    def __init__(self,nom, tag, image):
        self.__nom = nom
        self.__tag = tag
        self.__image = image

    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self,value):
        self.__nom = value
    
    @property
    def tag(self):
        return self.__tag
    
    @tag.setter
    def tag(self,value):
        self.__tag = value
    
    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self,value):
        self.__image = value

    def __str__(self):
        return f'Book: {self.__nom} ({self.__tag})'

class BookEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj, Book):
            return {
                'nom': obj.nom,
                'tag': obj.tag,
                'image': obj.image
            }

class Library:
    def __init__(self):
        self.__books = []

    def add_books(self, book):
        self.__books.append(book)

    def display_books(self):
        for book in self.__books:
            print(book)
    
    def delete_books(self, nom):
        book_to_delete = None
        for book in self.__books:
            if(book.nom == nom):
                book_to_delete = book
        self.__books.remove(book_to_delete)

    def save(self):
        with open('bib.json', 'w') as output:
            save_str = json.dumps(self.__books, cls = BookEncoder)
            output.write(save_str)
    
if __name__ == '__main__':
    lib = Library()
    lib.display_books()
    lib.add_books(Book('fondation', 'sf', 'path/to/image'))
    lib.add_books(Book('Test', 'sf', 'path/to/image'))
    lib.display_books()
    print('\n')
    lib.save()
    lib.delete_books('Test')
    lib.display_books()
    

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