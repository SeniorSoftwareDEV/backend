from flask_cors import CORS
from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)
CORS(app)
app.config['MYSQL_HOST'] = 'tradingbuddy.cjwfktkwkbo1.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'RDStradingbuddydb0510!'
app.config['MYSQL_DB'] = 'trading'
mysql = MySQL(app)