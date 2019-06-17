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



def generateClassificationReport(y_test,y_pred):

	print(classification_report(y_test,y_pred))
	print(confusion_matrix(y_test,y_pred))    
	print('accuracy is ',accuracy_score(y_test,y_pred))


def test_run():

	test_data = 'iris.txt'
	test_dataframe = FL.FileHandling().file_to_dataframe(test_data,'\t')
	x = test_dataframe.iloc[:,:-1].values
	y = test_dataframe.iloc[:,-1].values
	#x = values
	#y = labels

	for i in range(10):
		x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
		#print y_test
		classifier = DecisionTreeClassifier()
		classifier.fit(x_train,y_train)

		y_pred = classifier.predict(x_test)

		generateClassificationReport(y_test,y_pred)


def main(input_file, method):

	input_file = open(input_file,'r')
	input_readlines = input_file.readlines()

	for i in range(len(input_readlines)):

		read = input_readlines[i]
		read = read.replace('\n','')
	
		token = read.split('\t')
		train_data = token[0]
		test_data = token[1]


		train_dataframe = FL.FileHandling().file_to_dataframe(train_data,'\t')
		x_test = train_dataframe.iloc[:,:-1].values
		y_test = train_dataframe.iloc[:,-1].values
		#important note : .values is necessary because we neet to make it as array.
		#not as a dataframe

		test_dataframe = FL.FileHandling().file_to_dataframe(test_data,'\t')
		x_train = test_dataframe.iloc[:,:-1].values
		y_train = test_dataframe.iloc[:,-1].values

		if method == "tree":
			classifier = DecisionTreeClassifier()
			classifier.fit(x_train, y_train)
			y_pred = classifier.predict(x_test)
			generateClassificationReport(y_test,y_pred)



if __name__ == "__main__":
	import sys
	import os
	import numpy as np
	from sklearn.tree import DecisionTreeClassifier
	from sklearn.metrics import accuracy_score
	from sklearn.metrics import classification_report
	from sklearn.metrics import confusion_matrix
	from sklearn.cross_validation import train_test_split
	from sklearn.model_selection import KFold
	import argparse

	sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
	import function_library as FL


	cv = KFold(5, shuffle=True, random_state=0)

	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input', dest = 'input_file')
	parser.add_argument('-m', '--method', dest = 'method')

	args = parser.parse_args()
	input_file = args.input_file
	method = args.method
	#format of input file should be like this..
	#train1<\t>test1<\n>
	#train2<\t>test2<\n>
	#...
	#...
	#train5<\t>test5<\n>

	main(input_file, method)	
