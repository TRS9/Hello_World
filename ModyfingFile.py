file_input = open("firsttry.txt", "r+")
file_input_copy = []
for field in file_input.readlines():
    index = field.find("\n")
    comma_field = field[:index] + "," + field[index:]
    file_input_copy.append(comma_field)
file_input.close()

file_output = open("secondtry.txt", "a")
for field in file_input_copy:
    file_output.write(field)
file_output.close()
