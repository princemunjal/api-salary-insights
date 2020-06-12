from flask import Blueprint, request, current_app as app
from flask_restful import Api, Resource
import pickle
import numpy as np

predict = Blueprint('predict',__name__)
api = Api(predict)
model = pickle.load(open('model.pkl', 'rb'))


class Predict(Resource):
	def post(self):
		try:
			response_data={"status":"failure", "message":"Internal Error. Please contact administrator."}
			response_cd=500
			request_data=request.get_json()
			exp = int(request_data["experience"])
			gender = int(request_data["gender"])
			jobtitle = int(request_data["jobTitle"])
			int_features = [exp, gender, jobtitle]
			final_features = [np.array(int_features)]
			prediction = model.predict(final_features)
			output = round(prediction[0], 2)
			response_data={"status":"success", "predictedSalary": output}
			response_cd=200
		except Exception as e:
			print(e)
			response_data={"status":"failure","message":"Internal Error. Please contact administartor.", "exception": str(e)}
		finally:
			return response_data,response_cd
	   
	   

    	
	def get(self):
		return {"message":"Prediction api is up!"}, 200

api.add_resource(Predict, "/")