import mysql.connector


class Conector:
    def __init__(self, host, user, password, port, database):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database

    def connect_mysql(self):
        python_testdb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database=self.database
        )
        return python_testdb

    def executesql(self, x, type_action='query'):
        connect = self.connect_mysql()
        if type_action == 'query':
            curser = connect.cursor()
            curser.execute(str(x))
            output = curser.fetchall()
            v = []
            for i in output:
                v.append(i)

            return '\n'.join(map(str, v))
        elif type_action == 'update':
            curser = connect.cursor()
            curser.execute(str(x))
            connect.commit()
        else:
            raise TypeError("the type parameter can get only 'query' or 'update'")
