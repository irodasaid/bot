import sqlite3
conn = sqlite3.connect ('menu.sqlite')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Menu
(PROD_ID INTEGER,
NAMES STRING,
PRICE INTEGER,
CURRENCY STRING)
''')
get_prod_names = '''
SELECT NAMES
FROM Menu
WHERE NAMES = '{}'
'''


