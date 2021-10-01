import pandas as pd 
from pandas import DataFrame


def save_data(x, file, sheet):
    with pd.ExcelWriter(file, mode='a', engine="openpyxl") as writer:
        df = DataFrame(x)
        df.to_excel(writer, sheet_name = sheet)

def read_data(file):
    return  pd.read_excel(file)