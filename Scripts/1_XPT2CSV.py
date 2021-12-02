import pandas as pd

data = pd.read_sas("LLCP2016.XPT", format='xport')
data.to_csv("brfss2016.csv")
del(data)

data = pd.read_sas("LLCP2017.XPT", format='xport')
data.to_csv("brfss2017.csv")
del(data)

data = pd.read_sas("LLCP2018.XPT", format='xport')
data.to_csv("brfss2018.csv")
del(data)

data = pd.read_sas("LLCP2019.XPT", format='xport')
data.to_csv("brfss2019.csv")
del(data)

data = pd.read_sas("LLCP2020.XPT", format='xport')
data.to_csv("brfss2020.csv")
del(data)
