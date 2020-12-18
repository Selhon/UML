class ReadingRoom:
    def __init__(self,bibliographer,collection,number,name):
        self.dutyBibliographer=bibliographer
        self.collection=collection
        self.users=[]
        self.number=number
        self.name = name
        bibliographer.room=self

    def removeReader(self,reader):
        self.users.remove(reader)
    def addReader(self,reader):
        self.users.append(reader)
    def showNumber(self):
        return self.number

#в разработке
    def changeBibliographer(self):
        return