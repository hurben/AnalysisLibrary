#------------------------------------- 19.05.13
#latex_compare.py
#
#> This script is made with the specific purpose.
#> Find the .tex differences from <original> <commented by someone>
#
#
#----------------------------------------------


def MAIN(file_1_readlines, file_2_readlines):

	#STEP 1 : compare maximum length
	MAX_LENGTH = compare_list_length(file_1_readlines, file_2_readlines)
	print len(file_1_readlines), ":", len(file_2_readlines)

	#STEP 2 : compare
	compare_per_line(file_1_readlines, file_2_readlines, MAX_LENGTH)


def compare_list_length(file_1_list, file_2_list):
	#STEP 1 : compare maximum length
	#We will use the longest length for specific comparision
	if len(file_1_list) >  len(file_2_list):
		MAX_LENGTH = len(file_1_list)
	else : 
		MAX_LENGTH = len(file_2_list)

	return MAX_LENGTH

def compare_per_line(file_1_readlines, file_2_readlines, MAX_LENGTH):
	#STEP 2 : compare each lines.
	sep = ' '


	for i in range(MAX_LENGTH):

		try :
			i_1_list = FL.DataHandling().tokenize_list(file_1_readlines[i], sep)
			i_2_list = FL.DataHandling().tokenize_list(file_2_readlines[i], sep)

			LIST_MAX_LENGTH = compare_list_length(i_1_list, i_2_list)


			if i_1_list != i_2_list:
#------------FUTURE WORK-----------------
#Instead of this stupid diff finding
#I will implement list pattern matching. hope there is a dp for this
#------------ BLOCK ---------------------
			#IF1 : each lines is not identical
				print "DIFF> LINE %s" % (i)
				print '> %s' % file_1_readlines[i]
				print '> %s' % file_2_readlines[i]

				temp_list = []

				for j in range(LIST_MAX_LENGTH):

					try:
						if i_1_list[j] != i_2_list[j]:
						#IF1-1 : each words are not identical
							print '---- Word ID %s || %s  <--> %s' % (j, i_1_list[j], i_2_list[j])
						else:
							None
					except IndexError:
						None
		except IndexError:
			print "Exceeding lines during comparison"


#------------FUTURE WORK-----------------
#------------ BLOCK ---------------------


if __name__ == "__main__":

	import function_library as FL
	import sys

	input_tex_1 = sys.argv[1]
	input_tex_2 = sys.argv[2]

	#tex_1_dataframe = FL.FileHandling().file_to_dataframe(input_tex_1, " ")
	#tex_2_dataframe = FL.FileHandling().file_to_dataframe(input_tex_2, " ")
	
	tex_1_readlines = FL.FileHandling().file_to_readlines(input_tex_1)
	tex_2_readlines = FL.FileHandling().file_to_readlines(input_tex_2)

	MAIN(tex_1_readlines, tex_2_readlines)
