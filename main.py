# Imports
import pyautogui
import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1) Read the new_or_established.csv file. Pass as parameter one name present in the spreadsheet. 
# If that name has visited the same location within 3 years and their status is not "cancelled", 
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
        patientDF = df[df['name'] == patientName]

        established = False
        
        for index, row in patientDF.iterrows(): # Loops through each row
            currentLoc = row['location']
            nextLoc = row['location'][index + 1]

            currentDate = int(row['date'][6:])
            earliestDate = int(row['date'][6:])

            for index, row in patientDF[currentLoc].iterrows(): # Loops through each row with same location
                if currentLoc != nextLoc:
                    earliestDate = int(row['date'][6:])

            if currentDate - earliestDate <= 3 and row['status'] != "cancelled":
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
    
    
    def providerSignIn(driver, email, password, phoneNumber, businessName, streetAddress, city, state, zipCode, taxIDNum, taxProvider):
        
        ### Signing in
        
        # Scrolling down so computer can see full "Sign in" element
        pyautogui.moveTo(1900, 500) # Move mouse to scroll bar
        pyautogui.mouseDown()
        pyautogui.moveTo(1900, 800, duration=0.5)
        pyautogui.mouseUp
        
        # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Sign in')]")))
        # driver.save_screenshot('screenshot_before_timeout.png')
        # driver.save_screenshot('screenshot_after_scroll.png')
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

    def openOutlookBrowser(emailAddress):
        # Opening outlook on a browser
        edge_browser = pyautogui.locateCenterOnScreen(r"C:\Users\LukeFinch\OneDrive - Jorie Healthcare\Pictures\Screenshots\Screenshot 2024-06-17 222915.png", confidence=0.9)
        pyautogui.moveTo(edge_browser)
        pyautogui.click()
        
        pyautogui.hotkey("ctrl", "t")
        pyautogui.sleep(1)
        pyautogui.write("outlook.com")
        pyautogui.hotkey("enter")
        pyautogui.sleep(4)

        # Signing in
        sign_in_button = pyautogui.locateCenterOnScreen(r"C:\Users\LukeFinch\OneDrive - Jorie Healthcare\Pictures\Screenshots\outlook_signin_icon.png", confidence=0.9)
        pyautogui.moveTo(sign_in_button)
        pyautogui.click()

        pyautogui.sleep(2)
        pyautogui.moveTo(pyautogui.locateCenterOnScreen(r"C:\Users\LukeFinch\OneDrive - Jorie Healthcare\Desktop\snippets\outlook_browser_signin_bar.png", confidence=0.9))
        pyautogui.click()
        pyautogui.write(emailAddress)
        pyautogui.hotkey("enter")

    def openEmailBrowser(sender, subject):
        """
        Purpose: Opening an email based on the subject and the sender by searching in the searchbar
        Parameter 1: subject of email
        Parameter 2: sender of email
        Return: None
        """
        pyautogui.sleep(6)
        outlook_searchbar = pyautogui.locateCenterOnScreen(r"C:\Users\LukeFinch\OneDrive - Jorie Healthcare\Desktop\snippets\outlook_browser_searchbar.png", confidence=0.7)
        pyautogui.moveTo(outlook_searchbar)
        pyautogui.click()
        pyautogui.write(sender + " " + subject)
        pyautogui.hotkey("enter")

    
    def openOutlookApp():
        # Opening outlook through the app instead of through a browser
        search_bar = pyautogui.locateCenterOnScreen(r"C:\Users\LukeFinch\OneDrive - Jorie Healthcare\Desktop\snippets\windows_searchbar_icon.png", confidence=0.8)
        pyautogui.moveTo(search_bar)
        pyautogui.click()
        pyautogui.write("outlook")
        pyautogui.hotkey("enter")



    def openEmailApp(sender, subject):
        """
        Purpose: Opening an email based on the subject and the sender by searching in the searchbar
        Parameter 1: subject of email
        Parameter 2: sender of email
        Return: None
        """
        pyautogui.sleep(2)
        outlook_searchbar = pyautogui.locateCenterOnScreen(r"C:\Users\LukeFinch\OneDrive - Jorie Healthcare\Desktop\snippets\outlook_searchbar.png", confidence=0.9)
        pyautogui.moveTo(outlook_searchbar)
        pyautogui.click()
        pyautogui.write(sender + " " + subject)
        pyautogui.hotkey("enter")



def main():
    ### 1
    # df = csvHandling.getDF("new_or_established 1.csv")
    # csvHandling.estOrNew(df, "Ana")

    
    ### 2
    # driver = OneHealthCareLogin.getDriver("https://provider.umr.com/")
    # OneHealthCareLogin.providerSignIn(driver, "lukefinch45@gmail.com", "Basketball23$", 2243016394, "Luke", "2929 Southwestern Blvd", "Dallas", "TX", 75225, 12345, "JohnDoe")
    

    ### 3
    OutlookHandling.openOutlookApp()
    OutlookHandling.openEmailApp("Kelly Long", "Compliance Update : Patient Data Security: Upholding Integrity as a HIPAA Priority.")
    
    # OutlookHandling.openOutlookBrowser("lfinch@joriehc.com")
    # OutlookHandling.openEmailBrowser("Kelly Long", "Compliance Update : Patient Data Security: Upholding Integrity as a HIPAA Priority.")


if __name__ == "__main__":
    main()