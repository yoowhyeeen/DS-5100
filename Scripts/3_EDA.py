import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

# %matplotlib inline
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None
# # read in all data
data = pd.read_csv("FiveYrLungCancer.csv")
FiveYrLungCancer = data
print(FiveYrLungCancer.shape)

cols = FiveYrLungCancer.columns
colours = ['#000099', '#ffff00'] # specify the colours - yellow is missing. blue is not missing.
sns.heatmap(FiveYrLungCancer[cols].isnull(), cmap=sns.color_palette(colours))
plt.title('All Missing Data in Five Years of Lung Cancer Data')
plt.show()

for col in FiveYrLungCancer.columns:
    pct_missing = np.mean(FiveYrLungCancer[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100,3)))

data = FiveYrLungCancer.loc[(~FiveYrLungCancer['CSRVSUM'].isnull())]
lungCancer_Ok_csrvsum = data[(data['CSRVSUM']<3) & (data['CSRVRTRN']<3) & (data['CSRVINSR']<3)]
print(lungCancer_Ok_csrvsum.shape)

cols = lungCancer_Ok_csrvsum.columns # first 30 columns
colours = ['#000099', '#ffff00'] # specify the colours - yellow is missing. blue is not missing.
sns.heatmap(lungCancer_Ok_csrvsum[cols].isnull(), cmap=sns.color_palette(colours))
plt.title('Missing Data Removed for CSRVSUM, CSRVRTRN, CSRVINSR  in Five Years of Lung Cancer Data')
plt.show()
for col in lungCancer_Ok_csrvsum.columns:
    pct_missing = np.mean(lungCancer_Ok_csrvsum[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100,3)))

data = FiveYrLungCancer.loc[(~FiveYrLungCancer['CSRVPAIN'].isnull())]
lungCancer_Ok_csrvpain = data[(data['CSRVPAIN']<3)]
print(lungCancer_Ok_csrvpain.shape)

cols = lungCancer_Ok_csrvpain.columns # first 30 columns
colours = ['#000099', '#ffff00'] # specify the colours - yellow is missing. blue is not missing.
sns.heatmap(lungCancer_Ok_csrvpain[cols].isnull(), cmap=sns.color_palette(colours))
plt.title('Missing Data Removed for CSRVPAIN in Five Years of Lung Cancer Data')
plt.show()
for col in lungCancer_Ok_csrvpain.columns:
    pct_missing = np.mean(lungCancer_Ok_csrvpain[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100,3)))