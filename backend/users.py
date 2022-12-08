from db_driver import get_db_connection

def register(name, password):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO users (username, password)'
        'VALUES (%s, %s) RETURNING username, password',
        (name, password)
    )
    user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return user

def get_by_username(username):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'SELECT id, username, password FROM users WHERE username = %s',
        (username,)
    )
    dupa = cur.fetchone()
    
    conn.commit()
    cur.close()
    conn.close()
    return dupa

def get_by_id(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'SELECT id, username, password FROM users WHERE id = %s',
        (id,)
    )
    dupa = cur.fetchone()
    
    conn.commit()
    cur.close()
    conn.close()
    return dupa


