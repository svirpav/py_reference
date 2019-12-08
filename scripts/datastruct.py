import numpy as np
import pandas as pd
import random

'''List.'''


class MyList:

    def my_list(self):
        # print('before call()', b)
        # self.__modify_list(b)
        # print('after call()', b)
        # self.__add_remove()
        # self.__reverse_list()
        # self.__add_list()
        # self.__double_list()
        self.__crt_ow_mul_dim_list()

    def __sort_list(self, data):
        data = sorted(data)
        # print(data)

    def __add_remove(self):
        a = []
        for i in range(10):
            a.append(str(i))
        print(a)
        a.remove('0')
        print(a)
        a.pop()
        print(a)
        a.pop(0)
        print(a)

    def __reverse_list(self):
        b = ['a', 'c', 'g', 'e', 'z', 'k', 'h', 'j']
        print(b)
        b.reverse()
        print(b)

    def __add_list(self):
        a = [1, 3]
        b = [3, 1]
        c = a + b
        print(c)

    def __double_list(self):
        a = [[], []]
        for i in range(25):
            if (i % 2) == 0:
                a[0].append(i)
            else:
                a[1].append(i)
        print(a)

    def __crt_ow_mul_dim_list(self):
        a = 3
        x = []
        for i in range(a):
            x.append([])
        print(x)
        for z, y in enumerate(x):
            print(z, y)


'''Dictionary.'''


class Dictionary:

    def my_dic(self):
        # self.__add_to_dict()
        self.__key_values()

    def __add_to_dict(self):
        a = dict()
        print(a)
        a['a'] = 0
        print(a)
        a['a'] += 20
        print(a)
        a['a'] += 10
        print(a)

    def __key_values(self):
        a = {'key': [2, 6]}
        print(a['key'][0])


'''Pandas.'''


class MyPandas:

    def my_pd(self):
        # self._my_data_frame()
        self.__drop_data()

    def __my_data_frame(self):
        data = [1, 2, 3, 4, 5, 6, 7]
        pd_data = pd.DataFrame(data)
        print(pd_data)

    def __drop_data(self):
        data = {'int': []}
        for i in range(1200):
            data['int'].append(random.randint(1, 35))
        pa_data = pd.DataFrame(data)
        print(pa_data[pa_data['int'] == 10].index)


'''Numpy.'''


class MyNumpy:

    def my_numpy(self):
        # self.__ndarray()
        # self.__create_multi_dim_array()
        self.__numpy_arrange()

    def __ndarray(self):
        a = [1, 2, 3, 4, 5, 6]
        array_1 = np.array(a)
        array_2 = np.array(a, ndmin=2)
        print('Default', array_1)
        print('Min 2 :', array_2)

        # int8, int16, int32, int64 can be replaced by
        # equivalent string 'i1', 'i2','i4', etc.

        sample = np.dtype([('name', 'S20'), ('qty', 'i1'), ('price', 'f4')])
        array_3 = np.array([('MA', 30, 12), ('XY', 12, 34)], dtype=sample)
        print(array_3)

        # Shape
        x = [[3, 4, 7], [2, 8, 9], [1, 5, 7], [3, 4, 7]]
        array_4 = np.array(x)
        print(array_4.shape)
        print(array_4)
        array_4 = array_4.reshape(2, 6)
        print(array_4)

        # Evanley spaced numbers
        x = np.arange(24)
        for i in x:
            print(i)

    def __create_multi_dim_array(self):
        a = np.array([0], ndmin=3)
        print(a)

    def __numpy_arrange(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        x = np.arange(len(labels))
        print(x)
