import pandas as pd
from krippendorff import alpha

# A: 2 Annotators, No missing data
data = pd.read_excel('table1.xlsx')

# drop the first column > timestamps (not used)
data_cleaned = data.drop(data.columns[0], axis=1)
data_transposed = data_cleaned.transpose()

data_matrix = [data_transposed[0].tolist(), data_transposed[1].tolist()]

# metric application
alpha_scalar = alpha(reliability_data=data_matrix, level_of_measurement='interval')
print("Agreement A:", alpha_scalar)

# B: 3 Annotators, No missing data
data = pd.read_excel('table2.xlsx')

# drop the first column > timestamps (not used)
data_cleaned = data.drop(data.columns[0], axis=1)
data_transposed = data_cleaned.transpose()

data_matrix = [data_transposed[0].tolist(), data_transposed[1].tolist(), data_transposed[2].tolist()]

# metric application
alpha_scalar = alpha(reliability_data=data_matrix, level_of_measurement='interval')
print("Agreement B:", alpha_scalar)

