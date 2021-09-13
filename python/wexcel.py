import pandas as pd 
from pandas import DataFrame


def save_data(x, file, sheet, i):

    df = DataFrame(x)
    df.to_excel(file, sheet_name = sheet)