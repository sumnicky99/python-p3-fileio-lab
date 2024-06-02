def write_file(file_name, file_content):
    # Convert file_name to a string and concatenate ".txt" extension to it
    file_name = str(file_name) + ".txt"
    # Open the file in write mode ('w') with utf-8 encoding
    with open(file_name, mode='w', encoding='utf-8') as file:
        # Write the provided content to the file
        file.write(file_content)


def append_file(file_name, append_content):
    # Convert file_name to a string and concatenate ".txt" extension to it
    file_name = str(file_name) + ".txt"
    # Open the file in append mode ('a') with utf-8 encoding
    with open(file_name, mode='a', encoding='utf-8') as file:
        # Append the provided content to the file
        file.write(append_content)


def read_file(file_name):
    # Convert file_name to a string and concatenate ".txt" extension to it
    file_name = str(file_name) + ".txt"
    # Open the file in read mode ('r') with utf-8 encoding
    with open(file_name, mode='r', encoding='utf-8') as file:
        # Read the content of the file and return it
        return file.read()
