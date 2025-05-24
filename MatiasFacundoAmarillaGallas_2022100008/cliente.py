import pymysql

def check_client(ci):
    try:
       
        connection = pymysql.connect(
            host='localhost',
            user='unida',  
            password='unida123',  
            database='cliente',  
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection.cursor() as cursor:
           
            sql = "SELECT ci FROM clientes WHERE ci = %s"
            cursor.execute(sql, (ci,))
            result = cursor.fetchone()
            
           
            return result is not None

    except pymysql.MySQLError as e:
        print(f"Error en la base de datos: {e}")
        return False
    finally:
        if 'connection' in locals():
            connection.close()