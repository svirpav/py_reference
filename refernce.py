from scripts import csvhandler
from scripts import datastruct
from scripts import matplot
from scripts import variable


csvH = csvhandler.CsvHandler()
ds_list = datastruct.MyList()
ds_dict = datastruct.Dictionary()
ds_panda = datastruct.MyPandas()
ds_numpy = datastruct.MyNumpy()
mplot = matplot.Plot()
var_str = variable.String()

# csvH.csvhandler()
# mplot.my_subplot()
# ref.my_variables()

''' Numpy.'''
# ds_numpy.my_numpy()

'''Data Frame.'''
ds_panda.my_pd()

'''Dictionary.'''
# ds_dict.my_dic()

'''List.'''
# ds_list.my_list()

'''Strings.'''
# var_str.my_string()

'''Plots.'''
# mplot.data_plot()
