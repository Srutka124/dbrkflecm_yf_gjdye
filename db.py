import sqlite3


db_name = 'db.splite'


conn = None
cursor= None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.commit()

def do (qery):
    cursor.execute(qery)
    conn.commit()
def create_tables():
    open()
    do('''
       CREATE TABLE IF NOT EXISTS users (
       id INTEGER PRIMARY KEY,
       status VARCHAR,
       points INTEGER)
       '''

    )
    do ('''
        CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY,
        status VARCHAR,
        give_points INTEGER,
        infa VARCHAR,
        photo VARCHAR,
        price INTEGER,
        name VARCHAR
    
        )
        '''
    )
    

def drop_tabel():
    open()
    do ('DROP TABLE IF EXISTS product')
    do ('DROP TABLE IF EXISTS user')
    close()

def insert_test_data():
    open()
    cursor.execute('''INSERT INTO users (status , points) VALUES (?,?)''',['ASasASASSa','5'] )
    conn.commit()
    cursor.execute('''INSERT INTO product (status ,give_points, infa, photo , price, name) 
                   VALUES (?, ?,?, ?,?,?)''', ['vip','5','adsdksadsakdksakdkd;ldksadd', 'https://t4.ftcdn.net/jpg/01/67/74/79/360_F_167747932_NE1da5cf9FM30QExtlFjbmk9ypItoJl2.jpg',
                                        '15000','GELEcSU'])
    conn.commit()


def show_tables():
    open()
    cursor.execute('''SELECT * FROM users''')
    print(cursor.fetchall())
    

    cursor.execute('''SELECT * FROM product''')
    print(cursor.fetchall())
    close()
def get_all_products():
    open()
    cursor.execute('''SELECT * FROM product''')
    return cursor.fetchall()

def get_category_by_id(id):
    open()
    cursor.execute('''SELECT * FROM categories WHERE categories.id == (?)''', [id])
    return cursor.fetchall()
def add_products(a, b ,c , d, e, f, g):
    cursor.execute('''INSERT INTO produts (status , giwe_points , infa , photo , price ,name)VALURES (?,?,?))''',[ 'a','b','c' , 'd','e' , 'f' , 'g'] )
    conn.commit()
    close()

drop_tabel()
create_tables()
insert_test_data()
show_tables()
# add_products("1212qw", "12wqwqw" , "12")
