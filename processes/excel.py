import pandas as pd



class CSVHandler:
    '''
    1) Read the new_or_established.csv file. Pass as parameter one name present in the spreadsheet. 
    If that name has visited the same location within 3 years and their status is not "cancelled", 
    return the string "Established". Else, return "New Patient"
    '''

    def __init__(self, path: str):
        self.df = pd.read_csv(path)
    

    def loc_by_value_and_index(self, index: int, value: str):
        currentLoc = self.df.iloc[index][value]
        return currentLoc
    

    def estOrNew(self, patient_name: str) -> str:
        """
        Parameter 1: CSV file to be read
        Parameter 2: any patient name from the file
        Return: String "Established" or "New Patient"
        """
        
        self.df['date'] = pd.to_datetime(self.df['date'])
        patientDF = self.df[self.df['name'] == patient_name]
        patientDF = patientDF.sort_values(by=['date', 'location'], ascending=False)

        established = False
        for i in range(len(patientDF) - 1):  # Loop through each row, except the last one
            currentLoc = self.loc_by_value_and_index(i, 'location')
            nextLoc = self.loc_by_value_and_index(i+1, 'location')

            currentDate = patientDF.iloc[i]['date'].year
            earliestDate = patientDF.iloc[i + 1]['date'].year

            for index, row in patientDF[patientDF['location'] == currentLoc].iterrows():
                if currentLoc != nextLoc:
                    earliestDate = row['date'].year

            # print(str(currentDate) + " and " + str(earliestDate))
            if currentDate - earliestDate <= 3 and patientDF.iloc[i]['status'] != "cancelled":
                established = True
                break

        if established == True:
            return "Established"
        else:
            return "New Patient"   
        