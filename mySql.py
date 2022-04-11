from Connector import Conector
mydb_players = Conector("localhost","root","******","3306","players")
mydb_northwind = Conector("localhost","root","******","3306","northwind")

# select
# print(mydb_players.executesql("select player_name from players where shirt_number in ('10','5','7')"))
# print(mydb_players.executesql("select player_name from players where player_name regexp '^[A|B|M]'"))
# print(mydb_players.executesql("select * from players where id > 5"))
# print(mydb_players.executesql("select player_name,shirt_number from players where player_name in ('Ansu Fati','Ferran Torres','Adama Traore') order by shirt_number desc"))
# print(mydb_players.executesql("select player_name,shirt_number from players where player_name in ('Memphis Depay','Ousmane Dembele','Ter Stegen') order by shirt_number asc"))


# join
# print(mydb_northwind.executesql("select concat(first_name,' ',last_name) as fullname, o.order_date,o.ship_city from customers as c inner join orders as o on c.id = o.customer_id group by o.ship_city"))
# print(mydb_northwind.executesql(" select p.product_name,p.quantity_per_unit,o.unit_price,o.discount,o.quantity,op.order_date from order_details as o inner join products as p on o.product_id = p.id inner join orders as op on o.order_id = op.id order by op.order_date desc"))
# print(mydb_northwind.executesql(" select p.product_name,p.quantity_per_unit,o.unit_price,o.discount,o.quantity,op.order_date from order_details as o inner join products as p on o.product_id = p.id inner join orders as op on o.order_id = op.id order by op.order_date desc"))
# print(mydb_northwind.executesql("select e.id,concat(e.first_name,' ',e.last_name) as fullname ,e.job_title,p.privilege_name,e.city from employee_privileges as ev inner join employees as e on ev.employee_id = e.id inner join privileges as p  group by e.city order by employee_id"))





# update

# print(mydb_players.executesql("select id,player_name,shirt_number from players"))
# print(mydb_players.executesql("select shirt_number from players where player_name in ('Minugeza')"))
# print(mydb_players.executesql("update players set shirt_number = '22' where id = 9;","update"))
# print(mydb_players.executesql("select shirt_number from players where player_name in ('Minugeza');"))
# print(mydb_players.executesql("select shirt_number,player_name from players where player_name in ('Ter-Stegen')"))
# print(mydb_players.executesql("update players set player_name = 'Marc Andre Ter-Stegen' where id = 0","update"))
# print(mydb_players.executesql("select shirt_number,player_name from players where id = 0"))
# print(mydb_players.executesql("select shirt_number,player_name from players where id = 28"))
# print(mydb_players.executesql("update players set player_name = 'Ez Abdoulay' where id = 28","update"))
# print(mydb_players.executesql("select shirt_number,player_name from players where id = 28 "))
# print(mydb_players.executesql("select shirt_number,player_name from players where id = 24"))
# print(mydb_players.executesql("update players set shirt_number = '55' where id = 24",'update'))
# print(mydb_players.executesql("select shirt_number,player_name from players where id = 24"))
# print(mydb_players.executesql("select shirt_number,player_name from players where id = 6 "))
# print(mydb_players.executesql("update players set shirt_number = '15' where id = 6",'update'))
# print(mydb_players.executesql("select shirt_number,player_name from players where id = 6 "))