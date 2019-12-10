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
            if item == "1":
                query_row_string = """
                UPDATE Map
                SET Influence = """ + amount + """
                WHERE ID = """ + location + """;
                """
            else:
                return "Unknown item"
            cursor.execute(query_row_string)
            conn.commit()
            query2 = "SELECT * FROM Map WHERE ID="+location+";"
            cursor.execute(query2)
            row = cursor.fetchall()
            response = Response(json.dumps(row), status=200, mimetype='application/json')
            return response
