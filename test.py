# Each Employee has a salary


class salary():

    def __init__(self,pay,bonus):

        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
        return (12*self.pay)+self.bonus
    


class employee():
    def __init__(self, name,age,pay,bonus):
        self.name=name
        self.age=age

        self.salary_object=salary(pay,bonus)

    def total_salary(self):

        return self.salary_object.annual_salary()
    

employee_sarah=employee("sarah",24,1000,25)

print(employee_sarah.total_salary())