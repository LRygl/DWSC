from scraperUtils.dataFileUtils import *
from scraperUtils.dateUtils import *
from selenium.webdriver.common.by import By
import csv
import os

def writeDataToCsv(elements,category,league, teams):


    # Define file prefix and suffix
    prefix = "SAZKA"
    suffix = "VSCP-v01"

    # Define header columns in a separate array
    header_columns = ['DateTime', 'Date', 'Time', 'Category', 'League', 'TeamA', 'TeamB']


    # Construct the filename
    csv_file = f"{prefix}-{getCurrentDate()}-{suffix}.csv"
    # Open the CSV file in write mode
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        # Create a CSV writer object
        csv_writer = csv.writer(file)

        # Write header row
        csv_writer.writerow(header_columns)  # Adjust column names

        counter = 0

        # Write data for each element
        for element in elements:
            dateTimeColumn = current_datetime
            dateColumn = getCurrentDate()
            timeColumn = getCurrentTime()
            categoryColumn = category
            leagueColumn = league
            teamAColumn = teams[counter]
            counter = counter + 1
            teamBColumn = teams[counter]
            counter = counter + 1
            #Write data to CSV as a row of values
            csv_writer.writerow([
                dateTimeColumn,
                dateColumn,
                timeColumn,
                categoryColumn,
                leagueColumn,
                teamAColumn,
                teamBColumn,
            ])

    # Get the file path of the current CSV file
    current_export_file_path = os.path.abspath(csv_file)

    # Get the size of the file in bytes
    # Prepare logic to write in the same file for all categories and dates until the file is over the limit
    file_size = getFileSize(current_export_file_path)
    is_over_limit = isFileOverSizeLimit(current_export_file_path,1024)
    print("Path of the current script:", current_export_file_path)
    print("File has current size of:", file_size)
    print("Is file over the limit:", is_over_limit)