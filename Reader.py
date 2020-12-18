from Checklist import *
from datetime import datetime
class Reader:
    def __init__(self,card):
        self.fullName=card.fullNameReader
        self.libraryCard=card
        self.checklist=None
        self.booksTaken=[]

    def takeChecklist(self,number):
        self.checklist=Cheklist(number,datetime.now(),self.fullName)

    def requestHelpFromBibliographer(self,bibliographer,book):
        self.booksTaken.append(bibliographer.findBookTitleAuthor(self.checklist.number, book.title,book.author))

    def enterReadingRoom(self,room):
        room.addReader(self)

    def set_name(self):
        return self.fullName
    def receiveBooks(self, books):
        for i in range(len(books)):
            self.booksTaken.append(books[i])
    def returnBooks(self):
        return self.booksTaken
    def comeToLibrary(self,library):
        library.users.append(self)

#в разработке

    def useElectronicCatalog(self):
        return 0
    def requestAccessToSpecialFund(self):
        return 0
    def submitRequestForPhotocopying(self):
        return 0
    def replaceLibraryCard(self):
        return 0