# coding: utf-8
import numpy as np
a = np.zeros(3)
a
type(a)
type(a[0])
a = np.zeros(3, dtype = int)
type(a[0])
z = np.zeros(10)
z.shape
#tuple
z.shape = (10,1)
z
z = np.zeros(4)
z.shape = (2,2)
z
z = np.empty(3)
z
z = np.linspace(2,12,20)
z
len(z)
t = np.arange(10, 15, 0.5)
t
#difference between the arange and linspace
t = np.arange(10)
t
#how many ways can we write the arange and linspace commands
z = np.identity(2)
z
#in python a matrix is an array of arrays
A = np.array([[-1, 2, 5],[3, -2, 1],[2, -3, 7]])
A
#setting up an array of arrays can lead to a matrix
A_inv = np.linalg.inv(A)
A_inv
I = A@A_inv
I
round(I)
np.round(I)
#multiplying matrices we use the matrix @ matrix inverse 
A = np.array([[2, -1, 1, 1], [1, 2, -1, -1], [-1, 2, 2, 2], [1, -1, 2, 1]])
A
B = np.array([[6], [3], [14], [8]])
B
x = np.linalg.inv(A)@B
x
np.random.uniform(1, 10, [2,2])
np.random.randint(1, 10, [2,2])
np.random.normal(5, 1 ,[2,2])
np.random.poisson(5, [2,2])
np.random.seed(500)
np.random.normal(5, 1, 6)
#Pandas
import pandas as pd 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', '')
s = pd.Series(np.random.randn(4), name = 'daily returns')
s
#randn() gives you the standard normal deviation
s.index
s * 100
np.abs(s)
s.describe()
# the mean, mediam and mode should be equal to each othe to be normally distribited
s.index = ['UNIL', 'SCB', 'MTN','ABSA']
s
s['ABSA'] = 0
s
'SCB' in s
import os
os.chdir('C://DataSc')
get_ipython().run_line_magic('ls', '')
df = pd.read_csv('test_pwt.csv')
type(df)
df
df.head(3)
df.tail(3)
df.sample(3)
df.columns
df_subset = df[['country', 'POP', 'tcgdp']]
df_subset
df = df_subset.set_index('country')
df
df.columns = 'population', 'total GDP'
df
df['population'] = df['population'] * 1e3
df['GDP percap'] = df['total GDP'] * 1e6 / df['population']
get_ipython().system('pip install yfinance')
tickers = ['GooG', 'FB','MSFT', 'AAPL']
import yfinance as yf
df = yf.download(tickers, start ='2021-01-01', end = '2026-10-16')['Close']
df.head()
import os 
os.chdir('C://DataSc')
