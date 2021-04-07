import pandas as pd
import numpy as np


insert_string = "insert into  #temp values "
target_file_location = "target1.csv"
output_file_location = "output.csv"


target_file = pd.read_csv(target_file_location, ",")


output_list = []
i = 0
k = 0
empty_string = ""
size = target_file.shape
total_rows = size[0]
print(total_rows)
print(total_rows % 990)
for index, row in target_file.iterrows():

    if total_rows - k <= (total_rows % 990):
        if total_rows - k == 1:
            empty_string += "('" + str(row[0]) + "')"
        else:
            empty_string += "('" + str(row[0]) + "'),"
    else:
        if i == 990 - 5:

            empty_string += "('" + str(row[0]) + "')"
            total_string = insert_string + empty_string + ""
            output_list.append(total_string)
            empty_string = ""
            i = 0
        else:
            empty_string += "('" + str(row[0]) + "'),"
            i += 1
    k += 1

total_string = insert_string + empty_string + ")"
output_list.append(total_string[:-1])
output_list = output_list


pd = pd.DataFrame(output_list)
pd.to_csv(output_file_location, index=False)
print("complete")



