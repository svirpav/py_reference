class Variables:

    def __init__(self):
        self.a = 3

    def my_variables(self):
        print(self.a)
        self.a = 10
        print(self.a)
        self.__change_variable()
        print(self.a)

    def __change_variable(self):
        self.a = 25
