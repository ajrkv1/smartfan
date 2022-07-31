from flask import Flask
from flask_restful import Api, Resource, reqparse
import transmitter
import ssl
app = Flask(__name__)
api = Api(app)

light = False
fan = 0

        
class Light(Resource):
    def get(self):
        return {'light':light}
    def post(self):
        global light
        light = not light
        transmitter.light()
        return self.get()

class Fan(Resource):
    
    def get(self):
        return {'fan': fan}
    
    def post(self):
        global fan
        parser = reqparse.RequestParser()
        parser.add_argument('power',type=int,help='Fan power level')

        args = parser.parse_args()

        if not 'power' in args:
            return args
        power = args['power']

        if not (0 <= power <= 3):
            return {'status':400, 'message':'power value not in 0-3 range'}
        
        transmitter.fan(power)
        return {'fan': power}

api.add_resource(Light,'/light')
api.add_resource(Fan,'/fan')

if __name__ == "__main__":
    app.run()
