class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")
        
# Creating an instance of the Person class
new_person = Person("Reuben Kipkemboi by the way", 30, "male/Boy/")
# Calling the introduce method to display the person's information
new_person.introduce()