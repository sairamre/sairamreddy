# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s-ZeDK14XYWsgAWwVfHjg-nRW81b_hkV

Reg.No:1072
Name:KASAM SAI RAM REDDY
Date:12-10-2022
"""

import pandas as pd
import seaborn as sns

data =pd.read_csv("/content/Enrollments_28092022.csv")
data

data.info()

rows=len(data)
cols=len(data.axes[1])
print("rows:",str(rows))
print("cols:",str(cols))

import matplotlib.pyplot as plt
import statistics as stat

plt.hist(data['DEGREE'])
plt.show

plt.hist(data['SSC'])
plt.show

plt.hist(data['INTERMEDIATE'])
plt.show

data['INTERNSHIP'].value_counts()

interncourses=['Data science','web development','aws']
enrollments=[156,51,90]
plt.pie(enrollments,labels=interncourses)
plt.show()

import numpy as np

print("DEGREE")
print("mean=",np.mean(data['DEGREE']))
print("median=",np.median(data['DEGREE']))
print("mode=",stat.mode(data['DEGREE']))
print("INTERMEDIATE")
print("mean=",np.mean(data['INTERMEDIATE']))
print("median=",np.median(data['INTERMEDIATE']))
print("mode=",stat.mode(data['INTERMEDIATE']))
print("SSC")
print("mean=",np.mean(data['SSC']))
print("median=",np.median(data['SSC']))
print("mode=",stat.mode(data['SSC']))

cv= lambda x: np.std(x, ddof=1)/np.mean(x)*100

print("DEGREE")
print("Range=",max(data['DEGREE'])-min(data['DEGREE']))
print("Co-efficient of variation=",cv(data['DEGREE']))
data['DEGREE'].describe()

print("INTERMEDIATE")
print("Range=",max(data['DEGREE'])-min(data['INTERMEDIATE']))
print("Co-efficient of variation=",cv(data['INTERMEDIATE']))
data['INTERMEDIATE'].describe()

print("SSC")
print("Range=",max(data['DEGREE'])-min(data['SSC']))
print("Co-efficient of variation=",cv(data['SSC']))
data['SSC'].describe()

import scipy.stats as stats

print("Standard scores of Degree")
print(stats.zscore(data['DEGREE']))

print("Standard scores of Intermediate")
print(stats.zscore(data['INTERMEDIATE']))

print("Standard scores of Ssc")
print(stats.zscore(data['SSC']))

def outlier(a):
  q1 = np.quantile(a,0.25)
  q2 = np.quantile(a,0.75)
  m = np.median(a)
  iqr = q2-q1
  u_bound = q2+(1.5*iqr)
  l_bound = q1-(1.5*iqr)
  print(iqr,u_bound,l_bound)
  print("Inter Quartile Range:",iqr)
  outliers = a[(a<= l_bound)|(a>= u_bound)]
  print("outliers in boxplot:\n{}".format(outliers))

outlier(data['DEGREE'])

outlier(data['INTERMEDIATE'])

outlier(data['SSC'])

plt.boxplot(data['DEGREE'])
plt.show

plt.boxplot(data['INTERMEDIATE'])
plt.show

plt.boxplot(data['SSC'])
plt.show

def func(c):
  quantile = np.quantile(c, 0.9)
  Data=c[c==quantile]
  print("Students with 90% percentile:",Data.count())

func(data['DEGREE'])

func(data['INTERMEDIATE'])

func(data['SSC'])