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
#get and save

	from sklearn import datasets
	import pandas as pd

	iris = datasets.load_iris()
	iris_label = iris['target']

	iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
	iris_df['label'] = iris_label
	iris_df.to_csv('iris.txt', sep='\t', index=False)


def split_train_and_test_dataset(data_file, SPLIT_RATE):

	data_file = FL.FileHandling().file_to_dataframe(data_file, '\t')

	label_index_list = list(set(data_file['label']))
	MAX_COLUMNS = len(data_file.columns) - 1 #making zero-based
	MAX_SAMPLE_LENGTH = len(data_file['label'])

#	dataframe_without_label = data_file.ix[:,0:MAX_COLUMNS]
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

	test_dataframe_dict = {}

	import random
	for i in label_index_list:
		

		i_label = i
		LEN_LABEL_SAMPLES = label_count_dict[i]
		SPLIT_RANGE = (LEN_LABEL_SAMPLES+1) / SPLIT_RATE

		popup_index_list = random.sample(range(LEN_LABEL_SAMPLES + 1), SPLIT_RANGE)
		print i,'/' ,len(popup_index_list)

		for j in popup_index_list:

			test_values = dataframe_dict[(i_label, j)]

			test_dataframe_dict[(i_label,j)] = test_values

		for j in popup_index_list:
			dataframe_dict.pop((i_label, j))


	header_list = list(data_file.columns.values)

	dataframe_dict = make_dataframe_with_label_dict(dataframe_dict)
	test_dataframe_dict = make_dataframe_with_label_dict(test_dataframe_dict)

	organize_dict_to_pandas(dataframe_dict, header_list)
	organize_dict_to_pandas(test_dataframe_dict, header_list)


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

	args = parser.parse_args()
	input_file = args.input_file
	SPLIT_RATE  = int(args.split_rate)
	#input: should be dataframe that can be handled by pandas

#	input_data = FL.FileHandling().file_to_dataframe(input_file,'\t')
	split_train_and_test_dataset(input_file, SPLIT_RATE)

	

#	get_iris_dataset()
