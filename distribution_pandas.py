# Finding the distribution of raining days in a month and total rainfall in a month
# $ python distribution_pandas.py > result_year*.txt
# March 1st, 2016
# Walter Lin

import glob
import pandas as pd
import numpy as np

#path to directory
year = '2015'

mypath = '/Users/Walter/TianQiBaoProjects/python/Modelling/data/'+year

all_files = glob.glob(mypath + "/*.txt")

# Construct an empty DataFrame
frame = pd.DataFrame()

# Construct an empty list
list_ = []

for f in all_files:

    df = pd.read_csv(f, header = 0, engine = 'python', sep = '\s*', names = ['station', 'year', 'month', 'day', 'V10004','V10201','V10202','V12001','V12052','V12053','V13004','V13003','V13007', 'rainfall', 'V13241', 'V13242', 'V11002', 'V11042', 'V11212', 'V11041', 'V11043', 'V14032'])
    # Put all the df into list
    list_.append(df)

# Put the list into frame as our new DataFrame
frame = pd.concat(list_)

# Change all string in 'rainfall' column into int
frame.rainfall = frame.rainfall.astype(np.int)

# Change 32700 to 0 in order to sum up the monthly rainfall
frame.ix[frame.rainfall == 32700, 'rainfall'] = 0

#Group by some parameters and output the sum
frame['raindays'] = (frame.rainfall > 0).astype(np.int)

monthly_raindays = frame.groupby(['station', 'year', 'month']).aggregate({"raindays": np.sum, "rainfall": np.sum})

#print all monthly_sums
with pd.option_context('display.max_rows', 999, 'display.max_columns', 3):
	print monthly_raindays

# Output as int: fmt='%i'
np.savetxt( year + '.txt', monthly_raindays, fmt = '%i')