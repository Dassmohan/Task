class A:
    def method_a(self):
        print("Method A from class A")
class B(A):
    def method_b(self):
        print("Method B from class B")
class C(A):
    def method_c(self):
        print("Method C from class C")
class D(B, C):
    def method_d(self):
        print("Method D from class D")
obj_d = D()
obj_d.method_a()  
obj_d.method_b()  
obj_d.method_c()  
obj_d.method_d() 
