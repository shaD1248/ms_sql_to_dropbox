import csv
import pyodbc
import dropbox
from sql import fetch_data_from_sql

# pip install pyodbc dropbox

# Dropbox details
access_token = 'sl.BwrpxG2_3NNqsXb9nHRjvBtu9f5mGMpb9jikzX9nyblvNmo_dxxPN_VUM_A0a7jLsvFAaP3v4RXeq1C9bDaQjY2P4q0RTueMGP76-o7OcTY9aY_MoEo2acJGnWRlC5VgGyol992s57oQ'
dropbox_file_path = '/file.csv'  # Path where the file will be saved in Dropbox

# Temporary file
local_file_path = 'temp_data.csv'

def save_data_to_csv(data, headers):
    with open(local_file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)
    return local_file_path

def upload_file_to_dropbox(local_file_path, dropbox_path):
    dbx = dropbox.Dropbox(access_token)
    with open(local_file_path, "rb") as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)
    print(f"File uploaded to {dropbox_path} successfully.")

def main():
    data, headers = fetch_data_from_sql()
    local_file_path = save_data_to_csv(data, headers)
    upload_file_to_dropbox(local_file_path, dropbox_file_path)

if __name__ == '__main__':
    main()
