
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf

# /Users/habibdurodola/Documents/stockAnalysis/stockAnalysis/ProcterGambleStock.csv
boeingDataFrame = pd.read_csv('/Users/habibdurodola/Documents/stockAnalysis/stockAnalysis/BoeingStock.csv')
cocacolaDataFrame = pd.read_csv('/Users/habibdurodola/Documents/stockAnalysis/stockAnalysis/CocaColaStock.csv')
geDataFrame = pd.read_csv('/Users/habibdurodola/Documents/stockAnalysis/stockAnalysis/GEStock.csv')
ibmDataFrame = pd.read_csv('/Users/habibdurodola/Documents/stockAnalysis/stockAnalysis/IBMStock.csv')
pgDataFrame = pd.read_csv('/Users/habibdurodola/Documents/stockAnalysis/stockAnalysis/ProcterGambleStock.csv')

# convert date to string
boeingDataFrame['Date'] = pd.to_datetime(boeingDataFrame['Date'], format='%d/%m/%y')


print boeingDataFrame.head()

#Data Visualization
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,5))
sns.pointplot(data=boeingDataFrame, x="Date", y="StockPrice", ax=ax1)
sns.pointplot(data=boeingDataFrame, x="Date" ,y="StockPrice" , ax=ax2)

plt.show()

# sns.countplot(data=dataFrame, x="Pclass", hue="Survived", ax=ax2)


# dataFrame = boeingDataFrame.con

# dataFrame = pd.concat([boeingDataFrame, cocacolaDataFrame , geDataFrame , ibmDataFrame , pgDataFrame])


# print pd.concat([boeingDataFrame, cocacolaDataFrame , geDataFrame , ibmDataFrame , pgDataFrame])










