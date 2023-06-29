from api.config import app, mysql
from flask import jsonify, request
import json
from datetime import datetime

@app.route("/mttools/main", methods=["POST"])
def main():
    try:
        filter_data = json.loads(request.form.get('filter'))
        cursor = mysql.connection.cursor()
        ACCOUNT = filter_data['ACCOUNT']
        DATA = filter_data['DATA']
        SYMBOL = filter_data['SYMBOL']
        TimeRange = filter_data['TIME_RANGE']
        OPEN_DATE = datetime.strptime(filter_data['OPEN_DATE'], '%Y-%m-%dT%H:%M:%S.%fZ').date()
        CLOSED_DATE = datetime.strptime(filter_data['CLOSED_DATE'], '%Y-%m-%dT%H:%M:%S.%fZ').date()
        start_time = datetime.strptime(TimeRange[0], "%H:%M:%S").time()
        end_time = datetime.strptime(TimeRange[1], "%H:%M:%S").time()
        TYPE = ['Buy', 'Sell'] if filter_data['TYPE'] == 'All' else [filter_data['TYPE']]
        LEGS = ['Multi Leg', 'Single Leg'] if filter_data['LEGS'] == 'All' else [filter_data['LEGS']]
        type_placeholders = ','.join(['%s'] * len(TYPE))
        legs_placeholders = ','.join(['%s'] * len(LEGS))

        ##  Widget 2
        query = "SELECT Symbol, SUM(TotalProfit) FROM vwClosedOrdersSummary WHERE AccountID = %s AND LegType IN ({}) AND ActionType IN ({}) AND TIME(ClosedDateTime) >= %s AND TIME(ClosedDateTime) <= %s AND DATE(ClosedDateTime) >= %s AND DATE(ClosedDateTime) <= %s GROUP BY Symbol ORDER BY TotalProfit DESC".format(legs_placeholders, type_placeholders)
        parameters = (ACCOUNT, *LEGS, *TYPE, start_time, end_time, OPEN_DATE, CLOSED_DATE)
        cursor.execute(query, parameters)
        AggSPRes = cursor.fetchall()
       
        ##  Widet 3
        query = "select ClosedDateTime, TotalLegs from vwClosedOrdersSummary WHERE AccountID = %s AND LegType IN ({}) AND Symbol = %s AND ActionType IN ({}) AND TIME(ClosedDateTime) >= %s AND TIME(ClosedDateTime) <= %s AND DATE(ClosedDateTime) >= %s AND DATE(ClosedDateTime) <= %s".format(legs_placeholders, type_placeholders)
        parameters = (ACCOUNT, *LEGS, SYMBOL, *TYPE, start_time, end_time, OPEN_DATE, CLOSED_DATE)
        cursor.execute(query, parameters)
        ChardRes = cursor.fetchall()

        ##  Widget 9
        query = "select sum(MarginRequired) AS `Margin Required`, sum(MarginRequired) AS `Max Drawdown` from vwClosedOrdersSummary WHERE AccountID = %s AND Symbol = %s AND LegType IN ({}) AND TIME(ClosedDateTime) >= %s AND TIME(ClosedDateTime) <= %s AND DATE(ClosedDateTime) >= %s AND DATE(ClosedDateTime) <= %s".format(legs_placeholders)
        parameters = (ACCOUNT, SYMBOL, *LEGS, start_time, end_time, OPEN_DATE, CLOSED_DATE)
        cursor.execute(query, parameters)
        MM = cursor.fetchall()[0]
        query = "select sum(TotalLots) AS `Total Multi Leg Lots`,sum(TotalUnits) AS `Total Multi Leg Units` from vwClosedOrdersSummary where (LegType = 'Multi Leg' AND AccountID = %s AND Symbol = %s AND TIME(ClosedDateTime) >= %s AND TIME(ClosedDateTime) <= %s AND DATE(ClosedDateTime) >= %s AND DATE(ClosedDateTime) <= %s) group by LegType"
        parameters = (ACCOUNT, SYMBOL, start_time, end_time, OPEN_DATE, CLOSED_DATE)
        cursor.execute(query, parameters)
        ML = cursor.fetchall()[0]
        query = "select sum(TotalLots) AS `Total Multi Leg Lots`,sum(TotalUnits) AS `Total Multi Leg Units` from vwClosedOrdersSummary where (LegType = 'Single Leg' AND AccountID = %s AND Symbol = %s AND TIME(ClosedDateTime) >= %s AND TIME(ClosedDateTime) <= %s AND DATE(ClosedDateTime) >= %s AND DATE(ClosedDateTime) <= %s) group by LegType"
        parameters = (ACCOUNT, SYMBOL, start_time, end_time, OPEN_DATE, CLOSED_DATE)
        cursor.execute(query, parameters)
        MS = cursor.fetchall()[0]
        overview = {'Margin Required:': round(float(MM[0]), 2), 'Max DrawDown:': round(float(MM[1]), 2), 'Total Multi Leg Lots Traded:': round(float(ML[0]), 2), 'Total Multi Leg Units Traded:': ML[1], 'Total Single Leg Lots Traded:': round(float(MS[0]), 2), 'Total Single Leg Units Traded:': MS[1] }
        
        result = {'SP': AggSPRes, 'overview': overview, 'ChartRES': ChardRes}
        return result
    
    except Exception as e:
        print("Database connection failed due to {}".format(e))
        return jsonify({"message": "signin failed"})
    

@app.route("/mttools/index", methods=["POST"])
def get_init():
    try:
        ##  Widget 1
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM vwOpenOrdersAggSL")
        AggSLRes = cursor.fetchall()

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
        result = {'COMBO':{'DATA': data, 'ACCOUNT': account, 'LEGS': leg, 'SYMBOL': symbol, 'TYPE': type}, 'SL': AggSLRes}
        return result
    
    except Exception as e:
        print("Database connection failed due to {}".format(e))
        return jsonify({"message": "signin failed"})