# Oleksandr Budonnyi. Student number is: 122121434 

class Lodger(object):
    '''
    Manages three instance variables:
    -first name - immutable first name of the lodger
    -second name - immutable second name of the lodger
    -dob - immutable date of birth of the lodger
    -flat - is float number with one decimal place (first decimal is level and the second is flat number)
    -income - total income of the person per flat 
    -utilityPayed - list of counting months that the person payed for utility
    '''
    def __init__(self, name, dob, flat, income, utilityPayed):
        
        if type(name) != str:
            raise ValueError("Name must be a string")
        
        if type(dob) != str:
            raise ValueError("DOB must be a string")
        
        if type(flat) != float: 
            raise ValueError("Flat must be a float number where first decimal is level and second is a flat number")

        if type(income) != int:
            raise ValueError("Income must be an integer")
        
        if type(utilityPayed) != list:
            raise ValueError("The utilityPayed must be a list and more than one month")

        self._name = name
        self._dob = dob
        self._flat = flat
        self._income = income
        self._utilityPayed = utilityPayed
        
    def __str__(self):
        utilityPayed = ""
        for month in self._utilityPayed:
            utilityPayed = utilityPayed + "" + month
        return f"Lodger: {self._name}, DOB: {self._dob}, Flat: {self._flat}, Income: {self._income}, Months of paying: {utilityPayed}"
        
    def getName(self):
        return self._name
    def setName(self, name):
        self._name = name 
        
    def getDob(self):
        return self._dob
    def setDOB(self, dob):
        self._dob = dob
    
    def getflat(self):
        return self._flat
    def setflat(self, flat):
        self._flat = flat
    
    def getincome(self):
        return self._income
    def setSalary(self, salary):
        self._salary = salary
        
    def getutilityPayed(self):
        return self._utilityPayed
    def setutilityPayed(self, utilityPayed):
        self._utilityPayed = utilityPayed
        if type(utilityPayed) != list:
            raise ValueError("The utilityPayed must be a list")
    
    name = property(getName, setName)
    dob = property(getDob)
    flat = property(getflat)
    income = property(getincome)


if __name__  == "__main__":
    
    try: 
        sashaBudonnyi = Lodger("Sasha Budonnyi", "March 5, 2004", 2.2, 56000, ["Jan", "Feb", "Mar"])
        print(sashaBudonnyi)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)