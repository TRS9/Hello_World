abap = open("firsttry.txt", "r+")
#print(abap.readlines())
abap2 = []
i = 0
for field in abap.readlines():
    index = field.find("\n")
    comma_field = field[:index] + "," + field[index:]
    abap2.append(comma_field)

abap.close()
abap3 = open("secondtry.txt", "a")
for field1 in abap2:
    abap3.write(field1)
abap3.close()
print(abap2)