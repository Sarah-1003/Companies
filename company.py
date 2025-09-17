from owner import Owner
class Company():

    def __init__(self,title="ZUJ"):
        self.title=title
        self.owners=[]
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
        for owner in self.owners:
            print(f"Owner name's {owner.name} with id {owner.id}")




company_object=Company(title="Sarah & Kang")
company_object.addOwner(name="Lee Kang",id=202010001)
company_object.addOwner(name="Sarah Lee",id=202010002)

company_object.getOwners()

print(company_object)