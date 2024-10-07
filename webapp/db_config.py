import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='P@ssw0rd@321',
        database='izodemo'
    )
    return connection
