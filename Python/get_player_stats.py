import json
from flask_restful import Resource
from flask import Response, request
import pymysql as sql

class get_player_stats(Resource):
    def __init__(self, db_params):
        self.host_ = db_params['host']
        self.db_ = db_params['db']
        self.pass_ = db_params['password']
        self.user_ = db_params['user']
        print(self.user_)

    def get(self):
            conn = sql.connect(user=self.user_, host=self.host_, db=self.db_, passwd=self.pass_,cursorclass=sql.cursors.DictCursor)
            cursor = conn.cursor()
            query_row_string = """SELECT * from Users WHERE ID=1;"""
            cursor.execute(query_row_string)
            row = cursor.fetchall()
            response = Response(json.dumps(row), status=200, mimetype='application/json')
            return response
