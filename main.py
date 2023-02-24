import pandas as pd
import os


# df = pd.read_excel('excel.xlsx')
# print(df)

def main(excel_filename: str):
    if not os.path.exists(excel_filename):
        print('Incorrect filename. Try again')
        return None



if __name__ == '__main__':
    main('C:/Users/a.ibraev/Documents/GitHub/Halim/excel.xlsx')
