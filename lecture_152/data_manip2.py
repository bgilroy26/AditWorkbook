import pandas
 
data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data_2 = pandas.read_csv("http://www.pythonhow.com/data/sampledata_x_2.txt")
data_3 = data.append(data_2)
data_3.to_csv("sampledata3.txt", index=None)
