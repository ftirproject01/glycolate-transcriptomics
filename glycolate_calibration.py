# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 09:35:28 2024

@author: The_Box
"""
import pandas as pd
import statistics as st
import math as m
import matplotlib.pyplot as plt
import numpy as np

file = 'daten/glycolateMS.xlsx'
xl = pd.ExcelFile(file)
dataframe = xl.parse ("Tabelle1")

#dataframe.plot.scatter(x = 'SquareFeet', y = 'Price')

mean_mM = str(st.median(dataframe['mM']))
mean_counts = str(round(st.median(dataframe['counts']),2))

# Regressionsanalyse

def std(data): # data type: Liste
    mean = sum(data)/len(data)
    
    summanden = []
    for element in data:
        summand = (element - mean)**2
        summanden.append(summand)

    summe = sum(summanden)
    std = m.sqrt(summe / (len(data)))
    return std

def kovarianz(data1,data2):
    mean1 = sum(data1)/len(data1)
    mean2 = sum(data2)/len(data2)
    
    summanden = []
    
    for i in range(0,len(data1)):
        summand = (data1[i]-mean1)*(data2[i]-mean2)
        summanden.append(summand)
        
    kovarianz = sum(summanden)/(len(data1))
    print("kovarianz",kovarianz)
    kovarianz2 = np.cov(data1,data2)[0][1]
    print("kovarianz2",kovarianz2)
    
    return kovarianz

def korrelation(data1,data2):
    cov = kovarianz(data1,data2)
    std1 = std(data1)
    std2 = std(data2)
    korrelation = cov/(std1*std2)
    print(data1)
    korrelation2 = np.corrcoef(data1,data2)
    print("korrelation",korrelation)
    print("np.korrelation",korrelation2)
    
    return korrelation
   

def steigung(data1,data2,kor):
    std1 = std(data1)
    std2 = std(data2)
    steigung = kor*std2/std1
    
    from scipy import stats

    slope, intercept, r_value, p_value, std_err = stats.linregress(data1,data2)

    print('Slope: ',slope,'\nIntercept: ',intercept)
    
    return steigung

mM = list(dataframe['mM'])
counts = list(dataframe['counts'])

korrelation = korrelation(mM,counts)
steigung = steigung(mM,counts,korrelation)
print("steigung",steigung)

#plot

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(mM,counts,s=2)

lst1 = list(range(1,100))
lst2 = [steigung*element for element in lst1]

plt.plot(lst1,lst2, color='red')

textstring = "R² : " + str(round((korrelation),4)) 

ax.text(1,10 ,textstring,style='italic')


plt.show()


# linear regression einfacher

p1, p0 = np.polyfit(mM,counts, deg=1)

