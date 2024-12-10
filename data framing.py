

import pandas as pd

# Assuming 'data' is the one-column DataFrame
data = pd.read_csv(r'C:\Users\kk\Desktop\data1.csv')  # or however you load the data
print(len(data))
# Step 1: Convert the data column to a numpy array for reshaping
array_data = data.values

# Step 2: Reshape the array into 34 columns and 19 rows (for each column)
reshaped_data = array_data.reshape(19, 34)  # Rows first, then columns

# Step 3: Convert reshaped array back into a DataFrame
reshaped_df = pd.DataFrame(reshaped_data)

# Step 4: Display or save the reshaped DataFrame
reshaped_df.to_csv('C:/Users/kk/Desktop/reshaped_data.csv', index=False)  # if you want to save it
print(reshaped_df)

