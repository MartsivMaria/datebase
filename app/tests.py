import MySQLdb

try:
    connection = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Mary123",
        db="ajax_systems"
    )
    print("Підключення до MySQL успішне!")
except MySQLdb.Error as e:
    print("Помилка підключення до MySQL:", e)
finally:
    if connection:
        connection.close()
