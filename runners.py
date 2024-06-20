from processes import CSVHandler, BrowserOutlookHandling, OneHealthCareLogin, AppOutlookHandling
import pandas as pd

        
class Runners:
    def __init__(self):
        pass

    def run_csv(self):
        csv_path = r'download/file.csv'
        csv_handler = CSVHandler(csv_path)
        verdict = csv_handler.estOrNew("Ana")

    def run_outlook(self):
        AppOutlookHandling.openOutlook("lfinch@joriehc.com")
        AppOutlookHandling.openEmail("Kelly Long", "Compliance Update : Patient Data Security: Upholding Integrity as a HIPAA Priority.")
    

    def run_browser(self):
        BrowserOutlookHandling.openOutlook("lfinch@joriehc.com")
        BrowserOutlookHandling.openEmail("Kelly Long", "Compliance Update : Patient Data Security: Upholding Integrity as a HIPAA Priority.")



