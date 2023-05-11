# #import Flask object from flask package
# # from flask import Flask, jsonify
# import requests

# #create flask application instance
# # app = Flask(__name__)
# #API endpoint
# BASE_URL = "https://cybqa.pesapal.com/pesapalv3"

# #GET request to the API
# response = requests.get(BASE_URL)
# #raise exception when not a 2xx response
# response.raise_for_status()
# data = response.json()

# def api_intergration():
#     if ( response.status_code != 204 and
#         response.headers["content-type"].strip().startswith("application/json")
#         ):
#         try:
#             return data
#         except ValueError:
#             print("not found")

# #create our decorator(converts a py function into a flask view function)
# # view function converts the function return value into an HTTP response to be displayed by the HTTP client
# @app.route("", methods=["GET"])
# def api_testing():
#     #JWT authntication
    
#     #data from the api
#     data = request.get_json()
#     #response in json
#     return jsonify(data), 200


#run the application
#export work with unix
#set FLASK_APP=api_integration.py
#run the app in the development mode
#set FLASK_ENV=development
#run the application using flask run

import requests
import json

response = requests.get("https://cybqa.pesapal.com/pesapalv3", 
                        headers={"Accept": "application/json"})

json_object = json.loads(response)
print(json_object)
# print(f"Status Code: {response.status_code}, Content: {response.json()}")
