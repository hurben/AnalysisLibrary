#---------------------distribute_dataset.py  19.05.14
#
#
#objective : from given data. (probably various input)
#
#[1] create test dataset, training dataset
#[2] Save each dataset as each file.
#
#
#---------------------------------------------------

def get_iris_dataset():

	from sklearn import datasets
	import pandas as pd

	iris = datasets.load_iris()
	iris_label = iris['target']

	iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
	iris_df['label'] = iris_label
	iris_df.to_csv('iris.txt', sep='\t', index=False)










if __name__ == "__main__":

	import sys
	import os
	import argparse

	sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#	print os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#	print os.path.dirname(os.path.abspath(__file__))

	import function_library as FL
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input', dest = 'input_file')

	args = parser.parse_args()
	input_file = args.input_file
	#input: should be dataframe that can be handled by pandas

	input_data = FL.FileHandling().file_to_dataframe(input_file,'\t')
	print input_data

	


	get_iris_dataset()
