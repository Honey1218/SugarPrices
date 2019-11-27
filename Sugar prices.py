import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('C:/Users/vijay/Downloads/Untitled spreadsheet.xlsx')

X = df[['Year']].values
Y = df['Cost of Sugar'].values

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X,Y)
lr.predict([[2050]])