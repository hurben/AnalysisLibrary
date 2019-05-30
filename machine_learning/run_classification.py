#---------------------run_classification.py.py  19.05.24
#
#
#objective : run classification from divided data
#
#
#
#---------------------------------------------------



def generateClassificationReport(y_test,y_pred):

	print(classification_report(y_test,y_pred))
	print(confusion_matrix(y_test,y_pred))    
	print('accuracy is ',accuracy_score(y_test,y_pred))



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


	sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
	import function_library as FL

	cv = KFold(5, shuffle=True, random_state=0)
	print cv

	##TEST--
	test_data = 'iris.txt'
	test_dataframe = FL.FileHandling().file_to_dataframe(test_data,'\t')
	x = test_dataframe.iloc[:,:-1].values
	y = test_dataframe.iloc[:,-1].values
	#x = values
	#y = labels

	for i in range(10):
		x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
		print y_test
		classifier = DecisionTreeClassifier()
		classifier.fit(x_train,y_train)
		y_pred = classifier.predict(x_test)
	#	generateClassificationReport(y_test,y_pred)


