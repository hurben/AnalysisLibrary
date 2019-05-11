###################### 19.05.12
#
#Objective : Practicing PEP and libraries that I am not good.
#
#
#


class FileHandling:

    def read_file(self, input_text, option):

        if option == "dataframe":
            import pandas

            print "[Loading pandas]"
            input_data = pandas.read_csv(input_text, sep=" ", header=None)
            print "Loaded Dataframe : "
            print input_data
            print "Loading row 2 : "
            print input_data[1:2]
            print "Loading col 3 : "
            print input_data[2]
















if __name__ == "__main__":

    simple_text_input = './test_data/simple_test.txt'
    data_type = "dataframe"

    FileHandling().read_file(simple_text_input, data_type)


else:
    print "Loading as FunctionLibrary"
