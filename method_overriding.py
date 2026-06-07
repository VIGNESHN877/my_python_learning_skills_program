# this is a Method Overriding 


class Father:                          #----------------------
    def __init__(self):                                      #| parent class and method 
        print("Father constructor ! ")                       #|
                                                            #  -----------
    def say_hello(self):
        print("Hello From Father ! ")


class Child(Father):
    print("Child COnstructor ! ")

    def say_hello(self):
        print("Hello From Child ! ")


Child=Child()
Child.say_hello()

Father = Father()
Father.say_hello()