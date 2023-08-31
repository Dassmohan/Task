class person:
    def __init__(self,name,department):
        self.name=name;
        self.department=department;
    def message(self):
        print("Hi everyone")
    def details(self):
        print("My name is {}".format(self.name))
        print("I am {} department".format(self.department))
class student(person):
    def __init__(self,name,department):
        self.name=name;
        self.department=department;
x=student("Mohandass","CSE")
x.message()
x.details()