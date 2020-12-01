from statsmodels.tsa.stattools import adfuller

def adfuller_test(sales):
	'''
	Return the evidence against the null hypothesis(Ho) for analysis of the stacinonary of the series using the p-value
	
	
	Paramaters
	----------
	sales: Pandas Series in which the hypothesis test is to be performed
	
	
	Returns
	-------
	Text (Print)
	'''
	
	
	result=adfuller(sales)
	labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations Used']
	for value,label in zip(result,labels):
		print(label+' : '+str(value) )
	if result[1] <= 0.05:
		print("strong evidence against the null hypothesis(Ho), reject the null hypothesis. Data has no unit root and is stationary")
	else:
		print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")




