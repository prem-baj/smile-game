#!/usr/bin/python

import psycopg2

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE answers (
            id SERIAL PRIMARY KEY,
            solution INTEGER NOT NULL,
            answer INTEGER
        )
        """,)
    conn = None
    try:
        # read the connection parameters
        # connect to the PostgreSQL server
        conn = psycopg2.connect(
            host='localhost',
            database='smile-game',
            user="",
            password=""
        )
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            print(command)
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()