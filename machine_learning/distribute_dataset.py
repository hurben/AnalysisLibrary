#---------------------distribute_dataset.py  19.05.14
#
#
#objective : from given data. (probably various input)
#
#[1] create test dataset, training dataset as files
#[2] Save each dataset as each file.
#
#Consideration : Can be replaced by [sklearn.cross_validation][train_test_split] library
#However, this script is more like a fine-tune
#modfiable for balanced label retrieval
#---------------------------------------------------
from __future__ import division

def get_iris_dataset():
#get and save

	from sklearn import datasets
	import pandas as pd

	iris = datasets.load_iris()
	iris_label = iris['target']

	iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
	iris_df['label'] = iris_label
	iris_df.to_csv('iris.txt', sep='\t', index=False)


def split_train_and_test_dataset(data_file, SPLIT_RATE):

	label_index_list = list(set(data_file['label']))
	MAX_COLUMNS = len(data_file.columns) - 1 #making zero-based
	MAX_SAMPLE_LENGTH = len(data_file['label'])

	dataframe_dict = {}
	label_count_dict = {} #zero-based

	for i in range(MAX_SAMPLE_LENGTH):

		i_feature_data_list = []
		i_label = data_file['label'][i]

		try :label_count_dict[i_label] += 1
		except KeyError : label_count_dict[i_label] = 0

		for j in range(MAX_COLUMNS):

			j_feature = data_file.ix[i,j]
			i_feature_data_list.append(j_feature)

		dataframe_dict[(i_label, label_count_dict[i_label])] = i_feature_data_list

##### Random Sampling datas
	test_dataframe_dict = {}
	import random
	print '#> Starting Random Sampling- %s' 

	for i in label_index_list:
		

		i_label = i
		LEN_LABEL_SAMPLES = label_count_dict[i]
		SPLIT_RANGE = (LEN_LABEL_SAMPLES+1) / SPLIT_RATE
		SPLIT_RANGE = int(round(SPLIT_RANGE))
		print ("Label <%s> have <%s> samples."
		"<%s> samples is discarded for test data") % (i_label, LEN_LABEL_SAMPLES, SPLIT_RANGE)

		popup_index_list = random.sample(range(LEN_LABEL_SAMPLES + 1), SPLIT_RANGE)

		for j in popup_index_list:

			test_values = dataframe_dict[(i_label, j)]

			test_dataframe_dict[(i_label,j)] = test_values

		for j in popup_index_list:
			dataframe_dict.pop((i_label, j))
	print '#-------------------------'
#####

	header_list = list(data_file.columns.values)

	dataframe_dict = make_dataframe_with_label_dict(dataframe_dict)
	test_dataframe_dict = make_dataframe_with_label_dict(test_dataframe_dict)

	training_dataframe = organize_dict_to_pandas(dataframe_dict, header_list)
	test_dataframe = organize_dict_to_pandas(test_dataframe_dict, header_list)

	create_data_files('train', training_dataframe)
	create_data_files('test', test_dataframe)


def handle_NAN(dataframe):

#	feature names
#	print dataframe.columns

#	feature names with true/false (nan)
#	print dataframe.isnull().any()

#	feature names onl with true (nan)
#	print dataframe.columns[dataframe.isnull().any()]

#	feature_with_nan = dataframe.columns[dataframe.isnull().any()].tolist()

#	print feature_with_nan[0]
#	mean = dataframe[feature_with_nan[0]].mean(skipna = True)
#	dataframe[feature_with_nan[0]] = dataframe[feature_with_nan[0]].fillna(mean)

	if dataframe.isnull().values.any() == True:
		print "We found there are Nan values in certain features"
		print "How should we handle this? Type specific number"
		print "< 1 > Use feature means for missing values"
		print "< 2 > Exclude that sample"
		option = int(input("Which one? : "))

		if option == 1:
			feature_with_nan = dataframe.columns[dataframe.isnull().any()].tolist()

			for feature_name in feature_with_nan:
				mean = dataframe[feature_name].mean(skipna = True)
				dataframe[feature_name] = dataframe[feature_name].fillna(mean)

		if option == 2:
			None

	return dataframe


def make_dataframe_with_label_dict(dataframe_dict):

	dataframe_with_label_dict = {}

	for key in dataframe_dict.keys():

		try : label = key[0]
		except TypeError : label = key
		dataframe_with_label_dict[key] = dataframe_dict[key]
		dataframe_with_label_dict[key].append(label)

	return dataframe_with_label_dict


def organize_dict_to_pandas(dataframe_dict, header_list):

	import pandas as pd

	dataframe = pd.DataFrame.from_dict(dataframe_dict, orient='index')
	dataframe.columns = header_list

	return dataframe


def create_data_files(datatype, dataframe):

	import pandas as pd
	
	index = 1 
	loop_break = 0
	while loop_break == 0:	
		data_file = '%s.set.%s' % (datatype, index)

		if os.path.isfile(data_file) == True:
			index += 1
			data_file = '%s.set.%s' % (datatype, index)
		else:
			loop_break = 1

	dataframe.to_csv(data_file, sep="\t", index=False)

	

if __name__ == "__main__":

	import sys
	import os
	import argparse

	sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

	import function_library as FL
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input', dest = 'input_file')
	parser.add_argument('-s', '--splitrate', dest = 'split_rate')
	parser.add_argument('-n', '--number_of_sets', dest = 'number_of_sets')

	args = parser.parse_args()
	input_file = args.input_file
	SPLIT_RATE  = int(args.split_rate)
	NUMBER_OF_SETS  = args.number_of_sets
	#input: should be dataframe that can be handled by pandas

	#data handling
	data_file = FL.FileHandling().file_to_dataframe(input_file, '\t')
	data_file = handle_NAN(data_file)

	if NUMBER_OF_SETS == None:
		NUMBER_OF_SETS = 1
		split_train_and_test_dataset(input_file, SPLIT_RATE)

	else: 	
		NUMBER_OF_SETS = int(NUMBER_OF_SETS)

		for i in range(NUMBER_OF_SETS):
			split_train_and_test_dataset(data_file, SPLIT_RATE)

	

#	get_iris_dataset()
