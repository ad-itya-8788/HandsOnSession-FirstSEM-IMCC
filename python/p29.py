class A:
    def show(self):
        print("Class A show method")


class B(A):
    def show(self):
        print("Class B show method")
        super().show()


class C(A):
    def show(self):
        print("Class C show method")
        super().show()


class D(B, C):
    def show(self):
        print("Class D show method")
        super().show()
obj = D()
obj.show()
