#Just a copy of decorator example in class

def add_method(cls):
    class NewClass(cls):
            def new_method(self):
                  print("This is the new one")
    return NewClass
@add_method
class MyClass:
      def original_method(self):
            print("This is the original")


obj = MyClass()
obj.original_method()
obj.new_method()