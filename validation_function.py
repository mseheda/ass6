from file_processing import process_file, process_headers


def is_valid(filename: str, key: str, data_for_validation):
    if key not in process_headers(filename):
        print("Invalid key")
        return False
    data_array = []
    for line in process_file(filename):
        if line[key] not in data_array:
            data_array.append((line[key]))
    return (str(data_for_validation) in data_array)

# f = 'data_source.tsv'
# key_for_dict = "NOC"
# data_for_checking = 'GBR'
# print(is_valid(f, key_for_dict, data_for_checking))
