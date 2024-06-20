import pyautogui



class AppOutlookHandling:

    def openOutlook():
        # Opening outlook through the app instead of through a browser
        search_bar = pyautogui.locateCenterOnScreen(r"C:\Users\LukeFinch\OneDrive - Jorie Healthcare\Desktop\snippets\windows_searchbar_icon.png", confidence=0.8)
        pyautogui.moveTo(search_bar)
        pyautogui.click()
        pyautogui.write("outlook")
        pyautogui.hotkey("enter")



    def openEmail(sender, subject):
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