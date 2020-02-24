import pandas 
import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.datasets import make_blobs
# from scipy.stats import norm
# from numpy import mean
# from numpy import std

def helloWorld():
	print ("Hello, World")


def loadAndCleanData(filename):
	data = pd.read_csv(filename)
	newData = data.fillna("0")
	print(newData)
	return(newData)

def computePDF(feature,DataFrame):
	s = DataFrame[feature].plot.kde()
	plt.show()

def viewDistribution(feature, DataFrame):
	DataFrame.hist(column= feature, log=True)
	plt.show()

def computeProbability(feature,bin,DataFrame):
	# count the number of data points in the bin 
	count = 0.0 
	for i,datapoint in DataFrame.iterrows():
		#See if the data is in the right bin 
		if datapoint[feature]>=bin[0] and datapoint[feature]<bin[1]:
			count += 1 
	# count the total number of data points 
	totalData = len(data)
	# divide the number of people in the bin by the total number of people

	probabiliy = count/totalData
	# return the results 
	return probabiliy

def computeDefaultRisk(column, feature, bin, DataFrame):
	count = 0.0 
	count2 = 0.0
	for i,datapoint in DataFrame.iterrows():
		if datapoint[feature]>=bin[0] and datapoint[feature]<bin[1]:
			count += 1 
			if datapoint[column]==1:
				count2+=1
	totalData = len(DataFrame)
	probability = count/totalData
	probability2 = count2/totalData
	print(probability2/probability)
	return probability2/probability


# def predictDefaultRisk()



	
