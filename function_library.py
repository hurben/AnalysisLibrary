#------------------------------------------------- 19.05.12
#
#Objective : Practicing PEP and libraries that I am not good.
#
#
#------------------------------------------------------------


class FileHandling:

	def file_to_dataframe(self, input_text, option):
	#Input : Dataframe
	#Initial purpose : Machine learning ready data.
		import pandas
		input_data = pandas.read_csv(input_text, sep=option)
		
		return input_data

	def file_to_readlines(self, input_data):
	#> General Usage
	#Load files that is not formed as a dataframe

		open_file = open(input_data,'r')
		readlines_file = open_file.readlines()

		return readlines_file

class DataHandling:
	
	def tokenize_list(self, input_list, option):
		
		input_list.replace('\n','') #
		input_list.replace('\r','') #Replacing dirty formats that could caused by various type of inputs..
		tokenized_list = input_list.split(option)
		
		
		return tokenized_list

		


if __name__ == "__main__":

	import sys
	import argparse

	parser = argparse.ArgumentParser()

	parser.add_arguement("-i", "--input", dest="input_file")
	parser.add_arguement("-s", "--sep", dest="sep")

	args = parser.parse_args()
	input_file = args.input_file
	input_sep = args.sep
	

	simple_text_input = './test_data/simple_test.txt'

	FileHandling().read_file(input_file, sep_type) 

else:
	print "Loading <function_library.py>"

