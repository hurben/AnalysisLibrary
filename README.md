General practice
================

General convenience for my own.
-------------------------------



## latex_compare.py

> Created during my thesis writting.
| Comparing micro revised texs (comments, grammer correction.. etc)
| FLAWS : If someone add newline, it will be messed up.


## machine_learning/distribute_dataset.py

> Handling input_data (Dataframe)
|
|1. Divide Test & Training dataset.
|
|	-i [input file] (pandas dataframe foramt)
|	row = sample
|	column = feature
|	final column = label
|
|	-s [split_rate}
|	split samples by percentage
|	ex) 10 = 10% will divid samples 10% per label (this will handle unbalanced label)
|
|	-n [number_of_sets]
|	for K-fold test
|	N will be defined from number of random sets
|
|[2] write test dataset & training dataset each files.


## machine_learning/run_classification.py.py 



>objective : run classification from divided data

1. from file that contains list of train & test dataset.
2. perform classification from given method

>Current imported methods
1. "tree" = DecisionTreeClassifier  19.06.01
  
 





