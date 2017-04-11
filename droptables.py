import sqlite3


db_conn = sqlite3.connect('phase3.db')
print "database DROPd!"
DROPCursor = db_conn.cursor()
try:
	db_conn.execute("DROP TABLE IF EXISTS TRANS;")
	db_conn.execute("DROP TABLE IF EXISTS BUYS;")
	db_conn.execute("DROP TABLE IF EXISTS USER;")
	db_conn.execute("DROP TABLE IF EXISTS RATES;")
	db_conn.execute("DROP TABLE IF EXISTS ADDRESS_INFO;")
	db_conn.execute("DROP TABLE IF EXISTS ADDRESS;")
	db_conn.execute("DROP TABLE IF EXISTS CREDIT_CARD_INFO;")
	db_conn.execute("DROP TABLE IF EXISTS CREDIT_CARD;")
	db_conn.execute("DROP TABLE IF EXISTS PHONE_INFO;")
	db_conn.execute("DROP TABLE IF EXISTS PHONE;")
	db_conn.execute("DROP TABLE IF EXISTS VIEWS;")
	db_conn.execute("DROP TABLE IF EXISTS USER_SELLS;")
	db_conn.execute("DROP TABLE IF EXISTS SALE_ITEM;")
	db_conn.execute("DROP TABLE IF EXISTS HAS_A;")
	db_conn.execute("DROP TABLE IF EXISTS CATEGORY;")
	db_conn.execute("DROP TABLE IF EXISTS SELLER_ITEM;")
	db_conn.execute("DROP TABLE IF EXISTS SUPPLIER_ITEM;")
	db_conn.execute("DROP TABLE IF EXISTS SUPPLIER_SELLS;")
	db_conn.execute("DROP TABLE IF EXISTS SUPPLIER;")

except sqlite3.OperationalError:
    print "table DROP error!"