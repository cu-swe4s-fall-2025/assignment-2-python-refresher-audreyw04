#!/bin/bash


# Successful run of the script with no errors
echo "Example of successful run:"
python3 print_fires.py \
    --file_name Agrofood_co2_emission.csv \
    --country_column 1 \
    --country "Algeria" \
    --fires_column 5 

# Example of error handling when the file does not exist
echo -e "\nExample of error handling when the file does not exist:"
python3 print_fires.py \
    --file_name NonExistentFile.csv \
    --country_column 0 \
    --country "Algeria" \
    --fires_column 4    

# Example of error handling when the specified country is not found
echo -e "\nExample of error handling when the specified country is not found:"
python3 print_fires.py \
    --file_name Agrofood_co2_emission.csv \
    --country_column 0 \
    --country "NonExistentCountry" \
    --fires_column 4 