import sqlite3

connection = sqlite3.connect('Chatbot.db')
cursor = connection.cursor()

sql = """CREATE TABLE `otazky` (
  `otazkaPK` int(10) NOT NULL ,
  `otazka` varchar(255) NOT NULL,
  `odpovediodpovedPKFK` int(10) NOT NULL , 
  `ucelyucelPKFK` int(10) NOT NULL ,
  `ucel` varchar(255) NOT NULL,
  PRIMARY KEY (otazkaPK) ,
  FOREIGN KEY (odpovediodpovedPKFK) REFERENCES odpovedi(odpovedPK),
  FOREIGN KEY (ucelyucelPKFK) REFERENCES  ucely(ucelPK)
)"""

sql2 = """CREATE TABLE `odpovedi` (
  `odpovedPK` int(10) NOT NULL PRIMARY KEY,
  `odpoved` varchar(255) NOT NULL,
  `typ` varchar(255) NOT NULL,
  `ucel` varchar(255) NOT NULL
)"""

sql3 = """CREATE TABLE `ucely` (
  `ucelPK` int(10) NOT NULL PRIMARY KEY ,
  `ucel` varchar(255) NOT NULL
)"""

cursor.execute(sql)
cursor.execute(sql2)
cursor.execute(sql3)

result = cursor.fetchall()

print(result)

cursor.close()
