from company import Company
class Department(Company):

    def __init__(self,title="ZUJ",dname="IT",empCount=10):
        super().__init__(title)
        self.dname=dname
        self.empCount=empCount
        self._DeptBudget=0
        self._total_budget=0
        self._EmpBudget=0
    # Getter of Dapartment name as attribute 
    def __str__(self):
        return(
        f"===========Department Information===========\n"
        f"Company:{self.title}\n"
        f"The Department name: {self._dname}\n"
        f"Employees Count: {self._empCount}\n"
        f"Department budget: {self.getDeptBudget(self._dname)}\n"
        f"Employee budget: {self.getEmpBudget(self._EmpBudget)} \n"
        f"Total Budget: {self.getTotalBudget()}\n"
        f"============================================\n")
    @property
    def dname(self):
        return self._dname
    @dname.setter
    def dname(self,entered_dname):
        dname_dict={"IT","HR","Sales"}    
        if entered_dname not in dname_dict:
            raise ValueError("The departments availabe are HR, IT,Sales")
        self._dname=entered_dname
    @property
    def empCount(self):
        return self._empCount
    @empCount.setter
    def empCount(self,new_empCount):
        available_emp_count={5,10,20,40,60}
        if new_empCount not in available_emp_count :
            raise ValueError("Employees count should be 5, 10, 20, 40 or 60")
        if not isinstance(new_empCount,int):
            raise TypeError("Employees count should be integer")
        self._empCount=new_empCount
    def getDeptBudget(self,dname):
        if self._dname=="IT":
            self._DeptBudget=20000
            return  self._DeptBudget
        elif self._dname=="HR":
            self._DeptBudget=10000
            return  self._DeptBudget
        elif self._dname=="Sales":
            self._DeptBudget=30000
            return  self._DeptBudget

    def getEmpBudget(self,empCount):
        if self._empCount==5 or self._empCount==10:
            self._EmpBudget=self._empCount*1000
            return  self._EmpBudget
        elif self._empCount==20 or self._empCount==40:
            self._EmpBudget=self._empCount*800
            return  self._EmpBudget
        elif self._empCount==60:
            self._EmpBudget=self._empCount*700
            return   self._EmpBudget
    
    def getTotalBudget(self):

        self._total_budget= (self._DeptBudget)+(self._EmpBudget)+1500
        return self._total_budget



