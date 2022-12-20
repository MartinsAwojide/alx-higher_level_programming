#!/usr/bin/python3
"""
    file: 0-select_states.py
"""

if __name__ == "__main__":
        import MySQLdb
        from sys import argv

        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=argv[1],
                passwd=argv[2],
                db=argv[3])
        cur = db.cursor()

        cur.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cur.fetchall()
        for row in rows:
                print(row)

        cur.close()
        db.close()
