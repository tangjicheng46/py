import random
import sys

import mysql.connector


class Student:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
        self.id = random.randint(0, 1000)
        seq = "".join([chr(i) for i in range(ord('a'), ord('z'))])
        self.name = random.choice(seq.upper()) + \
            "".join(random.choices(seq, k=5))

    def insert_query(self, cursor):
        query = f'INSERT INTO student (id, name) VALUES ({self.id}, "{self.name}")'
        print(query)
        cursor.execute(query)


def main(password):
    cnx = mysql.connector.connect(
        user="root", password=password, database="testforpy")
    cursor = cnx.cursor(buffered=True)
    N = 100
    for i in range(N):
        s = Student()
        s.insert_query(cursor=cursor)
        cnx.commit()
    cnx.close()


if __name__ == "__main__":
    password = sys.argv[1]
    main(password=password)
