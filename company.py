from owner import Owner
class Company():

    def __init__(self,title="ZUJ"):
        self.title=title
        self.owners=[]
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,new_title):
        self._title=new_title
    def __str__(self):
        return (
            f"=========Company Information==============\n"
            f"Company title: {self.title}\n"
            f"Owners: {[(owner.name, owner.id) for owner in self.owners]}\n"
            f"==========================================\n"
)
    def addOwner(self,id,name):
        self.owner=Owner(id,name)
        self.owners.append(self.owner)
    def getOwners(self):
        return (f"Owners: {[(owner.name, owner.id) for owner in self.owners]}")
