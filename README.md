[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# python-refresher

# my_utils.py
Creates a function get_column which handles input file appropriately. It parses the lines of the file searching for the query value in the query column. If found, it stores the value in teh specified results column into and array and continues until all lines are checked. It then prints the array. Handles columns with 0 index. 

# print_fires.py 
Assigns values for each argument in the get_column function in my_utils. Uses a 1 base index for columns which is then adjusted within the my_utils file. 

country='string'
county_column = int (0 base)
fires_column = int  (0 base)
file_name = 'file_path'

Then runs the get_column function and prints the result. 

# run.sh
Handles running print_fires.py using python3. No additional argument needed.

# Execution

$ chmod +x run.sh
$ ./run.sh

OR

$ sh run.sh