from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from predict_api import predict

# EB looks for an 'application' callable by default.
app = Flask(__name__)
CORS(app)
Api(app)
app.register_blueprint(predict, url_prefix="")




# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #application.debug = True
    app.run()