from Connector import Conector
mydb_players = Conector("localhost","root","*******","3306","python_test")
mydb_players.connect_mysql()
print(mydb_players.executesql("select player_name from players where shirt_number in ('10','5','7')"))
sakila_db = Conector("localhost","root","D10S0404","3306","sakila")
sakila_db.connect_mysql()
print(sakila_db.executesql("select count(actor_id) from actor"))
print(sakila_db.executesql("select count(film_id) from film"))











# for player in players:
#     psh.append(player)
# print(psh)

# for player in players:
#     try:
#         print("Player Name: " + player[1])
#         print("Player Shirt: " + player[2])
#     except TypeError:
#         continue