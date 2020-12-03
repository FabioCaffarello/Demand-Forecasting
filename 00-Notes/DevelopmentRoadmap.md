# Notebooks
---

## 01 Baseline

- This Notebook aimed to draw a predictive baseline to calculate the demand forecast in up to 3 months of different items from different stores.
	- As a baseline metric was used a traditional model: SARIMA. This is a strapolation of ARIMA for seasonal analysis.
	
	- Evaluation Metric: SMAPE
		- Symmetric mean absolute percentage error 
		$$SMAPE =\cfrac{1}{n}\sum_{i=1}^{n} \cfrac{|F_i - A_i|}{\cfrac{|A_i| + |F_i|}{2}}$$



	
## Functions
---

Modules arim
evaluation
exploratory_data_analysis


| Modules                   | Functions                       | NoteBooks   |
| :-----------------------: | :-----------------------------: | :---------: |
| arima                     | adfullerTest ; rollingStatsPlot | 01-Baseline |
| evaluation                | edaPlot                         | 01-Baseline |
| exploratory_data_analysis | smape                           | 01-Baseline |