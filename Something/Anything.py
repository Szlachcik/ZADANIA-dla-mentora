class Car:
   def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color

mustang = Car(make="Ford", model_name="Mustang", color="Yellow", top_speed=250)
print(mustang)
print(mustang.make)
faker = Faker()

class person:
    def __init__(self, first_name, last_name, company, position, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email = email
number_1 = person(first_name="Marlin", last_name="Hayes", company="Keebler", position="Central Brand Manager", email="Maudie.Jacobson44@yahoo.com")
number_2 = person(first_name="Carmel", last_name="Wilkinson", company="Harvey LLC", position="Human Solutions Agent", email="Erwin95@yahoo.com")
number_3 = person()
print(f"last_name: {faker.last_name()}")