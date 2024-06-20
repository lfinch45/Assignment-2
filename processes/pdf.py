import pandas as pd


class PDFHandler:
    def __init__(self, path):
        self.pdf = pd.read_hdf(path)