import numpy as np
import pandas as pd



def smape(yTrue, yPred):
	'''
	error calculation of the prediction using the SMAPE metric 
	
	
	Paramaters
	----------
	yTrue: Timeseries with the actual value
	yPred: Timeseries with the estimated value
	
	Returns
	-------
	SMAPE error
	
	'''
	
	
	denominator = (np.abs(yTrue) + np.abs(yPred)) / 2
	diff = 100 * np.abs(yTrue - yPred) / denominator
	diff[denominator == 0] = 0.0

	return np.nanmean(diff)