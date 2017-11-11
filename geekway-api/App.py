from flask import Flask, Blueprint
from flask_restful import Api
from flask_cors import CORS
from resources.LoginResource import LoginResource

app = Flask(__name__)
app.config['DEBUG'] = True

api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix='/api')

api.add_resource(LoginResource, '/login')

app.register_blueprint(api_bp)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run(host='0.0.0.0')