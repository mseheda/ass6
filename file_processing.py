def process_file(filename):
    data = []
    with open(filename, 'r') as file:
        headings = file.readline().strip().split('\t')
        for line in file:
            data.append(process_line(line, headings))
    return data


def process_line(line, headers):
    data_array = line.strip().split('\t')
    return {headers[i]: data_array[i] if i < len(data_array) else None for i in range(len(headers))}


def process_headers(filename):
    with open(filename, 'r') as file:
        headings = file.readline().strip().split('\t')
    return headings
