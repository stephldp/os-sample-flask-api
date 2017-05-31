from flask import Flask
from api_v1 import blueprint as api_v1

application = Flask(__name__)
application.register_blueprint(api_v1)

if __name__ == "__main__":
    application.run(debug=True)
