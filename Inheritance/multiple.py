class Parent1:
    def method1(self):
        print("Method from Parent1")
class Parent2:
    def method2(self):
        print("Method from Parent2")
class Child(Parent1, Parent2):
    def child_method(self):
        print("Method in Child")
x = Child()
x.method1()  
x.method2()  
x.child_method()  
