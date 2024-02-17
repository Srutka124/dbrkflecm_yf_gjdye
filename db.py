import sqlite3


db_name = 'db.splite'


conn = None
cursor= None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    conn = sqlite3.connect.cursore
def close():
    cursor .close()
    conn.commit()

def do (qery):
    cursor.execute(qery)
    conn.commit()
def create_tables():
    open()
    do('''
       CREate TTABLE IF NOT EXISTS users(
       id INTEGER PRIMARY KEY,
       status VARCHAR,
       bnus INTEGER,
       login VARCHAR,
       password VARCHAR,
       product_best INTEGER[]
       )
       '''

    )
    do ('''
        CREATE TTABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY,
        status VARCHAR
        give_bonus INTEGER
        )
        
        '''
        

        
        
        
    )
    do('''CREATE TABLE IF NOT EXISTS categories (
       id INTEGER PRIMARY KEY,
       name VARCHAR )
       ''')
   

def drop_tabel():
    open()
    
    do ('DROP TABLE IF EXISTS product')
    do ('DROP TABLE IF EXSISTS USER')
    close()
def insert_test_data():
    open()
    cursor.execute('''INSERT INTO users (login, password) VALUES (?,?)''', ['admin', 'admin'])
    conn.commit()

    

    cursor.execute('''INSERT INTO ptoduct 
                   (title, description, image, class_id,author_id ) 
                   VALUES (?, ?,?,?,?)''', ['NEWS TITLE',
                                             "descrosakfokdsf", 
                                            '2asd', 
                                            '1',
                                            '1',
                                            ])
    conn.commit()
def show_tables():
    open()
    cursor.execute('''SELECT * FROM users''')
    print(cursor.fetchall())
    
    cursor.execute('''SELECT * FROM categories''')
    print(cursor.fetchall())

    cursor.execute('''SELECT * FROM product''')
    print(cursor.fetchall())
    close()
def get_all_news():
    open()
    cursor.execute('''SELECT product.title, product.description, categories.name, users.login
                   FROM news INNER JOIN categories 
                   ON news.class_id == categories.id
                INNER JOIN users ON news.author_id == users.id''')
    return cursor.fetchall()

def get_category_by_id(id):
    open()
    cursor.execute('''SELECT * FROM categories WHERE categories.id == (?)''', [id])
    return cursor.fetchall()
def add_news():
    cursor.execute('''INSERT INTO news 
                   (title, description, image, class_id,author_id ) 
                   VALUES (?, ?, ?, ?, ?)''', [title, description, image, class_id, author_id])
    conn.commit()
    close()

# drop_table()
# create_tables()
# insert_test_data()
# show_tables()
add_product("1212qw, 12wqwqw")
news = get_all_news()
print(get_category_by_id(news[0][4]))