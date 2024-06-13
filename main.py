# Imports
# import pyautogui
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

    def getDF(csvFile):
        df = pd.read_csv(csvFile)
        return df
    

    def estOrNew(df, patientName) -> str:
        """
        Parameter 1: CSV file to be read
        Parameter 2: any patient name from the file
        Return: String "Established" or "New Patient"
        """
        established = False
        for index, row in df.iterrows():
            while row['name'] == patientName:
                currentLoc = row['location']
                while row['location'] == currentLoc:
                    if int(row['date'][6:]) <= 3 and row['status'] != "cancelled":
                        established = True
                        break

        if established == True:
            return "Established"
        else:
            return "New Patient"           

# 2) Create a login class to the website https://provider.umr.com/
class OneHealthCareLogin:
    
    def getDriver(webLink):
        # setting up WebDriver to interact with given website in Edge browser
        driver = webdriver.Edge(service=Service(r"C:\Users\LukeFinch\Downloads\edgedriver_win64\msedgedriver.exe"))
        driver.get(webLink)

        return driver
    
    
    def signIn(driver, email, password, phoneNumber, businessName, streetAddress, city, state, zipCode, taxIDNum, taxProvider):
        
        ### Signing in
        driver.find_element(By.XPATH, "//button[contains(text(),'Sign in')]").click()

        # Entering login credentials
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "user_name")))
        driver.find_element(By.ID, "username").send_keys(email)
        driver.find_element(By.ID, "login-pwd").send_keys(password)

        driver.find_element(By.XPATH, "//button[contains(text(),'Continue')]").click()

        ### Entering info
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "form.providerPhoneNumberFirstPart")))
        driver.find_element(By.NAME, "form.providerPhoneNumberFirstPart").send_keys(str(phoneNumber[:3]))
        driver.find_element(By.NAME, "form.providerPhoneNumberSecondPart").send_keys(str(phoneNumber[3:7]))
        driver.find_element(By.NAME, "form.providerPhoneNumberThirdPart").send_keys(str(phoneNumber[7:]))
        driver.find_element(By.NAME, "form.businessName").send_keys(businessName)
        driver.find_element(By.NAME, "form.streetAddress").send_keys(streetAddress)
        driver.find_element(By.NAME, "form.city").send_keys(city)
        driver.find_element(By.NAME, "form.state").send_keys(state)
        driver.find_element(By.NAME, "form.zipCode").send_keys(str(zipCode))
    

        driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()

        # Entering tax info
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.NAME, "taxIdNum")))
        driver.find_element(By.NAME, "taxIdNum").send_keys(str(taxIDNum))
        driver.find_element(By.NAME, "taxIdDesc").send_keys(taxProvider)

        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

        ### Should be finished registering now







# 3) Login into Outlook and open an email based on the subject and the sender
# Provider public home
# new_or_established.csv

class OutlookHandling:

    def logIn():
        pass
    
    def openEmail(subject, sender):
        """
        Parameter 1: subject of email
        Parameter 2: sender of email
        Return: None
        """
        pass



def main():
    df = csvHandling.getDF("new_or_established 1.csv")
    # print(df.dtypes)
    for index, row in df.iterrows():
        print(row['location'])
    
    # item1 = df.iloc[1, 1]
    # item2 = df.iloc[7, 1]
    # print(type(item1))
    # print(type(item2))


if __name__ == "__main__":
    main()