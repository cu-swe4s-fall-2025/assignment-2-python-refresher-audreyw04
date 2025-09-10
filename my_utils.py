def get_column(file_name, query_column, query_value, result_column):
    result_array = []
    read_file = open(file_name, 'r')
    for line in read_file:
        columns = line.strip('\n').split(',')
        if columns[query_column] == query_value:
            result_array = columns[result_column]
            result_array.append(result_array[result_column])
    read_file.close()
    return result_array
