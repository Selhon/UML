class Cheklist:
    def __init__(self,number,dateTime,nameReader):
        self.number=number
        self.dateTime=dateTime
        self.listBook=[]
        self.nameReader=nameReader
        self.nameBibliographer=None
    def addBibliographer(self,name):
        self.nameBibliographer=name
    def addBookToList(self, book):
        self.listBook.append(book)
    def removeBookFromList(self,book):
        self.listBook.remove(book)

#в разработке
    def showList(self):
        return 0

