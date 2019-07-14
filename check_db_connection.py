import pymysql.cursors


connecton = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = connecton.cursor()
    cursor.execute("SELECT * FROM group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connecton.close()
