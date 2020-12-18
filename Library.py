class Library:
    def __init__(self, readingRooms, specialFunds,registration,copyDepartment,catalog):
        self.readingRooms=readingRooms
        self.specialFunds=specialFunds
        self.registration=registration
        self.copyDepartment=copyDepartment
        self.catalog=catalog
        self.users=[]

    def showCopyDepartment(self):
        return self.copyDepartment

    def showRegistration(self):
        return self.registration

    def showSpecialFunds(self):
        return self.specialFunds

    def showReadingRoom(self):
        return self.readingRooms