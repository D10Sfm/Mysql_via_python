import mysql.connector
python_testdb = mysql.connector.connect(
    host= "localhost",
    user="root",
    password="*******",
    port="3306",
    database="python_test"
)
db_cursor = python_testdb.cursor()

db_cursor.execute("SELECT * FROM players")

players = db_cursor.fetchall()

for player in players:
  try:
    print("Player Name: "+player[1])
    print("Player Shirt: " + player[2])
  except TypeError:
    continue

db_cursor.execute("SELECT player_name FROM players WHERE shirt_number in ('10','5','16','19','7')")

players = db_cursor.fetchall()
psh = []
for player in players:
    psh.append(player)
print(psh)