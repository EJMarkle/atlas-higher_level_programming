#!/usr/bin/python3
""" Lists all states that start with 'N' from db 'hbtn_0e_0_usa' """
import MySQLdb
import sys


if __name__ == "__main__":
    """Check correct # args"""
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()
