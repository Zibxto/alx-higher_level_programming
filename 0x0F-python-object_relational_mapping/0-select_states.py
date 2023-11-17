#!/usr/bin/python3
''' A script that lists all states from the database hbtn_0e_0_usa '''


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    conn.close()