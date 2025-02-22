import contextlib
import io
import unittest

##Q1
class Vehicle:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
    
    def display(self):
        print(f"Make: {self.make}; Model: {self.model}")

    def __str__(self) -> str:
        return f"{self.make} {self.model}"
    
car = Vehicle("Toyota", "Prado")

##Q2
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")

class Driver(Person):
    def __init__(self, name, license_number):
        super().__init__(name)
        self.licence_number = license_number

    def display(self):
        print(f"Name: {self.name}, Licence number: {self.licence_number}")

##Q3
class Passenger:
    def __init__(self, name, ticket_id):
        self.__name = name ##private attributes
        self.__ticket_id = ticket_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def ticket_id(self):
        return self.__ticket_id

    @ticket_id.setter 
    def ticket_id(self, new_id):
        self.__ticket_id = new_id

##Q4
class Person:
    def __init__(self):
        self.__distance = 10
    
    @property
    def distance(self):
        return self.__distance

    def ride(self):
        return f"Riding for {self.__distance}km"

class Cyclist(Person):
    def __init__(self):
        super().__init__()
        self.__ext_dist = 40

    def ride(self):
        return f"Riding for {self.distance + self.__ext_dist}km"
        
##Q5
from abc import ABC, abstractmethod

class TransportUser(ABC):
    @abstractmethod
    def travel(self):
        pass  # TODO: Enforce implementation in subclasses

class Commuter(TransportUser):
    def travel(self):
        return "Traveling by bus"

##Q7
class TransportCompany:
    def __init__(self):
        self.__vehicles: list[Vehicle] = []

    def add_vehicle(self, vehicle: Vehicle):
        if isinstance(vehicle, Vehicle) and (vehicle not in self.__vehicles):
            self.__vehicles.append(vehicle)
            return True
        return False

    @property
    def fleet(self):
        return self.__vehicles

#Verification
class TestWeek1(unittest.TestCase):
    ### Q1 TESTCASES ###
    def test_model_q1(self):
        test = Vehicle("Toyota", "Prado")
        self.assertEqual(test.make, "Toyota")
    
    def test_make_q1(self):
        test = Vehicle("Toyota", "Prado")
        self.assertEqual(test.model, "Prado")
    
    def test_display_q1(self):
        test = Vehicle("Toyota", "Prado")
        _stout = io.StringIO()
        with contextlib.redirect_stdout(_stout):
            test.display()
            self.assertEqual(_stout.getvalue(), "Make: Toyota; Model: Prado\n")
    
    def test_bonus_q1(self):
        test = Vehicle("Toyota", "Prado")
        self.assertEqual(str(test), "Toyota Prado")
        self.assertNotEqual(repr(test), "Toyota Prado", "repr() not same as str()")
    
    ### Q2 TESTCASES ###
    def test_name_q1(self):
        driver = Driver("Alice", "D12345")
        self.assertEqual(driver.name, "Alice")
    
    def test_lic_num_q1(self):
        driver = Driver("Alice", "D12345")
        self.assertEqual(driver.licence_number, "D12345")
    
    ### Q3 TESTCASES ###
    def test_name_q1(self):
        passenger = Passenger("Bob", "T4567") ##Init name
        self.assertEqual(passenger.name, "Bob") 
    
    def test_set_name_q1(self):
        passenger = Passenger("Bob", "T4567")
        self.assertEqual(passenger.name, "Bob") 
        
        passenger.name = "Charlie" ##setter
        self.assertEqual(passenger.name, "Charlie")
    
    ### Q4 TESTCASES ###
    def test_person_ride_q4(self):
        person = Person()
        self.assertEqual(person.ride(), "Riding for 10km")
    
    def test_cyclist_ride_q4(self):
        cyclist = Cyclist()
        self.assertEqual(cyclist.ride(), "Riding for 50km")
    
    ### Q5 TESTCASES ###
    def test_travel_q5(self):
        commuter = Commuter()
        self.assertEqual(commuter.travel(), "Traveling by bus")

    ### Q7 TESTCASES ###
    def test_add_vehicle_q7(self):
        company = TransportCompany()
        vehicle = Vehicle("Tesla", "Model S")
        
        company.add_vehicle(vehicle)
        self.assertTrue(vehicle in company.fleet)

if __name__ == "__main__":
    unittest.main()
    
    
