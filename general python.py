#general python 


Tuple = (a,b) #Immutable (cannot change elements inside) list


#Formatting  

#F-string  

formatted_text = f"text {variable:.2f}" # :2.f to round float to 2dp

#Dot format 

formatted_text = "text {:.2f}".format(variable) #remove :.2f if don't need convert variable to 2dp 

#Alignment 

formatted_text = f"{text:<n}" #</>/^ means left/right/centre respectively, n is length of text 


#math operations

% #modulo; gives remainder

// #floor division; gives quotient


#random module

integer_inclusive_both_ends = random.randint(a,b) 

integer_inclusive_start_exclusive_end = random.randrange(a,b) #similar to range


#List slicing 

List[i:j] #give index i to index (j - 1) [similar to range()] 

List[i:j:k] #give index i to index (j - 1) with step k 


#Array 

array_of_j_integers = [0 for i in range(j)] #change 0 to '' for string

2d_array_with_rows_and_columns = [[ “0” for i in range (columns)] for j in range (rows)]  

item_in_2d_array = array[row][column] #floor (row), unit(column)

#Pretty print 2d array:

for row in array: 

    output = “” 

    for cell in row: 

        output += str(cell) + “ “ 

    print(output) 


#File

#reading

file = open(“full name of file (with file extension)”, “r”) 


file.readline() #ignore heading if needed


data = [] 

 
for line in file: 

    line = line.strip() 

    line = line.split(“,”)

    #if line != “": for blank lines (without data)

    data.append(line) 


file.close() 

#csv file, when "data"

import csv 

file = open(“full name of file”,”r”) 

data = list(csv.reader(file)) 

file.close() 


#writing
entire content of existing file will be erased -> use open(“file name”,”a”) if add onto existing file: 

file = open(“file name.extension”, “w”) #will erase content if file already exist
#file = open("existing file name.extension","a") if add onto existing file

file.write(str(contents) + “\n”)  

file.close() 


#Commands  

line = file.read(n) #reads first n characters of file 

line = file.readline() #reads contents of entire line (reads first line if called file not read yet, etc) 

line.lstrip() #strip (remove white space character) at line’s left side [vice versa for line.rstrip()] 


 

  
