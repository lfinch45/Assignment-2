# Imports
import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 1) Read the new_or_established.csv file. Pass as parameter one name present in the spreadsheet. 
# If that name has visited the same location within 3 years and their status is not "canceled", 
# return the string "Established". Else, return "New Patient"
class csvHandling:

    def estOrNew(csvFile, patientName):
        """
        Parameter 1: CSV file to be read
        Parameter 2: any patient name from the file
        Return: String "Established" or "New Patient"
        """
        pass



# 3) Login into Outlook and open an email based on the subject and the sender
# Provider public home
# new_or_established.csv

class OutlookHandling:

    def openEmail(subject, sender):
        """
        Parameter 1: subject of email
        Parameter 2: sender of email
        Return: None
        """
        pass



def main():
    pass

if __name__ == "__main__":
    main()