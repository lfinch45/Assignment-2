import pyautogui
from pathlib import Path
from datetime import datetime

current_directory = Path(__file__).parent
local_folder = fr"{current_directory}/screenshot"
sample_screenshot = "Screenshot 2024-06-17 222915.png"


class BrowserOutlookHandling:

    def get_todays_image(self, image_number):
        current_datetime = datetime.now()
        current_date = current_datetime.strftime("%Y-%m-%d")
        custom_screenshot = f"Screenshot {current_date} {image_number}.png"
        return custom_screenshot

    def openOutlook(emailAddress):
        # Opening outlook on a browser
        edge_browser = pyautogui.locateCenterOnScreen(fr"{local_folder}/{sample_screenshot}", confidence=0.9)
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

    def openEmail(sender, subject):
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
