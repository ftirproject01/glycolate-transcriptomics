# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 09:35:28 2024

@author: The_Box
"""
import pandas as pd
import statistics as st
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

file = 'daten/glycolateMS.xlsx'
xl = pd.ExcelFile(file)
dataframe = xl.parse ("Tabelle1")
mM = list(dataframe['mM'])
counts = list(dataframe['counts'])

mean_mM = str(st.mean(dataframe['mM']))
mean_counts = str(round(st.mean(dataframe['counts']),2))

slope, intercept, r_value, p_value, std_err = sc.stats.linregress(data1,data2)
print('Slope: ',slope,'\nIntercept: ',intercept)
p1, p0 = np.polyfit(mM,counts, deg=1)
print(p1,p0)

#plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(mM,counts,s=2)

lst1 = list(range(1,100))
lst2 = [slope*element for element in lst1]
plt.plot(lst1,lst2, color='red')

textstring = "R² : " + str(round((p1),4)) 
ax.text(1,10 ,textstring,style='italic')
plt.show()
