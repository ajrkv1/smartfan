from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
light = False

class Light(Resource):
    
    def get(self):
        return {'light':light}
    def post(self):
        light = not light
        return self.get()


api.add_resource(Light,'/light')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
