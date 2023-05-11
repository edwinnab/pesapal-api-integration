# #import Flask object from flask package
from flask import Flask, jsonify
import requests

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
        
        data = response.json()
        iframe_url = data.get("iframe_url")
        
        response_data = {
            "iframe_url": iframe_url
        }
        #response in json
        return jsonify(response_data), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app.run(host='localhost', port=5000)