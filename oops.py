#1: Create a Class with instance attributes
'''class vehicle():
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
obj=vehicle(240,50)
print(obj.max_speed,obj.mileage)

class vehicle:
    pass
'''
#2: Create a Vehicle class without any variables and methods
'''class vehicle:
    def __init__(self,name,speed,mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage
obj=vehicle("pulsar",120,18)
print(f"name of the vehicle is {obj.name} and speed of the vehicle is {obj.speed}, mileage is {obj.mileage}")'''
# 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
'''class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class bus(vehicle):
    pass
school_bus=bus("school volvo",180,12)
print(f"name of the vehicle is {school_bus.name},speed of the vehicle is{school_bus.max_speed},mileage is {school_bus.mileage}")'''
# 4: Class Inheritance
'''class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers")
class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())'''
#e 5: Define a property that must have the same value for every class instance (object)
'''class vehicle:
    colour="white"
    def __init__(self,name,speed,mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage
class bus(vehicle):
    pass
class car(vehicle):
    pass
school_bus=bus("oxford",180,12)
print(school_bus.colour,school_bus.name,"speed is ",school_bus.speed,"mileage is:",school_bus.mileage)
car = car("thar",240,18)
print(car.colour,car.name,car.speed,car.mileage)'''
#6: Class Inheritance
'''class vehicle:
    def __init__(self,name,speed,capacity):
        self.name=name
        self.speed=speed
        self.capacity=capacity
    def fare(self):
        return self.capacity * 100
class bus(vehicle):
    def fare(self):
        amount=super().fare()
        amount+=amount*10/100
        return amount
school_bus=bus("volvo",120,50)
print("total fare is:",school_bus.fare())'''
#7: Check type of an object
'''class vehicle:
    colour="white"
    def __init__(self,name,speed,mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage
class car(vehicle):
    pass
school_bus=car("volvo",180,50)
print(type(school_bus))'''

# 8: Determine if School_bus is also an instance of the Vehicle class
'''class vehicle:
    def __init__(self,name,speed,mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage
class car(vehicle):
    pass
c=car("thar",240,50)
print(isinstance(c,vehicle))'''
#9: Check object is a subclass of a particular class
'''class animal:
    pass
class dog(animal):
    pass
class puppy(dog):
    pass
class cat:
    pass
print(issubclass(dog, animal))   
print(issubclass(animal, dog))   
print(issubclass(cat, animal))    
print(issubclass(puppy, animal)) '''



