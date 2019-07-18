import json
import os

class IOBooks:

    def __init__(self, dirname):
        self.dirname = dirname
    
    def load_book(self, filename):
        with open(self.dirname + '/' + filename, 'r', encoding='utf-8') as f:
            d = self.json.load(f)
            #print(d)
            #print("Owner:", d['Owner'])
            return d

    def load_books(self):
        filenames = os.listdir(self.dirname + '/')
        books = []
        for filename in filenames:
            d = load_book(filename)
            books.append(d)
        return books

    #print(load_book('example.json'))
    #print(load_books())

    #for book in load_books():
    #   print(book)

    def build_book(self, title, authors,      #wartości domyślne muszą być zawsze w kolejności po wart. wymaganych
            sub_title="",
            publisher="",
            publish_year=-1, 
            read_date="", 
            owner="", 
            user="", 
            rating=-1, 
            notes=""):
        d = {
            "Title": title,
            "Subtitle": sub_title,
            "Authors": authors,
            "Publisher": publisher,
            "PublishYear": publish_year,
            "ReadDate": read_date,
            "Owner": owner,
            "User": user,
            "Rating": rating,
            "Notes": notes,
        }
        return d

    def save_book(self, book):
        title = book["Title"]
        title = title.lower()
        title = title.replace(' ', '_')
        print(title)

        with open(self.dirname + '/' + title + ".json", "w") as f:
            json.dump(book,f)

books = IOBooks('books')
print(books.load_books())
#test
#a = build_book("Pan Tadeusz", ["Adam Mickiewicz"])
#print(save_book(a))