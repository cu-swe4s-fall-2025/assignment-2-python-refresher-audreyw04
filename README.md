[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# python-refresher

# my_utils.py
Creates a function get_column which handles input file appropriately. It parses the lines of the file searching for the query value in the query column. If found, it stores the value in the specified results column into and list of integers and continues until all lines are checked. It then prints the list. Handles columns with 0 index. 

Has functions calculate_mean, calculate_median, and calculate_sd which do their specified jobs. They are utilized in the print fires script.

# print_fires.py 
Accepts arguments given from the run.sh file using the parse_args function and assigns them appropriately for the get_column function in my_utils as well as the calculation functions when specified. Uses a 0 base index for columns. 

Example inputs from parse_args: 
    --file_name Agrofood_co2_emission.csv \
    --country_column 1 \
    --country "Algeria" \
    --fires_column 5 \
    --calculate mean

Then runs the get_column function and prints the result. If calculate is specified (mean, median, sd) then the respective function will be run on the data and the output printed.

# run.sh
Handles running print_fires.py using python3. Feeds specified arguments to print_fires.py for three different Example cases. 

Example 1:
python3 print_fires.py \
    --file_name Agrofood_co2_emission.csv \
    --country_column 1 \
    --country "Algeria" \
    --fires_column 5 

Exhibits a successful code run using the above arguments. 

Example 2:
python3 print_fires.py \
    --file_name NonExistentFile.csv \
    --country_column 0 \
    --country "Algeria" \
    --fires_column 4    

Exhibits appropriate error handling when the given file does not exist.

Example 3:
python3 print_fires.py \
    --file_name Agrofood_co2_emission.csv \
    --country_column 0 \
    --country "NonExistentCountry" \
    --fires_column 4 

Exhibits appropriate error handling when the result list is empty because the query value could not be found.

# Execution

$ chmod +x run.sh
$ ./run.sh

OR

$ sh run.sh

# Testing

Testing done using test_my_utils.py in python to test the functionality and accuracy of the calculation functions. 

Testing done using test_print_fires.sh in bash to test the functionality of the print fires file and the calculations when applied to the specified data. 