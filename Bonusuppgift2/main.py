# 1
def create_file_from_string(my_filename, my_string):
    # my_filename += my_filename + '.txt'
    fw = open(my_filename, 'w')
    fw.write(my_string)
    fw.close()


# 2
def print_file_on_screen(my_filename):
    # my_filename += my_filename + '.txt'
    fr = open(my_filename, 'r')
    text = fr.read()
    return text
