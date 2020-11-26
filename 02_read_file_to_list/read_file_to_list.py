def read_file_to_list(file):
    with open(file) as f:
        lines = []
        for line in f.readlines():
            lines.append(line.strip())
    return [element for element in lines if element]

