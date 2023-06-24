from flask_cors import CORS
from flask import Flask, send_from_directory
from flask_mysqldb import MySQL
app = Flask(__name__, static_folder='../../frontend/build/static')
@app.route('/')
def index():
    return send_from_directory('../../frontend/build', 'index.html')
@app.route('/<path:text>')
def all_routes(text):
    return send_from_directory('../../frontend/build', 'index.html')

CORS(app)
app.config['MYSQL_HOST'] = 'tradingbuddy.cjwfktkwkbo1.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'RDStradingbuddydb0510!'
app.config['MYSQL_DB'] = 'trading'
mysql = MySQL(app)