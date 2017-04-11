# from flask import Flask
# from flask_bootstrap import Bootstrap
import sqlite3


db_conn = sqlite3.connect('phase3.db')
print "database created!"
createCursor = db_conn.cursor()

try:
	db_conn.execute("CREATE TABLE IF NOT EXISTS TRANS(TRANS_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,TIMESTAMP TEXT NOT NULL, IS_SUCCESS TEXT, SALE_TYPE TEXT NOT NULL);")
	db_conn.execute("CREATE TABLE IF NOT EXISTS BUYS(USER_ID INTEGER, TRANSACTION_ID INTEGER, PRODUCT_ID INTEGER, PRIMARY KEY(USER_ID,TRANSACTION_ID,PRODUCT_ID));")
	db_conn.execute("CREATE TABLE IF NOT EXISTS USER(USER_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, USERNAME TEXT NOT NULL, ANNUAL_INCOME INTEGER NOT NULL, PASSWORD TEXT NOT NULL,  EMAIL TEXT NOT NULL, NAME TEXT NOT NULL);")
	db_conn.execute("CREATE TABLE IF NOT EXISTS RATES(USER_ID INTEGER PRIMARY KEY,  DESCRIPTION TEXT NOT NULL, RATING INTEGER NOT NULL);")
	db_conn.execute("CREATE TABLE IF NOT EXISTS ADDRESS_INFO(USER_ID INTEGER NOT NULL, STREET TEXT NOT NULL, PRIMARY KEY(USER_ID,STREET));")
	db_conn.execute("CREATE TABLE IF NOT EXISTS ADDRESS(STREET TEXT NOT NULL, CITY TEXT NOT NULL, STATE TEXT NOT NULL,PRIMARY KEY(STREET));")
	db_conn.execute("CREATE TABLE IF NOT EXISTS CREDIT_CARD_INFO(USER_ID INTEGER NOT NULL, CCNUMBER INTEGER NOT NULL,PRIMARY KEY(USER_ID,CCNUMBER));")
	db_conn.execute("CREATE TABLE IF NOT EXISTS CREDIT_CARD(TYPE TEXT NOT NULL, CCNUMBER INTEGER PRIMARY KEY NOT NULL);")
	db_conn.execute("CREATE TABLE IF NOT EXISTS PHONE_INFO(USER_ID INTEGER NOT NULL, PHONE_NUMBER INTEGER NOT NULL,PRIMARY KEY(USER_ID,PHONE_NUMBER));")
	db_conn.execute("CREATE TABLE IF NOT EXISTS PHONE(PHONE_NUMBER INTEGER PRIMARY KEY NOT NULL);")
	db_conn.execute("CREATE TABLE IF NOT EXISTS VIEWS(USER_ID INTEGER NOT NULL, PRODUCT_ID INTEGER , TIMESTAMP TEXT NOT NULL,PRIMARY KEY(PRODUCT_ID,USER_ID));")
	db_conn.execute("CREATE TABLE IF NOT EXISTS USER_SELLS(USER_ID INTEGER NOT NULL, PRODUCT_ID INTEGER ,PRIMARY KEY(PRODUCT_ID,USER_ID));")
	db_conn.execute("CREATE TABLE IF NOT EXISTS SALE_ITEM(PRODUCT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, LIST_PRICE FLOAT NOT NULL, PRODUCT_NAME TEXT NOT NULL,  PRODUCT_DESCRIPTION TEXT NOT NULL, URL TEXT NOT NULL);")
	db_conn.execute("CREATE TABLE IF NOT EXISTS HAS_A(PRODUCT_ID INTEGER NOT NULL, CATEGORY_NAME TEXT, PRIMARY KEY(PRODUCT_ID,CATEGORY_NAME));")
	db_conn.execute("CREATE TABLE IF NOT EXISTS CATEGORY(CATEGORY_NAME TEXT PRIMARY KEY);")
	db_conn.execute("CREATE TABLE IF NOT EXISTS SELLER_ITEM(PRODUCT_ID INTEGER PRIMARY KEY NOT NULL, RESERVE_PRICE FLOAT NOT NULL, CURRENT_BID FLOAT NOT NULL,  TIME_REMAINING TEXT NOT NULL, PRODUCT_LOCATION TEXT NOT NULL);")
	db_conn.execute("CREATE TABLE IF NOT EXISTS SUPPLIER_ITEM(PRODUCT_ID INTEGER PRIMARY KEY NOT NULL, STOCK_LEVEL INTEGER NOT NULL);")
	db_conn.execute("CREATE TABLE IF NOT EXISTS SUPPLIER_SELLS(PRODUCT_ID INTEGER NOT NULL, SUPPLIER_ID INTEGER NOT NULL, PRIMARY KEY(PRODUCT_ID,SUPPLIER_ID));")
	db_conn.execute("CREATE TABLE IF NOT EXISTS SUPPLIER(SUPPLIER_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, PHONE_NUMBER INTEGER NOT NULL, ADDRESS TEXT NOT NULL, POC TEXT NOT NULL, COMPANY_NAME TEXT NOT NULL, REVENUE FLOAT NOT NULL, SUPPLIER_CATEGORY TEXT NOT NULL);")


	db_conn.commit()
