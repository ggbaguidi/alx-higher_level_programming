#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
that is safe from MySQL injections!
"""
import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=mysql_username,
                           passwd=mysql_password,
                           db=database_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states\
                 WHERE name=%s\
                 ORDER BY states.id ASC",(state_name_searched,))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == state_name_searched:
            print(row)
    cur.close()
    conn.close()
