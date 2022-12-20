#!/usr/bin/python3
"""
    2-my_filter_states.py
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    if len(argv) != 5:
        exit(0)

    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=argv[1], passwd=argv[2], db=argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name='{}' \
        ORDER BY id ASC".format(argv[4]))
        for row in cur.fetchall():
            if row[1] == argv[4]:
                print(row)
        cur.close()
        db.close()
    except:
        pass
