class parrot:
    species="bird"
    def __init__(self,name,age):
      self.name = name
      self.age = age
cherry=parrot("cherry",10)
tom=parrot("tom",12)
print("Cherry and tom are", cherry.species)
print("{} is {} years old".format(cherry.name,cherry.age))
print("{} is {} years old".format(tom.name,tom.age))
        