class String:

    def my_string(self):
        # self.__if_el_in_str()
        # self.__str_separator()
        self.__str_to_int()

    def __if_el_in_str(self):
        name = '*506789'
        if '*' in name:
            print('internal')

    def __str_separator(self):
        sStr = '5/29/2015 - 6/12/2015'
        a = sStr.split(sep=' ')
        print(a)

    def __str_to_int(self):
        a = '3,179.48'
        try:
            x = int(a)
        except ValueError:
            var = a.split(',')
            tmp = int(var[0])
            tmp = tmp * 1000
            x = tmp + float(var[1])
        print(int(x))
