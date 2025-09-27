"""Flask app with blueprint example (template)"""
from flask import Flask, Blueprint, jsonify, request
api = Blueprint('api', __name__)

@api.route('/echo', methods=['POST'])
def echo():
    return jsonify(request.get_json() or {})

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/api')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5002)