except sqlite3.OperationalError:
    print "table creation error!"

print "Table has been created"

# RUN THESE IN ORDER YOU MUST ENTER THE USER,SALE_ITEM,TRANSACTION_ID AND SUPPLIER TO CREATE THE ID'S

db_conn.execute("INSERT INTO TRANS (TIMESTAMP, IS_SUCCESS, SALE_TYPE)  VALUES(DateTime('now'), 'TRUE', 'BID'), (DateTime('now'), 'TRUE', 'BUY NOW'), (DateTime('now'), 'TRUE', 'BID'), (DateTime('now'), 'TRUE', 'BID'), (DateTime('now'), 'TRUE', 'BUY NOW');")
db_conn.execute("INSERT INTO USER (USERNAME, ANNUAL_INCOME, PASSWORD,EMAIL,NAME)  VALUES('ABC11', 40235, 'MONKEY123','ABC11@hotmail.com','Abe Cambrige'), ('MHG13', 65231, 'CAT123','MHG13@hotmail.com','Mike Griffith'), ('TYR14', 91201, 'FISH123','TYR14@hotmail.com','Tyler Roudolf'), ('SPW15', 56210, 'DOG123','SPW15@hotmail.com','Steve Witherspoon'), ('NWB12', 120365, 'RAT123','NWR12@hotmail.com','Nate Bedford');")
db_conn.execute("INSERT INTO SALE_ITEM (LIST_PRICE, PRODUCT_NAME, PRODUCT_DESCRIPTION, URL)  VALUES(65.14, 'WHIRLPOOL BLENDER', '10 INCH BLENDER STAINLESS STEEL BLADES','www.himalaya.com/AOIHSDF8ADUHFASD'), (15.32, 'QUICKSILVER T-SHIRT', 'RED COTTON T-SHIRT','www.himalaya.com/OAIQWHEOF7W0E9'), (122, 'JORDAN SHOES', 'BLUE JORDAN SHOES','www.himalaya.com/2A1WRFWRSG31A5'), (40.21, 'RGH-12 MOUSE', 'TOSHIBA MOUSE','www.himalaya.com/QAHWEF51SE'), (5.13, 'NIKE SOCKS', 'BLACK LARGE SOCKS','www.himalaya.com/PINWEF155AWE');")
db_conn.execute("INSERT INTO SUPPLIER (PHONE_NUMBER, ADDRESS, POC, COMPANY_NAME,REVENUE,SUPPLIER_CATEGORY)  VALUES(2651452698, '5406 BOULDER DRIVE', 'XXXX','BIBLER CO.',6654654.2,'ELECTRONICS'), (1526459584, '5891 MAIN DRIVE', 'YYYY','WIBLER INC.',1256954.5,'CLOTHING'), (5412859451, '6842 OAK ROAD', 'ZZZZ','SHNIDEL INC.',2594875.3,'JEWELRY'), (4869542631, '11 FRANK AVE', 'JJJJ','JEMBLE CO.',4584951.2,'AUTOMOTIVE'), (3629514726, '36 BEAVER AVE', 'PPPP','STIENBERG INC.',654128.8,'HARWARE TOOLS');")
db_conn.execute("INSERT INTO BUYS (USER_ID,TRANSACTION_ID,PRODUCT_ID)  VALUES(1,5,4), (1,5,2), (1,4,1), (1,3,3), (1,2,5);")
db_conn.execute("INSERT INTO RATES (RATING,DESCRIPTION,USER_ID)  VALUES(4,'VERY GOOD',4), (2,'LACKLUSTER',1), (5,'AMAZING',2), (1,'TERRIBLE',5), (3,'THE WORST',3);")
db_conn.execute("INSERT INTO ADDRESS_INFO (USER_ID,STREET)  VALUES(4,'1 BOULDER DRIVE'), (2,'6 MAIN DRIVE'), (5,'62 OAK DRIVE'), (1,'75 HACIENDA DRIVE'), (3,'88 CACTUS DRIVE');")
db_conn.execute("INSERT INTO ADDRESS (CITY,STREET,STATE)  VALUES('PITTSBURGH','1 BOULDER DRIVE','PA'), ('PHILIDELPHIA','6 MAIN DRIVE','PA'), ('NEW YORK CITY','62 OAK DRIVE','NY'), ('LOS ANGELOS','75 HACIENDA DRIVE','CA'), ('AUSTIN','88 CACTUS DRIVE','TX');")
db_conn.execute("INSERT INTO CREDIT_CARD_INFO (USER_ID,CCNUMBER)  VALUES(4,4444555566668888), (2,1111222255558888), (5,2222555566669999), (1,6666555588889999), (3,2222999944446666);")
db_conn.execute("INSERT INTO CREDIT_CARD (TYPE,CCNUMBER)  VALUES('VISA',4444555566668888), ('MASTER',1111222255558888), ('VISA',2222555566669999), ('MASTER',6666555588889999), ('DISCOVER',2222999944446666);")
db_conn.execute("INSERT INTO PHONE_INFO (USER_ID,PHONE_NUMBER)  VALUES(4,6543219874), (2,3216549874), (5,9638527410), (1,7419638520), (3,9516238470);")
db_conn.execute("INSERT INTO PHONE (PHONE_NUMBER)  VALUES(6543219874), (3216549874), (9638527410), (7419638520), (9516238470);")
db_conn.execute("INSERT INTO VIEWS (USER_ID,PRODUCT_ID,TIMESTAMP)  VALUES(4,4,'3:15PM'), (2,1,'4:15PM'), (5,2,'5:45PM'), (1,5,'9:05PM'), (3,3,'3:15PM');")
db_conn.execute("INSERT INTO USER_SELLS (USER_ID,PRODUCT_ID)  VALUES(4,4), (2,1), (5,2), (1,5), (3,3);")
db_conn.execute("INSERT INTO HAS_A (PRODUCT_ID,CATEGORY_NAME)  VALUES(4,'ELECTRONICS'), (2,'CLOTHING'), (5,'JEWELRY'), (1,'AUTOMOTIVE'), (3,'HARWARE TOOLS');")
db_conn.execute("INSERT INTO CATEGORY (CATEGORY_NAME)  VALUES('ELECTRONICS'), ('CLOTHING'), ('JEWELRY'), ('AUTOMOTIVE'), ('HARWARE TOOLS');")
db_conn.execute("INSERT INTO SELLER_ITEM (PRODUCT_ID,RESERVE_PRICE,CURRENT_BID,TIME_REMAINING,PRODUCT_LOCATION)  VALUES(4,60.21,40.36,'3:28PM', 'PITTSBURGH'), (2,15.32,7.69,'3:28PM', 'NEW YORK CITY'), (5,122,80,'3:28PM', 'NEW YORK CITY'), (1,40.21,32,'3:28PM', 'ST.LOUIS'), (3,5.13,1.23,'3:28PM', 'PITTSBURGH');")
db_conn.execute("INSERT INTO SUPPLIER_ITEM (PRODUCT_ID,STOCK_LEVEL)  VALUES(4,65), (2,14), (5,12), (1,40), (3,5);")
db_conn.execute("INSERT INTO SUPPLIER_SELLS (PRODUCT_ID,SUPPLIER_ID)  VALUES(4,4), (2,2), (5,5), (1,4), (3,3);")

db_conn.commit()

print "data base is created"
# app = Flask(__name__)
# Bootstrap(app)
# @app.route('/')
# def hello():
    # return "Hello World!"
# @app.route('/login')
# def login():
    # return "<h2> Welcome. Please enter your user name and" \
           # " PW to proceed"
# @app.route('/home')
# def home_page():
    # return "Welcome back! ___"  include var for username in underline
# @app.route('/browse')
# def browse():
    # return "this is where they will be able to search products"
# if __name__ == "__main__":
    # app.run(debug='TRUE')


db_conn.close()
print "database is closed"