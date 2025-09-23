from typing import List

def get_column(file_name, query_column, query_value, *, result_column=1):
    """
    This function reads a CSV file and retrieves values from a specified column.
    It filters rows based on a query value in the query column.
    """

    #initialize empty list to store results
    result_array: List[int] = []
    #open file and read lines with handling errors
    try:
        read_file = open(file_name, 'r')
    except FileNotFoundError:
        exit(f"File '{file_name}' not found.")

    next(read_file, None)
    #iterate through lines and split by comma
    for line in read_file:
        columns = line.strip('\n').split(',')
        #check if the query column matches the query value
        if columns[query_column-1] == query_value:
            #get the value from the result column as a float
            val = float(columns[result_column].strip())
            #convert to int and append to result array
            result_array.append(int(val))

    #if no entries found, print message, otehrwise print number of entries found
    if not result_array:
        print(f"No entries found for '{query_value}' in column {query_column}")
    else: 
        print(f"Found {len(result_array)} entries for '{query_value}'")
    read_file.close()
    return result_array
