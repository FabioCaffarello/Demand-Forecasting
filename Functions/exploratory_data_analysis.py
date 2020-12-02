import matplotlib.pyplot as plt
import pandas as pd




def edaPlot(dataset, rule):
	'''
	Plot y versus x as lines of the sales of each store
	
	y: Timeseries Values
	X: Time
	
	Paramaters
	----------
	timeseries: Pandas Series to be plotted 
	rule: time period of analysis (available for monthly and weekly analysis)
        - "Monthly"
        - "Weekly"
	
	Returns
	-------
	Plot
	
	'''


	maping = {
				'Monthly': 'M',
				'Weekly': 'W'
				}
	#Resample the timeseries by the rule
	stores = pd.DataFrame(dataset.groupby(['date','store']).sum()['sales']).unstack()
	stores = stores.resample(maping[rule], label='left').sum()
	stores.sort_index(inplace = True)

	#Plot rolling statistics:
	with plt.style.context('seaborn-dark-palette'):
		stores.plot(figsize=(16,9), title=f'{rule} Store Sales', linewidth=2)
		plt.legend(loc='best')
		plt.show()