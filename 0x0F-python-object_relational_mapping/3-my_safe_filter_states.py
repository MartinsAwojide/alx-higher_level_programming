#!/usr/bin/python3
"""
    3-my_safe_filter_states.py
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":

    if len(argv) != 5:
        exit(0)

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states \
        WHERE name LIKE %s ORDER BY id ASC", (argv[4],))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except:
        pass
