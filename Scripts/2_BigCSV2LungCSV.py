import pandas as pd

# '_SEX' is not present before 2019; will convert 'SEXVAR' to 'SEX' for 2020, 2019;
#  'SEX1' to 'SEX' for 2018; 'SEX' stays  unchanged for 2017, 2016

# '_RACEPRV' not present before 2020; will use '_RACE' for all years instead

cancer_vars2016 = ['_STATE', 'SEX', '_AGEG5YR', '_EDUCAG', 'MARITAL', 'EMPLOY1', '_INCOMG',
               'DECIDE', 'DIFFWALK', 'DIFFALON', '_RACE', 'MENTHLTH',
               'PHYSHLTH', 'POORHLTH','CSRVSUM', 'CSRVRTRN', 'CSRVINSR',
               'CSRVPAIN']
data = pd.read_csv("brfss2016.csv")
# data = data[(data["CNCRDIFF"] <= 3) & (data["CNCRTYP1"] == 24) & (data['CSRVSUM']<3) & (data['CSRVRTRN']<3) & (data['CSRVINSR']<3) & (data['CSRVPAIN']<3)]
# data = data[(data["CNCRDIFF"] <= 3) & (data["CNCRTYP1"] == 24) & (data['CSRVSUM']<3) & (data['CSRVRTRN']<3) & (data['CSRVINSR']<3)]
data = data[(data["CNCRDIFF"] <= 3) & (data["CNCRTYP1"] == 24)]
lungCancer2016 = data[cancer_vars2016]
lungCancer2016.to_csv('lungCancer2016.csv')
del(data)

cancer_vars2017 = ['_STATE', 'SEX', '_AGEG5YR', '_EDUCAG', 'MARITAL', 'EMPLOY1', '_INCOMG',
               'DECIDE', 'DIFFWALK', 'DIFFALON', '_RACE', 'MENTHLTH',
               'PHYSHLTH', 'POORHLTH','CSRVSUM', 'CSRVRTRN', 'CSRVINSR',
               'CSRVPAIN']
data = pd.read_csv("brfss2017.csv")
# data = data[(data["CNCRDIFF"] <= 3) & (data["CNCRTYP1"] == 24) & (data['CSRVSUM']<3) & (data['CSRVRTRN']<3) & (data['CSRVINSR']<3) & (data['CSRVPAIN']<3)]
# data = data[(data["CNCRDIFF"] <= 3) & (data["CNCRTYP1"] == 24) & (data['CSRVSUM']<3) & (data['CSRVRTRN']<3) & (data['CSRVINSR']<3)]
data = data[(data["CNCRDIFF"] <= 3) & (data["CNCRTYP1"] == 24)]
lungCancer2017 = data[cancer_vars2017]
lungCancer2017.to_csv('lungCancer2017.csv')
del(data)

cancer_vars2018 = ['_STATE', 'SEX1', '_AGEG5YR', '_EDUCAG', 'MARITAL', 'EMPLOY1', '_INCOMG',
               'DECIDE', 'DIFFWALK', 'DIFFALON', '_RACE', 'MENTHLTH',
               'PHYSHLTH', 'POORHLTH','CSRVSUM', 'CSRVRTRN', 'CSRVINSR',
               'CSRVPAIN']
data = pd.read_csv("brfss2018.csv")
# data = data[(data["CNCRDIFF"] <= 3) & (data["CNCRTYP1"] == 24) & (data['CSRVSUM']<3) & (data['CSRVRTRN']<3) & (data['CSRVINSR']<3) & (data['CSRVPAIN']<3)]
# data = data[(data["CNCRDIFF"] <= 3) & (data["CNCRTYP1"] == 24) & (data['CSRVSUM']<3) & (data['CSRVRTRN']<3) & (data['CSRVINSR']<3)]
data = data[(data["CNCRDIFF"] <= 3) & (data["CNCRTYP1"] == 24)]
lungCancer2018 = data[cancer_vars2018]
lungCancer2018.rename(columns={'SEX1': 'SEX'}, inplace=True)
lungCancer2018.to_csv('lungCancer2018.csv')
del(data)


cancer_vars2019 = ['_STATE', 'SEXVAR', '_AGEG5YR', '_EDUCAG', 'MARITAL', 'EMPLOY1', '_INCOMG',
               'DECIDE', 'DIFFWALK', 'DIFFALON', '_RACE', 'MENTHLTH',
               'PHYSHLTH', 'POORHLTH','CSRVSUM', 'CSRVRTRN', 'CSRVINSR',
               'CSRVPAIN']
data = pd.read_csv("brfss2019.csv")
# data = data[(data["CNCRDIFF"] <= 3) & (data["CNCRTYP1"] == 24) & (data['CSRVSUM']<3) & (data['CSRVRTRN']<3) & (data['CSRVINSR']<3) & (data['CSRVPAIN']<3)]
# data = data[(data["CNCRDIFF"] <= 3) & (data["CNCRTYP1"] == 24) & (data['CSRVSUM']<3) & (data['CSRVRTRN']<3) & (data['CSRVINSR']<3)]
data = data[(data["CNCRDIFF"] <= 3) & (data["CNCRTYP1"] == 24)]
lungCancer2019 = data[cancer_vars2019]
lungCancer2019.rename(columns={'SEXVAR': 'SEX'}, inplace=True)
lungCancer2019.to_csv('lungCancer2019.csv')
del(data)

cancer_vars2020 = ['_STATE', 'SEXVAR', '_AGEG5YR', '_EDUCAG', 'MARITAL', 'EMPLOY1', '_INCOMG',
               'DECIDE', 'DIFFWALK', 'DIFFALON', '_RACE', 'MENTHLTH',
               'PHYSHLTH', 'POORHLTH','CSRVSUM', 'CSRVRTRN', 'CSRVINSR',
               'CSRVPAIN']
data = pd.read_csv("brfss2020.csv")
# data = data[(data["CNCRDIFF"] <= 3) & (data["CNCRTYP1"] == 24) & (data['CSRVSUM']<3) & (data['CSRVRTRN']<3) & (data['CSRVINSR']<3) & (data['CSRVPAIN']<3)]
# data = data[(data["CNCRDIFF"] <= 3) & (data["CNCRTYP1"] == 24) & (data['CSRVSUM']<3) & (data['CSRVRTRN']<3) & (data['CSRVINSR']<3)]
data = data[(data["CNCRDIFF"] <= 3) & (data["CNCRTYP1"] == 24)]
lungCancer2020= data[cancer_vars2020]
lungCancer2020.rename(columns={'SEXVAR': 'SEX'}, inplace=True)
lungCancer2020.to_csv('lungCancer2020.csv')
del(data)

FiveYrLungCancer = lungCancer2016.append(lungCancer2017)
del(lungCancer2016)
del(lungCancer2017)
FiveYrLungCancer = FiveYrLungCancer.append(lungCancer2018)
del(lungCancer2018)
FiveYrLungCancer = FiveYrLungCancer.append(lungCancer2019)
del(lungCancer2019)
FiveYrLungCancer = FiveYrLungCancer.append(lungCancer2020)
del(lungCancer2020)

FiveYrLungCancer = FiveYrLungCancer.reset_index()
FiveYrLungCancer.to_csv('FiveYrLungCancer.csv')
