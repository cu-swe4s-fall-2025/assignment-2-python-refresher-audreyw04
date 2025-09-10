def get_column(file_name, query_column, query_value, result_column):
    
    with open(file_name) as f:
        for i,_line in zip(range(3), f):
            print(i, _line.rstrip())

    result_array = []
    read_file = open(file_name, 'r')
    next(read_file, None)
    for line in read_file:
        columns = line.strip('\n').split(',')
        if columns[query_column-1] == query_value:
            result_array.append(columns[result_column])
    read_file.close()
    return result_array
