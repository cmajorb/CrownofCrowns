import json
from flask_restful import Resource
from flask import Response, request
import pymysql as sql

class get_map_locations(Resource):
    def __init__(self, db_params):
        self.host_ = db_params['host']
        self.db_ = db_params['db']
        self.pass_ = db_params['password']
        self.user_ = db_params['user']
        print(self.user_)

    def get(self):
            conn = sql.connect(user=self.user_, host=self.host_, db=self.db_, passwd=self.pass_,cursorclass=sql.cursors.DictCursor)
            cursor = conn.cursor()
            query_row_string = """SELECT t1.ID,t1.Group,t1.Color,t1.Influence,t1.Location1,t1.Location2,t1.Location3,t1.Location,t1.Owner,t1.Geography,t2.Color AS IColor FROM Map t1 JOIN Users t2 ON t2.ID = t1.Owner;"""
            cursor.execute(query_row_string)
            row = cursor.fetchall()
            response = Response(json.dumps(row), status=200, mimetype='application/json')
            return response
