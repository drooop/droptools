from pprint import pprint
import pymysql
import pymysql.cursors

HOST = "58.210.69.90"
PORT = 10010
USER = "itielec"
PASSWORD = "iti@123"
DATABASE = "gesm"

def get_data():
    connection = pymysql.connect(
        host='58.210.69.90',
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
    )
    with connection:
        with connection.cursor() as cursor:
            sql = "select * from gesm.ru_realdetail;"
            cursor.execute(sql)
            result = cursor.fetchall()
    return result


if __name__ == "__main__":
    res = get_data()
    pprint(res)
