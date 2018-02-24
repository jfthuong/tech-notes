import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
#
df1 = pd.DataFrame({
    'nb obj':123,
    'nb layers': 456,
    'nb toto': 456,
    'nb types': 0,
}, index=['TC01'], dtype='int32')

