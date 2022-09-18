import os
import glob
from datetime import *
import pandas as pd

todayDate = str(date.today())

search_term = input('Enter a search time to use when looking for files to merge\n')

# fetch list of file names matching the parameters we set
all_filenames = [i for i in glob.glob(f'*{search_term}*.csv')]

if len(all_filenames) > 0:
    print(f"{len(all_filenames)} files found, merging...")
    # combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

    # export to csv
    combined_csv.to_csv( f"{search_term}_{todayDate}.csv", index=False, encoding='utf-8')
    
    input(f"{len(all_filenames)} files merged \n ...")
else:
    input("no files found for that search term \n ...")