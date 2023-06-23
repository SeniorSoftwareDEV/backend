from api.config import app, mysql
from flask import jsonify

@app.route("/mttools", methods=["POST"])
def main():
    try:
        cursor = mysql.connection.cursor()
        data = []
        account = []
        leg = []
        symbol = []
        type = []
        
        cursor.execute("SELECT Name FROM syslistDataLevels")
        data_items = cursor.fetchall()
        for item in data_items:
            data.append(item[0])
            
        cursor.execute("SELECT TradeAcctID FROM TradeAccount")
        accounts = cursor.fetchall()
        for item in accounts:
            account.append(item[0])
            
        cursor.execute("SELECT Name FROM syslistLegTypes")
        legs = cursor.fetchall()
        for item in legs:
            leg.append(item[0])

        cursor.execute("SELECT Symbol FROM syslistSymbols")
        symbols = cursor.fetchall()
        for item in symbols:
            symbol.append(item[0])

        cursor.execute("SELECT ActionName FROM syslistActionTypes")
        actions = cursor.fetchall()
        for item in actions:
            type.append(item[0])
            
        result = {'DATA': data, 'ACCOUNT': account, 'LEGS': leg, 'SYMBOL': symbol, 'TYPE': type}
        return result
    except Exception as e:
        print("Database connection failed due to {}".format(e))
        return jsonify({"message": "signin failed"})