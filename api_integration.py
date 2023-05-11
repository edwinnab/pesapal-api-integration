# #import Flask object from flask package
from flask import Flask, jsonify
import requests
import jsonpickle

# #create flask application instance
app = Flask(__name__)
# #API endpoint
BASE_URL = "https://cybqa.pesapal.com/pesapalv3"

# #create our decorator(converts a py function into a flask view function)
# # view function converts the function return value into an HTTP response to be displayed by the HTTP client
@app.route("/", methods=["GET"])
def api_testing():
    try:
        #JWT authntication
        
        #data from the api
        response = requests.get(BASE_URL)
        response.raise_for_status()
        data = list(enumerate(response))
        
        # iframe_url = data.get("iframe_url")
        
        # response_data = {
        #     "iframe_url": iframe_url
        # }
        #response in json
        return jsonpickle.encode(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
