# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 10:05:17 2023

@author: sadwika sabbella
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a=[i for i in 'abcdefghijklmnop']
data=pd.read_excel(r"C:\Users\sadwika sabbella\Desktop\pyfh\credit_loan.xlsx",names=a)
print(data.columns)
##a=np.arange(1,151)
##data['new']=a

print(data.shape)
#print(data)
print(data.head())

print(data.isna().sum())


data['b'].value_counts()
data['b'].replace(to_replace='?',value= 10.00,inplace=True)
data['n'].replace(to_replace='?',value= 10.00,inplace=True)


s='adefgijlm'
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
for i in s:
    data[i]=le.fit_transform(data[i])

x=np.array(data.iloc[ : , :-1])##[0,1,2,3,5]])
y=data.iloc[ : ,-1].values
print(x.shape,y.shape)


from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3,random_state=1)

print(xtrain.shape,ytrain.shape)
print(xtest.shape,ytest.shape)


#from sklearn.neighbors import KNeighborsClassifier
#model=KNeighborsClassifier(n_neighbors=3)
#model.fit(xtrain,ytrain)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(xtrain,ytrain)

#from sklearn.naive_bayes import GaussianNB
#model=GaussianNB()
#model.fit(xtrain,ytrain)


ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred)*100)