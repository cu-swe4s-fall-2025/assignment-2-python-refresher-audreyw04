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
        if columns[query_column] == query_value:
            #get the value from the result column as a float
            val = float(columns[result_column].strip())
            #convert to int and append to result array
            result_array.append(int(val))

    #if no entries found, print message, otehrwise print number of entries found
    if not result_array:
        print(f"No entries found for '{query_value}' in column {query_column}")
    else: 
        # print number of entries found
        print(f"Found {len(result_array)} entries for '{query_value}'")
        
        
    read_file.close()
    return result_array


def calculate_mean(data: List[int]) -> float:
    """
    This function calculates the mean of a list of integers.
    It returns 0 if the list is empty to avoid division by zero.
    """
    if not data:
        return 0.0
    return sum(data) / len(data)

def calculate_median(data: List[int]) -> float:
    """
    This function calculates the median of a list of integers.
    It returns 0 if the list is empty.
    """
    if not data:
        return 0.0
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return float(sorted_data[mid])
    
def calculate_sd(data: List[int], mean: float) -> float:
    """
    This function calculates the standard deviation of a list of integers.
    It returns 0 if the list is empty to avoid division by zero.
    """
    if not data:
        return 0.0
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance ** 0.5

