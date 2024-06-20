from processes import CSVHandler, PDFHandler



class Browser(CSVHandler, PDFHandler):
    def __init__(self):
        super(Browser).__init__(self)