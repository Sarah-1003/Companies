class Owner():


    def __init__(self,id=202010001,name="owner"):
        # Iniliazing the instances attributes using both default constructor
        # and parameterized constructor
        self.id=id
        self.name=name
    def __str__(self):
        return (f"The owner name is {self.name} with id {self.id}")
    # Defining the setter and getter for ID attribute
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,new_id):
        if new_id <202010001 or new_id > 202139999:
            raise ValueError("The ID value should be between 202010001 and 202139999")
        
        self._id=new_id

    # Definig the setter and getter for name attribute

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name=new_name

