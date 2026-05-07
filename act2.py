class vehicle:
    def __init__(self, name, max_speed, mileage):
     self.name = name 
     self.max_speed = max_speed
     self.mileage = mileage
obj1=vehicle("School Volco",188,12)
print(obj1.name,obj1.max_speed,obj1.mileage)
obj2=vehicle("Audi Q5",248,18)
print(obj2.name,obj2.max_speed,obj2.mileage)
obj3=vehicle("BMW",268,15)
print(obj3.name,obj3.max_speed,obj3.mileage)

