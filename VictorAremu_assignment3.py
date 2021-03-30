# importing from os
import os

# Assignment 1, Question 1: Files and Operating Systems
# Creating a variable of my location to read from

# os.getcwd is getting my current Working Directory
BASE_DIRECTORY = os.getcwd()

# transactions.csv stored in a variable TRANSACT
TRANSACT = 'transactions.csv'
#  products.csv file stored in a Variable PRODUCT
PRODUCT = 'products.csv'
# the folder in which my file is been stored
DATA_FOLDER = 'data'
# the file to be read
IRIS_FILE = 'iris.csv'
# name of the file to write into
REDUCED = 'reduced.csv'
# Path to where data will be written
write_location = os.path.join(BASE_DIRECTORY, DATA_FOLDER, REDUCED)
# path to where products.csv is stored
product_file = os.path.join(BASE_DIRECTORY, DATA_FOLDER, PRODUCT)
# path to where transaction.csv is stored
transaction_file = os.path.join(BASE_DIRECTORY, DATA_FOLDER, TRANSACT)


# Creating a function to reade the file

def read_data(self, data_file=None):
    data_file = os.path.join(BASE_DIRECTORY, DATA_FOLDER, IRIS_FILE)
    # using the open method which takes to parameters, the directory to file and the action to perforrm on file
    with open(data_file, 'r') as file_object:
        return file_object.read()


data = read_data(IRIS_FILE).split('\n')
# creating a list variable for new file
new_file = []

for line in data:
    # this method removes the last two columns of the file and append it to the list(new_file) i created
    new_file.append(line.split(',')[1:3])

# pop method is performed to remove the unwanted empty string at the end of the file
new_file.pop()
# this line removes the last 50 rows from the buttom
new_file = new_file[:-50]

# Creating a function to Write the edited file into a new file called reduced.csv


def write_data(write_location, data=None):
    data_file = os.path.join(BASE_DIRECTORY, DATA_FOLDER, REDUCED)
    # using the open method which takes to parameters, the directory to file and the action to perforrm on file
    with open(write_location, 'w') as file_object:
        for line in data:
            file_object.write(",".join(line)+"\n")


# Calling the function and passing necessary parameters
write_data(write_location, new_file)


# Assignment 2 Question1 : Classes
# Creating a class Analysis, where all function is going to be

class Analysis():
    def __init__(self, file=None):
        self.file = file

    # type of data function
    def whatType(self, inp):
        """
        Returns the type of data in a given collection of data. 
        Assumes all data in the collection is of the same type
        """
        if inp.isnumeric():
            return type(int(inp))

        # does the input contain a decimal point?
        elif inp.count('.') == 1:
            if inp.split('.')[0].isnumeric() and inp.split('.')[1].isnumeric():
                return type(float(inp))
            else:
                return type(inp)

        else:
            return type(inp)

    # Read file function
    def read_data(self, data_file=None):
        """
        Arguments:
        data_file: path to csv file

        Returns:
        returns a list of lines of strings being the content of the data_file
        """
        if data_file:
            data_file = os.path.join(BASE_DIRECTORY, DATA_FOLDER, data_file)
            with open(data_file, 'r') as file_object:
                return file_object.readlines()
        else:
            data_file = os.path.join(BASE_DIRECTORY, DATA_FOLDER, self.file)
            with open(data_file, 'r') as file_object:
                return file_object.readlines()

     # ************** HELPERS END HERE ********

     # =================== Q1 =================
     # ========================================
    def dimension(self, data):
        """
        Returns information about the dimensions of the data
        Parameters:
            data: [str/list], being data read in from that has been read from a file
        Returns:
             a tuple of the form (n_rows,n_cols) where
            n_rows = the number or rows
            n_cols = the number of columns

        Expected output using products.csv file:
        n_rows = 200
        n_cols = 7
        """
        # condition statement present to check if data in file is coming as list or string

        if(type(data) == list):
            n_rows = len(data)-1  # number of rows
            n_cols = len(data[0].split(","))  # number of columns
        elif(type(data) == str):
            data = data.split("\n")
            data.pop()
            n_rows = len(data)-1
            n_cols = len(data[0].split(","))
        # *** ADD YOUR OWN LINES OF CODE BELOW THIS LINE ***

        return (n_rows, n_cols)

    # =================== Q2 =================
    # ========================================
    def unique(self, data, column):
        """
            Params:
                data: list, raw data
                column: str, name of column to check for uinque values

            Returns:
                a list of ONLY the unique values values in columns
        """
        # sample column names to test
        # 'product_id,product_line,product_class,product_size,list_price

        unique_values = None

        # *** ADD YOUR OWN LINES OF CODE BELOW THIS LINE ***
        # this is to get the headings of the the file
        header = data[0].strip().split(",")
        if(column in header):
            index = header.index(column)

        unique_values = []
        for line in data[1:]:
            result = line.strip().split(",")[index]
            if(result != ""):
                unique_values.append(result)
        # return statement is such that, question asked to return a list but then,
        # set method is been called on uniques_values to return values without repetition.
        return list(set(unique_values))

    # =================== Q3 =================
    # ========================================
    def info(self, data):
        """
        Params: 
            data: str, raw data read from file using read_data()
        Output:
            Prints out to the screen the following info about the data:
            - number of rows
            - number of columns
            - for each column, the columns name and the type of the data stored in that column 
        """
        # HIINT: use the function whatType() to help you get the type of the data in the columns

        # YOUR CODE AFTER THIS LINE
        no_of_rows = str(self.dimension(data)[0])
        no_of_columns = str(self.dimension(data)[1])

        # fortmatting the printout statement
        print("Number of rows: {}".format(no_of_rows))
        print("Number of columns: {}".format(no_of_columns))

        header = data[0].strip().split(",")
        dataVal = data[1].strip().split(",")
        for key, value in zip(header, dataVal):
            print("{} : {}".format(key, self.whatType(value)))


# ====================== LEAVE THESE LINES ALONE ====================
# The lines of code bellow should run smoothly without any problem
analyze = Analysis('products.csv')
data = analyze.read_data()
analyze.dimension(analyze.read_data())
analyze.unique(data, column='product_class')
analyze.info(data)

# Victor.Aremu
