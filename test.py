from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
import sys, json

app = Flask(__name__)

app.config['MYSQL_USER'] = 'test'
app.config['MYSQL_PASSWORD'] = 'test'
app.config['MYSQL_DB'] = 'test'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

CORS(app)

def get_table(t):
    curr = mysql.connection.cursor()
    curr.execute("SELECT * from " + t)
    rv = curr.fetchall()
    row_headers=[x[0] for x in curr.description]
    data=[]
    for result in rv:
        data.append(dict(zip(row_headers,result)))
    return data

@app.route("/")
def hello_world():
    to_return = {}
    to_return["cars"] = get_table("cars")
    to_return["log"] = get_table("log")

    return json.dumps(to_return)


if __name__ == "__main__":
    app.run()