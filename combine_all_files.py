# Credit to author below:
# code from https://stackoverflow.com/questions/42756696/read-multiple-csv-files-and-add-filename-as-new-column-in-pandas

import pandas as pd
import glob, os

output_location = "test_location"

files = glob.glob("master_folder/*.csv")
df = pd.concat([pd.read_csv(fp).assign(file_name=os.path.basename(fp)) for fp in files])
df.to_csv(output_location)