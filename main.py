from datetime import date
from Library import *
from ReadingRoom import *
from Bibliographer import *
from Catalog import collectionRussianBookFund
from Catalog import collectionUniversalReadingRoom
from SpecialFund import *
from Registration import *
from CopyDepartment import *
from Reader import *
from LibraryCard import *

#создание библиографа для читального зала
dutyBibliographerOne = Bibliographer("Nick")
dutyBibliographerTwo = Bibliographer("Vlad")

#создание читальных залов
readingRooms=[]
readingRooms.append(ReadingRoom(dutyBibliographerOne,collectionUniversalReadingRoom,0,"Универсальный читальный зал"))
readingRooms.append(ReadingRoom(dutyBibliographerTwo,collectionRussianBookFund,1,"Русский книжный фонд"))

#создание читателя
person=Reader(LibraryCard(34,"Иванов Иван Иванович",[],date(2019,9,1),"Ю"))

#создание библиотеки
library = Library(readingRooms,SpecialFund("Закрытый фонд"),Registration(),CopyDepartment(),None)

person.comeToLibrary(library)
library.users[0].takeChecklist(0)
library.users[0].enterReadingRoom(library.readingRooms[0])
library.readingRooms[0].dutyBibliographer.pickUpChecklist(library.users[0].checklist)
library.users[0].requestHelpFromBibliographer(library.readingRooms[0].dutyBibliographer,Book("Рай и Ад","Умар Сулейман аль-Ашкар",None,None,None,None,None,None,None,None))


print(library.users[0].booksTaken[0].title)
