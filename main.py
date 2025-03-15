import os
import pandas as pd
import random

# Define here the column names to be merged
# This configuration makes the script easier to port to different contexts
columns_to_merge = ["Title", "Prompt"]

# Define the folder path containing the CSV files
input_folder_path = "./input"

# Define the folder to export
output_folder_path = "./output"

# List to store the DataFrames
dataframes = []

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

# Save the combined DataFrame to a CSV file with appropriate encoding
filename = f"{output_folder_path}/combined_ideas.csv"
combined_df.to_csv(filename, index=False, encoding="utf-8-sig")
print(f"Combined file saved as {filename}")

# Save the combined DataFrame to an Excel file
filename = f"{output_folder_path}/combined_ideas.xlsx"
combined_df.to_excel(filename, index=False, engine="openpyxl")
print(f"Combined file saved as {filename}")
