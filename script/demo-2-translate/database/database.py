import pymysql

class DataBase:
    def connect(host = 'localhost',port = 3306,user = 'root',password ='psnb',db = 'translate'):

        db_config = {
            'host':host,
            'port':port,
            'user':user,
            'password':password,
            'database':db,
            'charset':'utf8'
        }

        try:
            return pymysql.connect(**db_config)
        except:
            raise pymysql.err.MySQLError