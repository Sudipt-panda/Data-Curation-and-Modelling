import pymysql

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Sudhir@93',
                             db='DataManagement',
                             port='3036'
                            )
                             
db_cursor = connection.cursor()

db_cursor.execute('SELECT * FROM data_analysis')

table_rows = db_cursor.fetchall()

df = pd.DataFrame(table_rows)
connection.close()