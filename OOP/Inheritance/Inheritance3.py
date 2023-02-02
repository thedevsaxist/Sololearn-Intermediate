class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()

"""super().spam() calls the spam method of the superclass"""