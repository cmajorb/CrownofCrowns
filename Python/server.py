from flask import Flask,request,render_template
import json
from flask_cors import CORS, cross_origin
from argparse import ArgumentParser
from flask_restful import Api
from get_map_locations import get_map_locations
from purchase import purchase
from get_players import get_players
from get_player_stats import get_player_stats
from get_gamestate import get_gamestate
# Set ''default'' parameters for database connections
params = {'user': 'root',
          'host': 'db',
          'db': 'mysql',
          'password': 'root'}

# parse command line (or dockerfile) modifications to the default params
parser = ArgumentParser()
parser.add_argument('--user')
parser.add_argument('--host')
parser.add_argument('--db')
parser.add_argument('--password')
args = parser.parse_args()

# iterate all vars in namespace 'args' and set their param equiv to passed value
#for arg in vars(args):
    # print(arg, vars(args)[arg])
    #params[arg] = str(vars(args)[arg])

print(params)

app = Flask(__name__, static_folder='static')
api = Api(app)
CORS(app)

client = None


@app.route('/')
def main():
    return "<html><h1>Home</h1></html>"

api.add_resource(get_map_locations, '/get_map_locations',
                 methods=['GET'], resource_class_kwargs={"db_params": params})
api.add_resource(purchase, '/purchase',
                 methods=['GET'], resource_class_kwargs={"db_params": params})
api.add_resource(get_players, '/get_players',
                 methods=['GET'], resource_class_kwargs={"db_params": params})
api.add_resource(get_player_stats, '/get_player_stats',
                 methods=['GET'], resource_class_kwargs={"db_params": params})
api.add_resource(get_gamestate, '/get_gamestate',
                 methods=['GET'], resource_class_kwargs={"db_params": params})

app.debug = True

app.run(host='0.0.0.0', port='9000', threaded=True)
