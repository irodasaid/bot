import sqlite3
conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users
(TELEGRAM_ID INTEGER,
USER_NAME STRING,
PHONE INTEGER,
LANG INTEGER )
''')
reg_in_table = '''INSERT INTO Users VALUES ('{}','{}',0,0)
'''
update_lang_in_table = '''
UPDATE Users
SET LANG = '{}'
WHERE TELEGRAM_ID = '{}'
'''
lang_in_table = '''
SELECT LANG
FROM Users
WHERE TELEGRAM_ID = '{}'
'''