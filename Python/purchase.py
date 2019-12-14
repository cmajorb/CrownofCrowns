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
            location = request.args.get('location')

            query0 = "SELECT * FROM GameState WHERE ID=1;"
            cursor.execute(query0)
            row1 = cursor.fetchall()
            if(int(row1[0]["CurrentTurn"]) != int(player)):
                return {"message":"It isn't your turn", "type":"error"}

            query = "SELECT * FROM Users WHERE ID="+player+";"
            cursor.execute(query)
            row = cursor.fetchall()
            query = "SELECT * FROM Map WHERE ID="+location+";"
            cursor.execute(query)
            locrow = cursor.fetchall()

            if item == "1":
                if int(row[0]["Influence"]) >= 1:
                    if(int(locrow[0]["Owner"])==int(player) or int(locrow[0]["Owner"])==0):
                        query1 = "UPDATE Map SET Influence = Influence + 1, Owner = %s WHERE ID =  %s;"
                        cursor.execute(query1, (player,location))
                        conn.commit()
                    else:
                        if int(locrow[0]["Influence"])==1:
                            query1 = "UPDATE Map SET Influence = 0, Owner = 0 WHERE ID =  %s;"
                            cursor.execute(query1, (location))
                            conn.commit()
                        else:
                            query1 = "UPDATE Map SET Influence = Influence - 1 WHERE ID =  %s;"
                            cursor.execute(query1, (location,))
                            conn.commit()
                    query2 = "UPDATE Users SET Influence = Influence - 1 WHERE ID = %s;"

                else:
                    return {"message":"Insufficient funds", "type":"error"}
            else:
                return {"message":"Unknown item", "type":"error"}


            cursor.execute(query2, (player,))
            conn.commit()
            query3 = "SELECT * FROM Users WHERE ID=1;"
            cursor.execute(query3)
            row = cursor.fetchall()
            response = Response(json.dumps(row), status=200, mimetype='application/json')

            return {"message":"Successfully purchased", "type":"success"}
