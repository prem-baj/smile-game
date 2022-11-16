from db_driver import get_db_connection

def register(name, password):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO users (name, password)'
        'VALUES (%s, %s) RETURNING name, password',
        (name, password)
    )
    user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return user

def update(answer=None,user_id=1):
    print("answer", answer)
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'UPDATE answers SET answer = %s WHERE answer IS NULL AND user_id = %s',
        (answer, user_id)
    )
                
    conn.commit()
    cur.close()
    conn.close()
    return id

def get_actual(user_id=1):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'SELECT id, solution FROM answers WHERE answer IS NULL AND user_id = %s',
        (user_id,)
    )
    dupa = cur.fetchone()
    
    conn.commit()
    cur.close()
    conn.close()
    return dupa

def remove_last_if_exist(user_id=1):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM answers WHERE answer IS NULL AND user_id = %s",
        (user_id,)
    )
    rows_deleted = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    return rows_deleted
