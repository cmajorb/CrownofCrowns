import json
from flask_restful import Resource
from flask import Response, request
import pymysql as sql

class purchaseunit(Resource):
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

            query0 = "SELECT * FROM Units ORDER BY RAND() LIMIT 3"
            query1 = "SELECT ActionTokens,Dentre FROM Users WHERE ID="+player
            cursor.execute(query0)
            trooprow = cursor.fetchall()
            cursor.execute(query1)
            userrow = cursor.fetchall()
            #if int(userrow[0]["ActionTokens"])>=1 and int(userrow[0]["ActionTokens"]):
            return trooprow
