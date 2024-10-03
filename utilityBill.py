# Oleksandr Budonnyi. Student number is: 122121434 

from lodger import Lodger

class Utilitytotal(Lodger):
    def 
    
    
# Get user input
name = input("Enter your name: ")
dob = input("Enter your date of birth: ")
flat = float(input("Enter your flat number (first decimal is level and second is a flat number): "))
income = int(input("Enter your income: "))
water = float(input("Enter your current water reading: "))
electricity = float(input("Enter your current electricity reading: "))
utilityPayed = input("Enter the months you have paid your utilities (separated by commas): ").split(',')
isparkslot = bool(input("Enter number of your parkslot: "))
parkslot = int(input("How many slots do you have: "))

months = len(utilityPayed)  # Calculate the number of months

# Create instances of Water, Electricity and Parkslot
water_lodger = Water(name, dob, flat, income, utilityPayed, water)
electricity_lodger = Electricity(name, dob, flat, income, utilityPayed, electricity)
parkslot_lodger = Parkslot(name, dob, flat, income, utilityPayed, isparkslot)

# Calculate costs
water_cost = water_lodger.calculateWaterCost(water) * months  # Multiply by months
electricity_cost = electricity_lodger.calculateElectricityCost(electricity) * months  # Multiply by months
parkslot_cost = parkslot_lodger.calculateCostParkslot(parkslot)

# Calculate total cost
total_cost = water_cost + electricity_cost + parkslot_cost

# Print costs
if __name__  == "__main__":
    
    try: 
        sashaBudonnyi = Lodger(name, dob, flat, income, utilityPayed )
        print(sashaBudonnyi)
        print(f"The cost for water for {months} months is: {water_cost} euro")
        print(f"The cost for electricity for {months} months is: {electricity_cost} euro")
        print(f"The cost for park slot is: {parkslot_cost} euro")
        print(f"The total utility cost is: {total_cost} euro")
    except ValueError as ex:
        print(ex)
