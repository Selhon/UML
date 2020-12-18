from CopyPublication import CopyPublication
class CopyDepartment:
    def __init__(self):
        self.queueOrders=[]
    def makeCopy(self):
        currOrder=self.queueOrders[0]
        currCopy=CopyPublication(currOrder[1].name,currOrder[1].author,currOrder[0],currOrder[1].content,currOrder[1].language)
        self.queueOrders.remove(currOrder)
        return currCopy
    def addOrder(self,reader,book):
        currOrder=[reader,book]
        self.queueOrders.append(currOrder)


#в разработке
    def getListOrders(self):
        return 0
    def isBookInDepartment(self):
        return 0