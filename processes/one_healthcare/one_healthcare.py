from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import Locators

kwargs_param = {
    'driver': 'driver_value',
    'email': 'email_value',
    'password': 'password_value',
    'business_name': 'business_value',
    'streetAddress' : 'street_value',
      'city': 'asodjaoids', 
      'state' : 'sttet', 
      'zipCode': 123456, 
      'taxIDNum': 123456, 
      'taxProvider': 'tax_provider'
}

class UserInterface:
    def __init__(self, **kwargs)
        self.driver = kwargs.get('driver')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.business_name = kwargs.get('business_name')
        self.street_address = kwargs.get('streetAddress')
        self.city = kwargs.get('city')
        self.sate = kwargs.get('state')
        self.zip_code = kwargs.get('zipCode')
        self.tax_id = kwargs.get('taxIDNum')
        self.tax_provider



        

class OneHealthCareLogin:
    
    def getDriver(webLink):
        # setting up WebDriver to interact with given website in Edge browser
        driver = webdriver.Edge(service=Service(r"C:\Users\LukeFinch\Downloads\edgedriver_win64\msedgedriver.exe"))
        driver.get(webLink)

        return driver
    
    
    def providerSignIn(driver, email, password, phoneNumber, businessName, streetAddress, city, state, zipCode, taxIDNum, taxProvider):
        
        ### Signing in
        driver.maximize_window()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'https://identity.onehealthcareid.com')]")))
        driver.find_element(By.XPATH, "//a[contains(@href, 'https://identity.onehealthcareid.com')]").click()
        
        # Entering login credentials

        # Getting the following message when taken to the Sign In screen:
        # [6536:23296:0618/102450.071:ERROR:socket_manager.cc(142)] Failed to resolve address for aa.online-metrix.net., errorcode: -105
        # [6536:23296:0618/102450.072:ERROR:socket_manager.cc(142)] Failed to resolve address for aa.online-metrix.net., errorcode: -105
        # [6536:23296:0618/102450.146:ERROR:socket_manager.cc(142)] Failed to resolve address for aa.online-metrix.net., errorcode: -105
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "username")))
        driver.find_element(By.ID, "username").send_keys(email)

        driver.find_element(By.ID, "login-pwd").send_keys(password)

        driver.find_element(By.ID, "btnLogin").click()

        ### Entering info
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, Locators.provider_phone_number)))
        driver.find_element(By.NAME, Locators.provider_phone_number).send_keys(str(phoneNumber[:3]))
        driver.find_element(By.NAME, Locators.provider_second_part).send_keys(str(phoneNumber[3:7]))
        driver.find_element(By.NAME, Locators.provider_third_part).send_keys(str(phoneNumber[7:]))
        driver.find_element(By.NAME, Locators.business_name).send_keys(businessName)
        driver.find_element(By.NAME, Locators.street_address).send_keys(streetAddress)
        driver.find_element(By.NAME, "form.city").send_keys(city)
        driver.find_element(By.NAME, "form.state").send_keys(state)
        driver.find_element(By.NAME, "form.zipCode").send_keys(str(zipCode))
    

        # driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()
        driver.find_element(By.ID, "continueButton").click()

        # Entering tax info
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.NAME, "taxIdNum")))
        driver.find_element(By.NAME, "taxIdNum").send_keys(str(taxIDNum))
        driver.find_element(By.NAME, "taxIdDesc").send_keys(taxProvider)

        # driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
        driver.find_element(By.ID, "continueButtonSubmit").click()