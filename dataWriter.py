from scraperUtils.dataFileUtils import *
from scraperUtils.dateUtils import *
from selenium.webdriver.common.by import By
import csv
import os

# Create a new CSV file
def writeDataToCsv(elements,category,league, teams):

    # Define file prefix and suffix
    prefix = "SAZKA"
    suffix = "VSCP-v01"

    # Define header columns in a separate array
    header_columns = ['DateTime', 'Date', 'Time', 'Category', 'League', 'TeamA', 'TeamB',"1","X","2","AboveBelow","AboveVal","BelowVal"]

    # Construct the filename
    csv_file = f"{prefix}-{getCurrentDate()}-{suffix}.csv"
    # Open the CSV file in write mode
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        # Create a CSV writer object
        csv_writer = csv.writer(file)

        # Write header row
        csv_writer.writerow(header_columns)  # Adjust column names


#Method used to append a row of data to the csv file 1

