import mysql.connector
class Conector:
    def __init__(self,host,user,password,port,database,client=False):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
    def connect_mysql(self):
        python_testdb = mysql.connector.connect(
            host= self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database=self.database
        )
        return python_testdb
    def executesql(self,x):
        connect = self.connect_mysql()
        curser = connect.cursor()
        curser.execute(str(x))
        output = curser.fetchall()
        v =[]
        for i in output:
            v.append(i)

        return v