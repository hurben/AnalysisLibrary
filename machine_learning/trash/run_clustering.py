#---------------------run_classification.py.py  19.05.24
#
#
#objective : run classification from divided data
#
#[1] from file that contains list of train & test dataset.
#[2] perform classification from given method
#
#>>Current imported methods
#  >"tree" = DecisionTreeClassifier	 19.06.01
#  >
#  >
#
#---------------------------------------------------



def test_run():

	test_data = 'iris.txt'
	test_dataframe = FL.FileHandling().file_to_dataframe(test_data,'\t')

	from sklearn.utils import shuffle
	test_dataframe = shuffle(test_dataframe)
	print test_dataframe

	dataframe = test_dataframe[['sepal length (cm)', 'sepal width (cm)']]
	validate_dataframe = dataframe.iloc[130:150,:]
	model_dataframe = dataframe.iloc[0:130,:]

	print validate_dataframe


	kmeans = KMeans(n_clusters=3).fit(dataframe)
	print kmeans
	print kmeans.labels_

	print kmeans.predict(validate_dataframe)


	import matplotlib.pyplot as plt
	import seaborn as sns;
	



def main(input_file, method):

	None


if __name__ == "__main__":
	import sys
	import os
	import numpy as np
	import argparse
	from sklearn.cluster import KMeans

	sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
	import function_library as FL


	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input', dest = 'input_file')
	parser.add_argument('-m', '--method', dest = 'method')
	parser.add_argument('-n', '--number', dest = 'cluster_number')

	args = parser.parse_args()
	input_file = args.input_file
	method = args.method
	cluster_number = args.cluster_number
	#format of input file should be like this..
	#train1<\t>test1<\n>
	#train2<\t>test2<\n>
	#...
	#...
	#train5<\t>test5<\n>

	if cluster_number == None:
		cluster_number = 2
	else:
		cluster_number = int(cluster_number)

	test_run()
	quit()
	main(input_file, method, cluster_number)	
