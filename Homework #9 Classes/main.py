# Create a class called "Vehicle" and methods that allow you to set the "Make", "Model", "Year,", and "Weight".

# The class should also contain a "NeedsMaintenance" boolean that defaults to False, and and "TripsSinceMaintenance" Integer that defaults to 0.

# Next an inheritance classes from Vehicle called "Cars".

# The Cars class should contain a method called "Drive" that sets the state of a boolean isDriving to True.  It should have another method called "Stop" that sets the value of isDriving to false.

# Switching isDriving from true to false should increment the "TripsSinceMaintenance" counter. And when TripsSinceMaintenance exceeds 100, then the NeedsMaintenance boolean should be set to true.

# Add a "Repair" method to either class that resets the TripsSinceMaintenance to zero, and NeedsMaintenance to false.

# Create 3 different cars, using your Cars class, and drive them all a different number of times. Then print out their values for Make, Model, Year, Weight, NeedsMaintenance, and TripsSinceMaintenance

# Extra Credit:

# Create a Planes class that is also an inheritance class from Vehicle. Add methods to the Planes class for Flying and Landing (similar to Driving and Stopping), but different in one respect: Once the NeedsMaintenance boolean gets set to true, any attempt at flight should be rejected (return false), and an error message should be printed saying that the plane can't fly until it's repaired.

class Vehicle:
    def __init__(self,make,model,year,weight,needs_maintenance = False,trips_since_maintenance = 0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needs_maintenance = needs_maintenance
        self.trips_since_maintenance = trips_since_maintenance

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_weight(self):
        return self.weight

    def get_needs_maintenance(self):
        return self.needs_maintenance

    def get_trips_since_maintenance(self):
        return self.trips_since_maintenance

    def set_make(self,make):
        self.make = make

    def set_model(self,model):
        self.model = model

    def set_year(self,year):
        self.year = year

    def set_weight(self,weight):
        self.weight = weight

    def set_needs_maintenance(self,needs_maintenance):
        self.needs_maintenance = needs_maintenance

    def set_trips_since_maintenance(self,trips_since_maintenance):
        self.trips_since_maintenance = trips_since_maintenance

    def repair(self):
        if self.needs_maintenance:
            self.needs_maintenance = False
            self.trips_since_maintenance = 0
            print("The maintenance of car is complete")
        else:
            print("The car doesn't need maintenance currently")

class Cars(Vehicle):

    def __init__(self, make, model, year, weight, needs_maintenance = False,trips_since_maintenance = 0):
        super().__init__(make, model, year, weight, needs_maintenance, trips_since_maintenance)
        self.is_driving = False

    def __str__(self):
        result = "Make of car "+str(self.make)+"\n"
        result += "Model of car "+str(self.model)+"\n"
        result += "Year "+str(self.year)+"\n"
        result += "Weight "+str(self.weight)+" Kg\n"
        result += "Car needs maintenance "+str(self.needs_maintenance)+"\n"
        result += "Trips since maintenance "+str(self.trips_since_maintenance)+"\n\n"
        return result

    def drive(self):
        if not self.is_driving:
            self.is_driving = True

    def stop(self):
        if self.is_driving:
            self.is_driving = False
            self.trips_since_maintenance += 2
        if self.trips_since_maintenance >= 100:
            self.needs_maintenance = True

class Planes(Vehicle):

    def __init__(self, make, model, year, weight, needs_maintenance = False, trips_since_maintenance = 0):
        super().__init__(make, model, year, weight, needs_maintenance, trips_since_maintenance)
        self.is_flying = False

    def flying(self):
        if self.needs_maintenance:
            print("Sorry the plane can not take flignt as it needs maintenance")
            return False
        if not self.is_flying:
            self.is_flying = True

    def landing(self):
        if self.is_flying:
            self.is_flying = False
            self.trips_since_maintenance += 3
        if self.trips_since_maintenance >= 100:
            self.needs_maintenance = True

car1 = Cars("Maruti","Wagon R",2021,1340)
car2 = Cars("Tata","Nexon XZ Plus",2020,1520,False,46)
car3 = Cars("Renault","Duster",2021,2050,False,68)

print(car1)
print(car2)
print(car3)

for n in range(40):
    car1.drive()
    car2.drive()
    car3.drive()
    car1.stop()
    car2.stop()
    car3.stop()

print(car1)
print(car2)
print(car3)

car1.repair()
car2.repair()
car3.repair()

plane = Planes("Airbus","A380",2021,5050,False,50)
for n in range(20):
    plane.flying()
    plane.landing()