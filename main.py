from database.db_connect import Connection
from gui.mainWindow import Ui_MainWindow as window
from members import Member
from members import Dog
import sys
from PyQt5.QtWidgets import QApplication, QTreeWidgetItem
from PyQt5.QtGui import QPixmap
from gui.memberIDcard import Ui_memberIDCard as MemberCard
from gui.dogIDcard    import Ui_dogIDcard as DogID


class interface:
    data = Connection()
    app = QApplication(sys.argv)
    ui = window()

    members = {}
    dogs = {}
    displayedMember = None
    displayedDog = None

    def __init__(self):
        self.fetchDogs()
        self.fetchMembers()
        self.populateTree()
        self.listener()


        #self.data.close_db()
        sys.exit(self.app.exec())

    def listener(self):
        self.ui.treeWidget.itemDoubleClicked.connect(lambda: self.showMembershipCard(self.ui.treeWidget.currentItem().text(0)))


    def fetchDogs(self):
        self.dogs.clear()
        joinBreeds = " JOIN Breeds ON dogs.Breed_id = Breeds.Breed_id"
        joinMembers = " JOIN Members ON dogs.Owner_id = Members.Member_id"
        info = self.data.query(select=["Dog_id", "Dogs.name", "Breeds.name", "Members.name", "color", "dob", "dogs.photo"], fromTable="Dogs", additional=f"{joinBreeds}{joinMembers}")
        for dogInfo in info:
            #print(dogInfo)

            dog = Dog()

            dog.dogID, dog.name, dog.breed, dog.owner, dog.color, dog.dob, dog.photo = dogInfo

            self.dogs[dog.name] = dog

            dog.card = DogID()
            dog.card.setupUi(dog.card)
            dog.card.name.setText(dog.name)
            dog.card.id.setText(f"{dog.dogID}")
            dog.card.breed.setText(dog.breed)
            dog.card.owner.setText(dog.owner)
            dog.card.color.setText(dog.color)
            dog.card.dob.setText(dog.dob)
            dog.card.Photo.setPixmap(QPixmap(u"gui/resources/dogs/"+dog.photo))

    def fetchMembers(self):
        self.members.clear()
        info = self.data.query(select=[], fromTable="Members")
        for memberInfo in info:
            member = Member()
            member.memberID, member.name, member.city, member.email, member.phone, member.memberDate, member.photo = memberInfo

            self.members[member.name] = member

            member.card = MemberCard()
            member.card.setupUi(member.card)
            member.card.name.setText(member.name)
            member.card.id.setText(f"{member.memberID}")
            member.card.Address.setText(member.city)
            member.card.Email.setText(member.email)
            member.card.Phone.setText(member.phone)
            member.card.MemberDate.setText(member.memberDate)
            member.card.Photo.setPixmap(QPixmap(u"gui/resources/people/"+member.photo))

            mumDogs = self.data.count(count="*", fromTable="Dogs", where=f'Owner_id = {member.memberID}')[0][0]
            member.card.Phone_3.setText(f"{mumDogs}")


    def populateTree(self):
        self.ui.treeWidget.clear()
        if self.displayedMember != None:
            self.displayedMember.card.hide()
            self.displayedMember = None

        if self.displayedDog != None:
            self.displayedDog.card.hide()
            self.displayedDog = None
        
        for member in self.members.values():
            tree = QTreeWidgetItem(self.ui.treeWidget)
            tree.setText(0, member.name)
            tree.setText(1, member.name)

            self.ui.memberCard.addWidget(member.card)
            member.card.hide()

            for dog in [dog for dog in self.dogs.values() if dog.owner == member.name]:
                child = QTreeWidgetItem(tree)
                child.setText(0, dog.name)

                self.ui.dogCard.addWidget(dog.card)
                dog.card.hide()

    def showMembershipCard(self, name):
        self.displayedMember
        if name in self.members.keys():
            member = self.members[name]
            #if self.displayedDog != None and self.displayedDog.owner != member.name:
            #    self.displayedDog.card.hide()
            #    self.displayedDog = None
            if self.displayedMember != None:
                self.displayedMember.card.hide()
                
            member.card.show()
            self.displayedMember = member

            member.card.Delete.clicked.connect(lambda: self.deleteMember(member))
            member.card.Edit_2.clicked.connect(lambda: self.registerDog(member))

            

        elif name in self.dogs.keys():
            dog = self.dogs[name]
            if self.displayedMember != None and self.displayedMember.name != dog.owner:
                self.displayedMember.card.hide()
                self.members[dog.owner].card.show()
                self.displayedMember = self.members[dog.owner]

            elif self.displayedMember == None:
                self.members[dog.owner].card.show()
                self.displayedMember = self.members[dog.owner]               

            if self.displayedDog != None:
                self.displayedDog.card.hide()
            dog.card.show()
            self.displayedDog = dog

        
            dog.card.Delete.clicked.connect(lambda: self.deleteDog(dog))
            dog.card.Transfer.clicked.connect(lambda: self.transferDog(dog, self.displayedMember))

        

    def deleteMember(self, member):
        ID = member.memberID
        self.data.remove(fromTable='Dogs', where=f'Owner_id = {ID}')
        self.data.remove(fromTable='Members', where=f'Member_id = {ID}')

        self.fetchDogs()
        self.fetchMembers()
        self.populateTree()

    def deleteDog(self, dog):
        ID = dog.dogID
        self.data.remove(fromTable='Dogs', where=f'Dog_id = {ID}')

        self.fetchDogs()
        self.fetchMembers()
        self.populateTree()

        self.members[dog.owner].card.show()
        self.displayedMember = self.members[dog.owner]

    def transferDog(self, dog, member):
        ID = dog.dogID
        self.data.edit(update="Dogs", where=f"Dog_id = {ID}", set=[("Owner_id", f"{member.memberID}")])

        self.fetchDogs()
        self.fetchMembers()
        self.populateTree()

        self.dogs[dog.name].card.show()
        member.card.show()

        self.displayedDog = dog
        self.displayedMember = member

    def registerDog(self, member):

        dogID = list(self.dogs.values())[-1].dogID + 1
        name = "Rufus"
        breed = "Doberman"
        color = 'black'
        dob = '2022-11-11'
        BreedID = self.data.query(fromTable="Breeds", select=["Breed_id"], where=f"name = '{breed}'")
        RegisteredTo = member.memberID
        photo = "nophoto.png"


        self.data.add(into="Dogs", values=[f"{dogID}", f'"{name}"', f"{BreedID[0][0]}", f"{RegisteredTo}", f'"{color}"', f'"{dob}"', f'"{photo}"'])

        self.fetchDogs()
        self.fetchMembers()
        self.populateTree()

        self.dogs[name].card.show()
        member.card.show()

        self.displayedDog = self.dogs[name]
        self.displayedMember = member

stuff = interface()