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
    do('''CREATE TABLE IF NOT EXISTS progect (
        id INTEGER PRIMARY KEY,
        img VARCHAR,
        text VARCHAR)''')
    close()

def drop_tabel():
    open()
    do ('''DROP TABLE IF EXISTS progect''')
    do ('DROP TABLE IF EXISTS product')
    do ('DROP TABLE IF EXISTS user')
    close()

def insert_test_data():
    open()
    cursor.execute('''INSERT INTO users (status , points) VALUES (?,?)''',['ASasASASSa','5'] )
    conn.commit()
    cursor.execute('''INSERT INTO product (status ,give_points, infa, photo , price, name) 
                   VALUES (?, ?,?, ?,?,?)''', ['12','5','fsfxfjdsflkjdsjflkjfljfjfdsjfdsjfsfkdsfdjfdsf fdsfdsf  s fdfds dfdsfddffdsf fdsfdsfsf fdsfdsf dsfdsfdds sfdsfdssfdsf dsfds ffdfdsfds fdsfdsfs sfds fd fsd sdsad dsdsadsa dsasad fs dsv ds hdds ffd gds fd', 'https://t4.ftcdn.net/jpg/01/67/74/79/360_F_167747932_NE1da5cf9FM30QExtlFjbmk9ypItoJl2.jpg',
                                        '15000','GELEcSU'])
    conn.commit()
    cursor.execute('''INSERT INTO progect (img , text) VALUES (?,?)''',['http://robitnia.com/wp-content/uploads/2015/06/krono-300x157.jpg','Завод з виробництва ДСП «Кроно» (Swiss Krono Group), м. Брошнів, Ів.-Франківська обл. Монтаж і введення в експлуатацію семи трансформаторних підстанцій. Виготовлення, монтаж та введення в експлуатацію електричних щитів (силових, керування, автоматизації). Монтаж та налагодження електричної частини технологічної лінії шліфовки. Реконструкція системи освітлення складів та виробничих приміщень.Завод з виробництва ДСП «Кроно» (Swiss Krono Group), м. Камянка-Бузька, Львівська обл. Монтаж і введення в експлуатацію двох трансформаторних підстанцій. Монтаж і введення в експлуатацію нового РП-10кВ ПС 110/10 кВ «Кроно». Виготовлення, монтаж та введення в експлуатацію електричних щитів (силових, керування, автоматизації). Монтаж та налагодження електричної частини технологічної лінії дробилки.Відгук'] )
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
def get_all_progect():
    open()
    cursor.execute('''SELECT * FROM progect''')
    return cursor.fetchall()

def get_product_by_id(id):
    open()
    cursor.execute('''SELECT * FROM product WHERE product.id == (?)''', [id])
    return cursor.fetchall()
def add_products(a, b ,c , d, e, f):
    open()
    cursor.execute('''INSERT INTO product (status, give_points, infa, photo, price, name) VALUES (?, ?, ?, ?, ?, ?)''', [a, b, c, d, e, f])
    conn.commit()
    close()

drop_tabel()
create_tables()
insert_test_data()
show_tables()

# add_products("1212qw", "12wqwqw" , "12")
