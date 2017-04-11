from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask import request
import sqlite3


db_conn = sqlite3.connect('test.db',check_same_thread=False)
print "database created!"
createCursor = db_conn.cursor()

try:
    db_conn.execute("CREATE TABLE USER(Username TEXT PRIMARY KEY NOT NULL,"
                    "Password TEXT NOT NULL);")
    db_conn.execute("INSERT INTO USER VALUES ('Nathan','Nathan')")
    # db_conn.execute("CREATE TABLE User(ID INTEGER PRIMARY KEY "
    #                 "AUTOINCREMENT NOT NULL, "
    #                 "FName TEXT NOT NULL, "
    #                 "LName TEXT NOT NULL, "
    #                 "Age INTEGER NOT NULL, "
    #                 "Address TEXT);")

    db_conn.commit()
except sqlite3.OperationalError:
    print "table creation error!"

print "Table has been created"

#db_conn.execute("INSERT INTO User (FName, LName, Age, Address) VALUES('Sidd', 'Shan', 22, '340 East Beaver')")
#db_conn.commit()


print "data base is created"
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello():
    return render_template("index.html")
    #return "Hello World!"


@app.route('/login.html',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username=request.form['Username']
        password=request.form['Password']
        createCursor.execute("SELECT Username,Password FROM USER WHERE Username='%s' AND Password='%s'",
                             {"username": username, "password": password})
        users = createCursor.fetchall()
        print "%s" % users
        return render_template("login.html")
                 #return render_template('index.html',users=users)
    else:
         return render_template("login.html")
    #return "<h2> Welcome. Please enter your user name and PW to proceed"


@app.route('/account.html')
def account():
    return render_template("account.html")


@app.route('/home')
def home_page():
    return "Welcome back! ___"  # include var for username in underline


@app.route('/browse')
def browse():
    return "this is where they will be able to search products"


if __name__ == "__main__":
    app.run(debug=True)


db_conn.close()
print "database is closed"
