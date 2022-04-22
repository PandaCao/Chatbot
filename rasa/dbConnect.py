import sqlite3

try:
    sqliteConnection = sqlite3.connect('Chatbot.db')
    cursor = sqliteConnection.cursor()
    print("Připojení k databázi bylo v pořádku")

    sqliteVerze = "select sqlite_version();"
    cursor.execute(sqliteVerze)
    verze = cursor.fetchall()
    print("SQLite Database Version is: ", verze)
    cursor.close()

except sqlite3.Error as error:
    print("Error při připojení k databázi:", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("Uzavření připojení k databázi.")