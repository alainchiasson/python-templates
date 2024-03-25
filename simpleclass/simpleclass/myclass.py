
class MyClass():

    def myfunc(self):
        print(f"This is my function in  a class")

class VarDemo():

    class_count = 0

    def __init__(self):
        self.inst_count = 0

    def inc(self):
        self.inst_count += 1

        VarDemo.class_count += 1

    def dump(self):
        print(f"class value is {VarDemo.class_count}, instance value is {self.inst_count}")