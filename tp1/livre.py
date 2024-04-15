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
        print(json.dumps(self.__books, cls=BookEncoder))
    
if __name__ == '__main__':
    lib = Library()
    lib.display_books()
    lib.add_books(Book('fondation', 'sf', 'path/to/image'))
    lib.add_books(Book('Test', 'sf', 'path/to/image'))
    lib.display_books()
    print('\n')
    lib.delete_books('Test')
    lib.display_books()