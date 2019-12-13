import json
from flask_restful import Resource
from flask import Response, request
import pymysql as sql

class purchase(Resource):
    def __init__(self, db_params):
        self.host_ = db_params['host']
        self.db_ = db_params['db']
        self.pass_ = db_params['password']
        self.user_ = db_params['user']
        print(self.user_)

    def get(self):

            conn = sql.connect(user=self.user_, host=self.host_, db=self.db_, passwd=self.pass_,cursorclass=sql.cursors.DictCursor)
            cursor = conn.cursor()
            player = request.args.get('player')
            item = request.args.get('item')
            amount = request.args.get('amount')
            location = request.args.get('location')
            query0 = "SELECT * FROM Users WHERE ID=1;"
            cursor.execute(query0)
            row = cursor.fetchall()
            if item == "1":
                if int(row[0]["Influence"]) >= int(amount):
                    query1 = "UPDATE Map SET Influence = Influence + %s WHERE ID =  %s;"
                    query2 = "UPDATE Users SET Influence = Influence - %s WHERE ID = %s;"
                else:
                    return {"message":"Insufficient funds", "type":"error"}
            else:
                return {"message":"Unknown item", "type":"error"}

            cursor.execute(query1, (amount,location))
            conn.commit()
            cursor.execute(query2, (amount,player))
            conn.commit()
            query3 = "SELECT * FROM Users WHERE ID=1;"
            cursor.execute(query3)
            row = cursor.fetchall()
            response = Response(json.dumps(row), status=200, mimetype='application/json')

            return {"message":"Successfully purchased", "type":"success"}
