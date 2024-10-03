# Oleksandr Budonnyi. Student number is: 122121434 

from lodger import Lodger

class Water(Lodger):
    def __init__(self, name, dob, flat, income, utilityPayed, water):
        super().__init__(name, dob, flat, income, utilityPayed)
        self._water = water
        
    def calculateRemainingIncome(self, totalCost):
        return self._income - totalCost

    def calculateWaterCost(self, waterUsage):
        waterPrice = 2
        self._water = waterUsage
        return waterUsage * waterPrice
    
    def __str__(self):
        utilityPayed = ""
        for month in self._utilityPayed:
            utilityPayed = utilityPayed + "" + month
            return utilityPayed
        

class Electricity(Lodger):
    def __init__(self, name, dob, flat, income, utilityPayed, electricity):
        super().__init__(name, dob, flat, income, utilityPayed)
        self._electricity = electricity

    def calculateElectricityCost(self, electricityUsage):
        electricityPrice = 1.7
        self._electricity = electricityUsage
        return electricityUsage * electricityPrice

def main():
    # Get user input
    name = input("Enter your name: ")
    dob = input("Enter your date of birth: ")
    flat = float(input("Enter your flat number (first decimal is level and second is a flat number): "))
    income = int(input("Enter your income: "))
    water = float(input("Enter your current water reading: "))
    electricity = float(input("Enter your current electricity reading: "))
    utilityPayed = input("Enter the months you have paid your utilities (separated by commas): ").split(',')
    months = len(utilityPayed)  # Calculate the number of months

    # Create instances of Water and Electricity
    water_lodger = Water(name, dob, flat, income, utilityPayed, water)
    electricity_lodger = Electricity(name, dob, flat, income, utilityPayed, electricity)

    # Calculate costs
    water_cost = water_lodger.calculateWaterCost(water) * months  # Multiply by months
    electricity_cost = electricity_lodger.calculateElectricityCost(electricity) * months
    
    # Calculate total cost and remaining income
    total_cost = water_cost + electricity_cost
    remaining_income = water_lodger.calculateRemainingIncome(total_cost)
    
    # Print costs
    print(f"The cost for water is: {water_cost} euro")
    print(f"The cost for electricity is: {electricity_cost} euro")
    print(f"The total cost for utilities is: {total_cost} euro")
    print(f"The remaining income after paying for utilities is: {remaining_income} euro")

if __name__  == "__main__":
    
    try: 
        main()
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)
        
        
    
