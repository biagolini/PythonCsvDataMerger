# Python CSV File Merger

This project is a simple yet robust tool for merging multiple CSV files into a single file. Designed to automate and enhance CSV file handling, the script allows for streamlined data combination, file origin tracking, and the assignment of randomized unique IDs.

## Features
- Combine multiple CSV files from a specified folder into a single CSV and Excel file.
- Automatically tracks the source file for each row by adding a "Source File" column.
- Generates randomized unique IDs for each row to ensure distinct entries.
- Supports `.csv` and `.xlsx` output formats for broad compatibility.

## Getting Started

Follow these steps to get the project up and running:

### Prerequisites
- Python 3.7 or later must be installed on your system.
- Required Python libraries: `pandas`, `openpyxl`.

### Installation

1. **Clone the Repository**  
   Clone the project repository to your local machine:
   ```bash
   git clone <repository-link>
   cd <repository-name>
   ```

2. **Create the Input Folder**  
   Inside the project directory, create a folder named `input_csv_folder`:
   ```bash
   mkdir input_csv_folder
   ```
   Place all your `.csv` files inside this folder.

3. **Set Up a Virtual Environment**  
   Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

4. **Install Dependencies**  
   Install the required libraries using `pip`:
   ```bash
   pip install pandas openpyxl
   ```

### Usage

Run the script with the following command:
```bash
python3 main.py
```

The script will:
1. Read all `.csv` files in the `input_csv_folder` directory.
2. Merge their contents while reorganizing columns into a specified order.
3. Add a "Source File" column indicating the origin of each row.
4. Generate randomized unique IDs for each row.
5. Save the combined data as:
   - `combined_ideas.csv`
   - `combined_ideas.xlsx`

### Notes
- To customize the order of columns, modify the `columns_to_merge` list in the script.
- The random IDs are generated to ensure uniqueness and are randomized in order.

### Example

1. Place `.csv` files in the `input_csv_folder` directory:
   ```
   input_csv_folder/
   ├── data1.csv
   ├── data2.csv
   └── data3.csv
   ```

2. Run the script:
   ```bash
   python3 main.py
   ```

3. The output will be saved as:
   ```
   combined_ideas.csv
   combined_ideas.xlsx
   ```

## Contributing

Feel free to submit issues, create pull requests, or fork the repository to help improve the project.

## License and Disclaimer

This project is open-source and available under the MIT License. You are free to copy, modify, and use the project as you wish. However, any responsibility for the use of the code is solely yours. Please use it at your own risk and discretion.

---

Happy coding! 🚀

