from array import array


def get_column(file_name, query_column, query_value, *, result_column=1):

    result_array = array('f')
    read_file = open(file_name, 'r')
    next(read_file, None)
    for line in read_file:
        columns = line.strip('\n').split(',')
        if columns[query_column-1] == query_value:
            result_array.append(float(columns[result_column]))
    read_file.close()
    return result_array
