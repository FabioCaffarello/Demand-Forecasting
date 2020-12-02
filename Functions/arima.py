from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import pandas as pd




def adfullerTest(timeseries, cutoff = 0.01):
	'''
	Return the evidence against the null hypothesis(Ho) for analysis of the stacinonary of the series using the Dickey-Fuller test
	
	
	Paramaters
	----------
	timeseries: Pandas Series in which the hypothesis test is to be performed
	cutoff: Critical Value (Default -> 0.01)
	
	Returns
	-------
	Text (Print) to be interpreted
	'''
	
	
	result=adfuller(timeseries)
	labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations Used']
	for value,label in zip(result,labels):
		print(label+' : '+str(value) )
	if result[1] <= cutoff:
		print("strong evidence against the null hypothesis(Ho), reject the null hypothesis. Data has no unit root and is stationary")
	else:
		print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")





def rollingStatsPlot(timeseries, window = 12):
	'''
	Plot y versus x as lines of the original data and the respective rolling statistics
	
	y: Timeseries Values
	X: Time
	
	Paramaters
	----------
	timeseries: Pandas Series to be plotted 
	window: Window for rolling statistics (Default -> 12)
	
	Returns
	-------
	Plot
	
	'''
	
	#Determing rolling statistics
	rollmean = timeseries.rolling(window).mean()
	rollstd = timeseries.rolling(window).std()
	
	#Plot rolling statistics:
	with plt.style.context('seaborn-dark-palette'):
		fig = plt.figure(figsize=(16, 9))
		orig = plt.plot(timeseries, linewidth=2, label='Original')
		mean = plt.plot(rollmean, linewidth=2, label='Rolling Mean')
		std = plt.plot(rollstd, linewidth=2, label = 'Rolling Std')
		plt.legend(loc='best')
		plt.title('Rolling Mean & Standard Deviation by Time')
		plt.show()
