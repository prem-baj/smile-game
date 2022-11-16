#!/usr/bin/python

import psycopg2
from db_driver import get_db_connection
def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE answers (
            id SERIAL PRIMARY KEY,
            solution INTEGER NOT NULL,
            answer INTEGER,
            user_id INTEGER NOT NULL
        )
        """,
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(63) NOT NULL,
            password VARCHAR(63) NOT NULL
        )
        """,    
    )
    conn = None
    try:
        conn = get_db_connection()
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