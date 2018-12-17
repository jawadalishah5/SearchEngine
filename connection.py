import pymysql
import pymysql.cursors


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Nust12345678',
                             db='tf',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
