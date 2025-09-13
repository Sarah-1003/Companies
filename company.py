class Owner():


    def __init__(self,id=201902069,name="Sarah Mahmoud Salah"):
        # Iniliazing the instances attributes using both default constructor
        # and parameterized constructor
        self.id=id
        self.name=name
    def __str__(self):
        return f"The owner name is {self.name} with id {self.id}"
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id):
        self._id=id


owner1=Owner()
print(owner1)
print(owner1.id)

owner=Owner(id=201802365, name='Kangjunii')

print(owner)
print(owner.id)
owner.name="kang-jun"
print(owner)
