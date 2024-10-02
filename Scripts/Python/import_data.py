import pyodbc
import pandas as pd

# Connect to SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=BEARFIST;'
                      'Database=Drive_data;'
                      'Trusted_Connection=yes;')

# Function to import a CSV file into the DriveFiles table
def import_csv_to_db(csv_file, drive_id, drive_name, conn):
    # Read the CSV into a DataFrame
    df = pd.read_csv(csv_file)

    # Print the columns for debugging
    print(f"Columns in {csv_file}: {df.columns.tolist()}")

    # Prepare insert query
    query = '''
    INSERT INTO DriveFiles (file_name, file_path, file_size, last_modified, drive_id, drive_name)
    VALUES (?, ?, ?, ?, ?, ?)
    '''
    
    # Execute the query for each row in the DataFrame
    cursor = conn.cursor()
    for index, row in df.iterrows():
        cursor.execute(query, 
                       row['File Name'],         # Updated column name
                       row['File Path'],         # Updated column name
                       row['File Size (MB)'],    # Updated column name
                       row['Date Modified'],      # Updated column name
                       drive_id, 
                       drive_name)
    
    conn.commit()

# List of CSV files with their corresponding drive names
files_to_import = [
    ('01 Games Drive.csv', 'Drive1', 'Games Drive'),
    ('02 Heavy E Drive.csv', 'Drive2', 'Heavy E Drive'),
    ('03 Data D Drive.csv', 'Drive3', 'Data D Drive'),
    ('08 Dreamcast.csv', 'Drive4', 'Dreamcast'),
    ('09 New.csv', 'Drive5', 'New Drive'),
    ('10 D.csv', 'Drive6', 'D Drive'),
    ('11 D Drive.csv', 'Drive7', '11 D Drive'),
    ('500 E Drive.csv', 'Drive8', '500 E Drive'),
    ('C Plex Drive.csv', 'Drive9', 'C Plex Drive'),
    ('Easy Store Drive.csv', 'Drive10', 'Easy Store Drive'),
    ('F Drive.csv', 'Drive11', 'F Drive'),
    ('One Touch Drive.csv', 'Drive12', 'One Touch Drive'),
    ('Ultra D Drive.csv', 'Drive13', 'Ultra D Drive'),
]

# Importing each file
for csv_file, drive_id, drive_name in files_to_import:
    import_csv_to_db(f'C:/drive_data/Upload/{csv_file}', drive_id, drive_name, conn)

# Close the connection
conn.close()
