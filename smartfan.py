from flask import Flask
from flask_restful import Api, Resource

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
        return self.get()

class Fan(Resource):
    
    def get(self):
        return {'fan': fan}
    
    def post(self,fan_power):
        global fan
        fan = fan_power
        return {'fan': fan}

api.add_resource(Light,'/light')
api.add_resource(Fan,'/fan','/fan/<int:fan_power>')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
