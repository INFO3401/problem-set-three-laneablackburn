import pandas as pd

def helloWorld():
	print ("Hello, World")


def loadAndCleanData(filename):
	data = pd.read_csv(filename)
	return(data)
	
