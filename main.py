import os
import pandas as pd
import random

# Define the file format to save ('xlsx' or 'csv')
save_format = "xlsx"  # Default format

# Define the folder path containing the CSV files
input_folder_path = "./input"

# Define the folder to export
output_folder_path = "./output"

# Get the last folder name from the input path
last_folder_name = os.path.basename(os.path.normpath(input_folder_path))

# List to store the DataFrames
dataframes = []

# Define here the column names to be merged
columns_to_merge = ["Title", "Prompt"]

# Loop to process each CSV file in the folder
for file_name in os.listdir(input_folder_path):
    if file_name.endswith(".csv"):
        file_path = os.path.join(input_folder_path, file_name)
        try:
            # Read the CSV file with appropriate encoding
            df = pd.read_csv(file_path, encoding="utf-8-sig")

            # Reorganize the columns in the specified order, ignoring the original order
            df = df[columns_to_merge]

            # Add the file name as a new column
            df["Source File"] = file_name

            # Add the DataFrame to the list
            dataframes.append(df)
        except Exception as e:
            print(f"Error processing file {file_name}: {e}")

# Combine all DataFrames into a single DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Generate unique IDs in random order
num_rows = len(combined_df)  # Total number of rows in the DataFrame
random_ids = random.sample(range(1, num_rows + 1), num_rows)  # Generate unique and random IDs
combined_df["Random ID"] = random_ids  # Add the column to the DataFrame

# Define output filenames using the last folder name
csv_filename = f"{output_folder_path}/{last_folder_name}.csv"
xlsx_filename = f"{output_folder_path}/{last_folder_name}.xlsx"

# Save based on selected format
if save_format.lower() == "xlsx":
    combined_df.to_excel(xlsx_filename, index=False, engine="openpyxl")
    print(f"Combined file saved as {xlsx_filename}")
elif save_format.lower() == "csv":
    combined_df.to_csv(csv_filename, index=False, encoding="utf-8-sig")
    print(f"Combined file saved as {csv_filename}")
else:
    print("Unknown save format. Defaulting to CSV.")
    combined_df.to_csv(csv_filename, index=False, encoding="utf-8-sig")
    print(f"Combined file saved as {csv_filename}")
