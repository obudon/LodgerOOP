# Oleksandr Budonnyi. Student number is: 122121434 

from lodger import Lodger

class Parkslot(Lodger):
    def __init__(self, name, dob, flat, income, utilityPayed, isparkslot):
        
        if type(isparkslot) != bool:
            raise ValueError("is park slot must be a boolean value")
        
        super().__init__(name, dob, flat, income, utilityPayed)
        self._isparkslot = isparkslot
        
    def __str__(self):
        return f"{ super().__str__()} Is any pakslot: {self._isparkslot}"
    
    def getIsparkslot(self):
        return self._isparkslot
    def setIsparkslot(self, isparkslot):
        if type(isparkslot) != bool:
            raise ValueError("Is park slot must be a boolean value")
        self._isparkslot = isparkslot
        
    isparkslot = property(getIsparkslot, setIsparkslot)
    
if __name__ == "__main__":
    
    try:
        sashabudonnyi = Parkslot("Sasha Budonnyi", "March 5, 2004", 2.2, 56000, ["Jan", "Feb", "Mar"], True)
        print(sashabudonnyi)
        sashabudonnyi.isparkslot = False
        print(sashabudonnyi.isparkslot)
        print(sashabudonnyi)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)