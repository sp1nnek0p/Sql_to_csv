import pymssql

import lists
from pathlib import Path
import os

CURRENT_DIR = Path.cwd()


conn = pymssql.connect('CTRACK-PC\CTRACK', 'sa', 'ctrack2k', "Ctrack6")
cursor = conn.cursor(as_dict=True)

cursor.execute('SELECT * FROM dbo.Mobiles')

if Path.is_file(CURRENT_DIR / 'export.csv'):
    os.remove(CURRENT_DIR / 'export.csv')


for row in cursor:
    if row['ID'] in lists.vehicles:

        newstring : str = ""
        if ',' in str(row['PLACE']):
            newstring = str(row['PLACE']).replace(',', '-')
        else:
            newstring = str(row['PLACE'])

        newstring1 = newstring.split('-')

        # print(row['ID'] +', '+ newstring1[-1]) # TESTING THE OUTPUT

        with open('export.csv', 'a') as f:
            f.writelines(
                row['ID'] +', '+
                newstring +', '+
                newstring1[-1]+'\n'
            )

conn.close()

