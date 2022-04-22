import sqlite3

connection = sqlite3.connect('Chatbot.db')
cursor = connection.cursor()

obory = """SELECT odpoved FROM odpovedi WHERE ucel='obory'"""

cursor.execute(obory)

result = cursor.fetchall()
for x in result:
    str = ''.join(x)
print(str)
